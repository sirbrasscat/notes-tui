"""
Tree view widget for browsing notes directory
"""

from pathlib import Path
from typing import Optional
from textual.widgets import Tree
from textual.widgets.tree import TreeNode
from notes_tui.core.notes_manager import NotesManager


class NotesTreeView(Tree):
    """File tree browser widget for notes"""
    
    def __init__(self, notes_manager: NotesManager, **kwargs):
        """Initialize the tree view
        
        Args:
            notes_manager: NotesManager instance
            **kwargs: Additional widget arguments
        """
        super().__init__("📁 Notes", **kwargs)
        self.notes_manager = notes_manager
    
    def on_mount(self) -> None:
        """Handle mounting of the widget"""
        self.load_tree()
    
    def load_tree(self) -> None:
        """Load the file tree"""
        root = self.root
        tree = self.notes_manager.get_directory_tree()
        self._load_tree_node(root, tree)
    
    def _load_tree_node(self, parent: TreeNode, tree_data: dict) -> None:
        """Recursively load tree nodes
        
        Args:
            parent: Parent tree node
            tree_data: Tree data dictionary
        """
        for child in tree_data.get('children', []):
            if child['is_dir']:
                icon = "📁"
                label = f"{icon} {child['name']}"
            else:
                icon = "📄"
                label = f"{icon} {child['name']}"
            
            node = parent.add(label, data=child)
            
            if child['is_dir'] and child['children']:
                self._load_tree_node(node, child)
