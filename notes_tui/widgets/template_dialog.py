"""
Template selection dialog widget
"""

from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.containers import Container, Vertical
from textual.widgets import Static, Button, Label, ListView, ListItem
from textual.binding import Binding
from typing import Optional, List, Dict, Callable


class TemplateSelectionDialog(ModalScreen[Optional[str]]):
    """Modal dialog for selecting a template"""
    
    CSS = """
    TemplateSelectionDialog {
        align: center middle;
    }
    
    #dialog-container {
        width: 60;
        height: 20;
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
    }
    
    #template-list {
        height: 12;
        border: solid $primary;
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
        Binding("enter", "select", "Select", show=True),
    ]
    
    def __init__(self, templates: List[Dict[str, str]], **kwargs):
        """Initialize the template selection dialog
        
        Args:
            templates: List of template dicts with name, filename, path, description
        """
        super().__init__(**kwargs)
        self.templates = templates
        self.selected_template: Optional[str] = None
    
    def compose(self) -> ComposeResult:
        """Create child widgets"""
        with Container(id="dialog-container"):
            yield Label("Select a Template", id="dialog-title")
            
            with ListView(id="template-list"):
                for template in self.templates:
                    label_text = f"{template['name']}\n  → {template['description']}"
                    yield ListItem(Label(label_text))
            
            with Container(id="button-container"):
                yield Button("Select", variant="primary", id="select-btn", classes="dialog-button")
                yield Button("Cancel", variant="default", id="cancel-btn", classes="dialog-button")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press"""
        if event.button.id == "select-btn":
            self.action_select()
        elif event.button.id == "cancel-btn":
            self.action_cancel()
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle list item selection"""
        # Store the selected index
        list_view = self.query_one("#template-list", ListView)
        self.selected_template = self.templates[event.list_view.index]["name"]
    
    def action_select(self) -> None:
        """Action: Select the current template"""
        list_view = self.query_one("#template-list", ListView)
        if list_view.index is not None:
            selected_name = self.templates[list_view.index]["name"]
            self.dismiss(selected_name)
        else:
            # No selection made
            self.dismiss(None)
    
    def action_cancel(self) -> None:
        """Action: Cancel the dialog"""
        self.dismiss(None)
