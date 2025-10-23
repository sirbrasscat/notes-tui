"""
Status bar widget
"""

from textual.widgets import Static
from rich.text import Text


class StatusBar(Static):
    """Status bar widget for showing application status"""
    
    def __init__(self, **kwargs):
        """Initialize the status bar
        
        Args:
            **kwargs: Additional widget arguments
        """
        super().__init__("Ready", **kwargs)
        self.message = "Ready"
    
    def update(self, message: str) -> None:
        """Update the status message
        
        Args:
            message: New status message
        """
        self.message = message
        self.update_content()
    
    def update_content(self) -> None:
        """Update the rendered content"""
        self.update(Text(self.message, style="white on blue"))
