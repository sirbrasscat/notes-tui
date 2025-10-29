"""
Main TUI application using Textual framework
"""

from pathlib import Path
from typing import Optional
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from rich.markdown import Markdown

from notes_tui.widgets.tree_view import NotesTreeView
from notes_tui.widgets.note_view import NotePreview
from notes_tui.widgets.status_bar import StatusBar
from notes_tui.widgets.template_dialog import TemplateSelectionDialog
from notes_tui.widgets.input_dialog import InputDialog
from notes_tui.core.notes_manager import NotesManager
from notes_tui.core.config import Config
from notes_tui.core.template_manager import TemplateManager
from notes_tui.core.editor_manager import EditorManager


class NotesApp(App):
    """Main Notes TUI Application"""
    
    CSS = """
    Screen {
        layout: vertical;
    }
    
    #main-container {
        height: 1fr;
        layout: horizontal;
    }
    
    #tree-pane {
        width: 30%;
        border: solid $primary;
    }
    
    #note-pane {
        width: 1fr;
        border: solid $accent;
    }
    
    #status-bar {
        height: 1;
        background: $panel;
    }
    """

    # Keybindings - defined at class level for Textual to pick them up
    BINDINGS = [
        # Navigation
        Binding("tab", "focus_next", "Next Panel", show=True),
        Binding("shift+tab", "focus_previous", "Prev Panel", show=False),
        
        # Quick Capture
        Binding("n", "new_note", "New", show=True),
        Binding("shift+n", "template_note", "Template", show=True),
        Binding("j", "quick_journal", "Journal", show=True),
        
        # File Operations
        Binding("e", "edit_note", "Edit", show=True),
        Binding("d", "delete_note", "Delete", show=True),
        
        # UI Controls
        Binding("p", "toggle_preview", "Preview", show=True),
        Binding("r", "refresh", "Refresh", show=True),
        Binding("/", "search", "Search", show=True),
        Binding("?", "help", "Help", show=True),
        
        # Quit
        Binding("q", "quit", "Quit", show=True),
        Binding("ctrl+c", "quit", "Quit", show=False),
    ]

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize the Notes TUI application
        
        Args:
            config_path: Optional path to custom config file
        """
        super().__init__()
        
        # Load configuration
        self.config = Config(config_path)
        
        # Initialize managers using config
        self.notes_dir = self.config.notes_directory
        self.notes_manager = NotesManager(self.notes_dir)
        self.template_manager = TemplateManager(self.config)
        self.editor_manager = EditorManager(self.config)
        
        # Set app title and subtitle
        self.title = "Notes TUI - Personal Markdown Notebook"
        self.sub_title = f"Root: {self.notes_dir}"
        
        # Current selected note
        self.current_note: Optional[Path] = None
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        
        with Horizontal(id="main-container"):
            yield NotesTreeView(
                notes_manager=self.notes_manager,
                id="tree-pane"
            )
            yield NotePreview(id="note-pane")
        
        yield StatusBar(id="status-bar")
        yield Footer()

    def on_mount(self) -> None:
        """Handle mounting of the app"""
        self.update_status("Ready - Press 'n' for new note, '?' for help")
        # Set focus to tree view for immediate navigation
        tree_view = self.query_one("#tree-pane", NotesTreeView)
        tree_view.focus()
    
    def on_notes_tree_view_note_selected(self, event: NotesTreeView.NoteSelected) -> None:
        """Handle note selection from tree view
        
        Args:
            event: Note selection event
        """
        self.current_note = event.note_path
        
        # Load note in preview pane
        note_preview = self.query_one("#note-pane", NotePreview)
        note_preview.load_note(event.note_path)
        
        # Update status
        rel_path = event.note_path.relative_to(self.notes_dir)
        self.update_status(f"Viewing: {rel_path}")

    def update_status(self, message: str) -> None:
        """Update the status bar message"""
        status_bar = self.query_one("#status-bar", StatusBar)
        status_bar.update_message(message)

    def action_new_note(self) -> None:
        """Action: Quick capture - create note with default template"""
        self.update_status("Quick note - enter name...")
        
        # Show input dialog for note name
        self.push_screen(
            InputDialog(
                title="Quick Note",
                prompt="Enter note name:",
                placeholder="my-quick-note"
            ),
            self._create_quick_note
        )
    
    def _create_quick_note(self, note_name: Optional[str]) -> None:
        """Create a quick note with default template
        
        Args:
            note_name: Name for the new note
        """
        if note_name is None:
            self.update_status("Note creation cancelled")
            return
        
        # Ensure .md extension
        if not note_name.endswith(".md"):
            note_name = f"{note_name}.md"
        
        # Get default category and template from config
        default_category = self.config.get('quick_capture.default_category', 'personal')
        default_template = self.config.get('quick_capture.default_template', 'general_note.md')
        
        # Create note path in the appropriate category
        category_dir = self.notes_dir / default_category
        category_dir.mkdir(parents=True, exist_ok=True)
        note_path = category_dir / note_name
        
        # Check if file already exists
        if note_path.exists():
            self.update_status(f"Note '{note_name}' already exists! Opening in editor...")
            # If it exists, just open it
            self._open_in_editor(note_path)
            return
        
        # Create the note from default template
        success = self.template_manager.create_note_from_template(
            template_name=default_template,
            output_path=note_path
        )
        
        if success:
            self.update_status(f"Created: {note_name}")
            self._open_in_editor(note_path)
        else:
            self.update_status(f"Failed to create note - opening blank file...")
            # If template fails, just create empty file and open
            note_path.touch()
            self._open_in_editor(note_path)
    
    def action_template_note(self) -> None:
        """Action: Create note with template selection (original behavior)"""
        self.update_status("Select a template...")
        
        # Get available templates
        templates = self.template_manager.list_templates()
        
        if not templates:
            self.update_status("No templates found!")
            return
        
        # Show template selection dialog
        self.push_screen(
            TemplateSelectionDialog(templates),
            self._on_template_selected
        )
    
    def _on_template_selected(self, template_name: Optional[str]) -> None:
        """Callback when template is selected
        
        Args:
            template_name: Name of selected template or None if cancelled
        """
        if template_name is None:
            self.update_status("Note creation cancelled")
            return
        
        self.update_status(f"Template '{template_name}' selected. Enter note name...")
        
        # Show input dialog for note name
        self.push_screen(
            InputDialog(
                title="Create New Note",
                prompt="Enter note name (without .md extension):",
                placeholder="my-note-name"
            ),
            lambda note_name: self._create_note_file(template_name, note_name)
        )
    
    def _create_note_file(self, template_name: str, note_name: Optional[str]) -> None:
        """Create the note file from template
        
        Args:
            template_name: Name of the template to use
            note_name: Name for the new note
        """
        if note_name is None:
            self.update_status("Note creation cancelled")
            return
        
        # Ensure .md extension
        if not note_name.endswith(".md"):
            note_name = f"{note_name}.md"
        
        # Get default category from config
        default_category = self.config.get('quick_capture.default_category', 'personal')
        
        # Create note path in the appropriate category
        category_dir = self.notes_dir / default_category
        category_dir.mkdir(parents=True, exist_ok=True)
        note_path = category_dir / note_name
        
        # Check if file already exists
        if note_path.exists():
            self.update_status(f"Note '{note_name}' already exists! Opening...")
            self._open_in_editor(note_path)
            return
        
        # Create the note from template
        success = self.template_manager.create_note_from_template(
            template_name=template_name,
            output_path=note_path
        )
        
        if success:
            self.update_status(f"Created: {note_name}")
            self._open_in_editor(note_path)
        else:
            self.update_status(f"Failed to create note from template '{template_name}'")

    def action_delete_note(self) -> None:
        """Action: Delete the current note"""
        self.update_status("Delete feature not yet implemented")
    
    def _open_in_editor(self, note_path: Path) -> None:
        """Open a note in external editor and refresh UI
        
        Args:
            note_path: Path to note file
        """
        try:
            # Suspend TUI to launch editor
            with self.suspend():
                self.update_status(f"Opening {note_path.name} in editor...")
                success = self.editor_manager.launch(note_path)
            
            if success:
                # Refresh the tree view
                tree_view = self.query_one("#tree-pane", NotesTreeView)
                tree_view.refresh_tree()
                
                # Set as current note
                self.current_note = note_path
                
                # Refresh preview
                note_preview = self.query_one("#note-pane", NotePreview)
                note_preview.load_note(note_path)
                
                self.update_status(f"Saved: {note_path.name}")
            else:
                self.update_status("Editor exited with error")
                
        except Exception as e:
            self.update_status(f"Error launching editor: {e}")
    
    def action_quick_journal(self) -> None:
        """Action: Open today's journal instantly"""
        from datetime import datetime
        
        # Get today's date
        today = datetime.now().strftime("%Y-%m-%d")
        journal_name = f"{today}.md"
        
        # Journal goes in journals/daily/ to match existing structure
        journal_dir = self.notes_dir / "journals" / "daily"
        journal_dir.mkdir(parents=True, exist_ok=True)
        journal_path = journal_dir / journal_name
        
        # If journal doesn't exist, create from template
        if not journal_path.exists():
            # Try to use daily_journal template with proper variables
            template_name = "daily_journal"  # Don't include .md extension
            
            # Provide variables for template
            variables = {
                'title': f'Daily Journal - {today}',
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'tags': "['daily', 'journal']",
                'status': 'active'
            }
            
            success = self.template_manager.create_note_from_template(
                template_name=template_name,
                output_path=journal_path,
                variables=variables
            )
            
            if not success:
                # If template doesn't exist or fails, create basic journal entry
                journal_path.write_text(f"# Daily Journal - {today}\n\n")
            
            self.update_status(f"Created journal: {today}")
        else:
            self.update_status(f"Opening journal: {today}")
        
        # Open in editor
        self._open_in_editor(journal_path)

    def action_edit_note(self) -> None:
        """Action: Edit the current note in external editor"""
        if self.current_note is None:
            self.update_status("No note selected")
            return
        
        if not self.current_note.exists():
            self.update_status(f"Note does not exist: {self.current_note}")
            return
        
        try:
            # Suspend the TUI to launch editor
            with self.suspend():
                self.update_status(f"Opening {self.current_note.name} in editor...")
                success = self.editor_manager.launch(self.current_note)
                
            if success:
                self.update_status(f"Edited: {self.current_note.name}")
                # Refresh the preview
                note_preview = self.query_one("#note-pane", NotePreview)
                note_preview.load_note(self.current_note)
            else:
                self.update_status("Editor exited with error")
                
        except Exception as e:
            self.update_status(f"Error launching editor: {e}")

    def action_search(self) -> None:
        """Action: Open search interface"""
        self.update_status("Search not yet implemented")
    
    def action_toggle_preview(self) -> None:
        """Action: Toggle preview pane visibility"""
        note_pane = self.query_one("#note-pane")
        note_pane.display = not note_pane.display
        status = "shown" if note_pane.display else "hidden"
        self.update_status(f"Preview pane {status}")
    
    def action_refresh(self) -> None:
        """Action: Refresh tree view"""
        tree_view = self.query_one("#tree-pane", NotesTreeView)
        tree_view.refresh_tree()
        self.update_status("Tree view refreshed")

    def action_help(self) -> None:
        """Action: Show help dialog"""
        help_text = "Notes TUI - Keybindings:\n\n"
        help_text += "  n - Quick note (default template)\n"
        help_text += "  N - New note (choose template)\n"
        help_text += "  j - Today's journal\n"
        help_text += f"  {self.config.get_keybinding('edit_note')} - Edit selected note\n"
        help_text += f"  {self.config.get_keybinding('delete_note')} - Delete selected note\n"
        help_text += f"  {self.config.get_keybinding('search')} - Search notes\n"
        help_text += f"  {self.config.get_keybinding('toggle_preview')} - Toggle preview pane\n"
        help_text += f"  {self.config.get_keybinding('refresh')} - Refresh tree view\n"
        help_text += "  Tab - Switch panels\n"
        help_text += f"  {self.config.get_keybinding('quit')} - Quit application\n"
        self.update_status(help_text.replace('\n', ' | '))


if __name__ == "__main__":
    app = NotesApp()
    app.run()
