"""
Input dialog widget for note creation
"""

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.containers import Container
from textual.widgets import Static, Button, Label, Input
from textual.binding import Binding
from typing import Optional


class InputDialog(ModalScreen[Optional[str]]):
    """Modal dialog for text input"""
    
    CSS = """
    InputDialog {
        align: center middle;
    }
    
    #dialog-container {
        width: 50;
        height: 12;
        border: thick $background 80%;
        background: $surface;
        padding: 1;
    }
    
    #dialog-title {
        width: 100%;
        content-align: center middle;
        text-style: bold;
        background: $primary;
        color: $text;
        padding: 1;
        margin-bottom: 1;
    }
    
    #dialog-input {
        width: 100%;
        margin: 1 0;
    }
    
    #button-container {
        width: 100%;
        height: 3;
        layout: horizontal;
        align: center middle;
    }
    
    .dialog-button {
        margin: 0 1;
    }
    """
    
    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
        Binding("enter", "submit", "Submit", show=False),
    ]
    
    def __init__(self, title: str, prompt: str, placeholder: str = "", **kwargs):
        """Initialize the input dialog
        
        Args:
            title: Dialog title
            prompt: Prompt text
            placeholder: Placeholder text for input
        """
        super().__init__(**kwargs)
        self.dialog_title = title
        self.prompt_text = prompt
        self.placeholder = placeholder
    
    def compose(self) -> ComposeResult:
        """Create child widgets"""
        with Container(id="dialog-container"):
            yield Label(self.dialog_title, id="dialog-title")
            yield Label(self.prompt_text)
            yield Input(placeholder=self.placeholder, id="dialog-input")
            
            with Container(id="button-container"):
                yield Button("Create", variant="primary", id="submit-btn", classes="dialog-button")
                yield Button("Cancel", variant="default", id="cancel-btn", classes="dialog-button")
    
    def on_mount(self) -> None:
        """Focus the input when mounted"""
        self.query_one("#dialog-input", Input).focus()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press"""
        if event.button.id == "submit-btn":
            self.action_submit()
        elif event.button.id == "cancel-btn":
            self.action_cancel()
    
    def action_submit(self) -> None:
        """Action: Submit the input"""
        input_widget = self.query_one("#dialog-input", Input)
        value = input_widget.value.strip()
        
        if value:
            self.dismiss(value)
        else:
            # Show error or just dismiss
            self.dismiss(None)
    
    def action_cancel(self) -> None:
        """Action: Cancel the dialog"""
        self.dismiss(None)
