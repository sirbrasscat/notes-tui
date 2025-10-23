"""
Note preview widget for displaying note content
"""

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
        self.current_note = None
    
    def render(self) -> Text | Markdown:
        """Render the note content
        
        Returns:
            Rendered markdown or text content
        """
        if self.current_note is None:
            return Text("Select a note to view its content", style="dim")
        
        return Markdown(self.current_note)
    
    def set_note(self, content: str) -> None:
        """Set the note content to display
        
        Args:
            content: Markdown content to display
        """
        self.current_note = content
        self.refresh()
