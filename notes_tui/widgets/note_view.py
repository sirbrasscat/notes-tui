"""
Note preview widget for displaying note content
"""

from pathlib import Path
from typing import Optional
from textual.widgets import Static
from textual.containers import ScrollableContainer
from rich.markdown import Markdown
from rich.text import Text


class NotePreview(Static):
    """Widget for previewing markdown notes"""
    
    def __init__(self, **kwargs):
        """Initialize the note preview widget
        
        Args:
            **kwargs: Additional widget arguments
        """
        super().__init__(**kwargs)
        self.current_note_content: Optional[str] = None
        self.current_note_path: Optional[Path] = None
    
    def render(self) -> Text | Markdown:
        """Render the note content
        
        Returns:
            Rendered markdown or text content
        """
        if self.current_note_content is None:
            return Text("Select a note to view its content", style="dim italic")
        
        return Markdown(self.current_note_content, code_theme="monokai")
    
    def set_note(self, content: str) -> None:
        """Set the note content to display
        
        Args:
            content: Markdown content to display
        """
        self.current_note_content = content
        self.refresh()
    
    def load_note(self, note_path: Path) -> None:
        """Load and display a note from file
        
        Args:
            note_path: Path to the note file
        """
        try:
            self.current_note_path = note_path
            content = note_path.read_text(encoding='utf-8')
            self.set_note(content)
        except Exception as e:
            self.set_note(f"# Error Loading Note\n\nCould not load: {note_path}\n\nError: {e}")
    
    def clear(self) -> None:
        """Clear the preview"""
        self.current_note_content = None
        self.current_note_path = None
        self.refresh()
