"""
Main TUI application using Textual framework
"""

from pathlib import Path
from typing import Optional
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from rich.markdown import Markdown

from notes_tui.widgets.tree_view import NotesTreeView
from notes_tui.widgets.note_view import NotePreview
from notes_tui.widgets.status_bar import StatusBar
from notes_tui.core.notes_manager import NotesManager
from notes_tui.core.config import Config


class NotesApp(Screen):
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
        status_bar.update(message)

    def action_new_note(self) -> None:
        """Action: Create a new note"""
        self.update_status("New note creation not yet implemented")

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
