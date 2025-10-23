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

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("ctrl+c", "quit", "Quit"),
        Binding("n", "new_note", "New", show=True),
        Binding("d", "delete_note", "Delete", show=True),
        Binding("e", "edit_note", "Edit", show=True),
        Binding("/", "search", "Search", show=True),
        Binding("?", "help", "Help", show=True),
    ]

    def __init__(self, notes_dir: Optional[Path] = None):
        """Initialize the Notes TUI application
        
        Args:
            notes_dir: Root directory for notes (defaults to current directory)
        """
        super().__init__()
        self.notes_dir = notes_dir or Path.cwd()
        self.config = Config(self.notes_dir)
        self.notes_manager = NotesManager(self.notes_dir)
        self.template_manager = TemplateManager()
        self.title = "Notes TUI - Personal Markdown Notebook"
        self.sub_title = f"Root: {self.notes_dir}"

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
        self.update_status("Ready")

    def update_status(self, message: str) -> None:
        """Update the status bar message"""
        status_bar = self.query_one("#status-bar", StatusBar)
        status_bar.update_message(message)

    def action_new_note(self) -> None:
        """Action: Create a new note"""
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
        
        # Create note path in the notes directory
        note_path = self.notes_dir / note_name
        
        # Check if file already exists
        if note_path.exists():
            self.update_status(f"Note '{note_name}' already exists!")
            return
        
        # Create the note from template
        success = self.template_manager.create_note_from_template(
            template_name=template_name,
            output_path=note_path
        )
        
        if success:
            self.update_status(f"Created note: {note_name}")
            # Refresh the tree view
            tree_view = self.query_one("#tree-pane", NotesTreeView)
            tree_view.refresh_tree()
        else:
            self.update_status(f"Failed to create note from template '{template_name}'")

    def action_delete_note(self) -> None:
        """Action: Delete the current note"""
        self.update_status("Delete feature not yet implemented")

    def action_edit_note(self) -> None:
        """Action: Edit the current note in external editor"""
        self.update_status("Edit feature not yet implemented")

    def action_search(self) -> None:
        """Action: Open search interface"""
        self.update_status("Search not yet implemented")

    def action_help(self) -> None:
        """Action: Show help dialog"""
        self.update_status("Help not yet implemented")


if __name__ == "__main__":
    app = NotesApp()
    app.run()
