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
    
    def update_message(self, message: str) -> None:
        """Update the status message
        
        Args:
            message: New status message
        """
        self.message = message
        self.update(Text(self.message, style="white on blue"))
