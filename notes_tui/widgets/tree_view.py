"""
Tree view widget for browsing notes directory
"""

from pathlib import Path
from typing import Optional
from textual.widgets import Tree
from textual.widgets.tree import TreeNode
from textual.message import Message
from notes_tui.core.notes_manager import NotesManager


class NotesTreeView(Tree):
    """File tree browser widget for notes"""
    
    # Tree widgets are focusable by default, but make it explicit
    can_focus = True
    
    class NoteSelected(Message):
        """Message emitted when a note is selected"""
        
        def __init__(self, note_path: Path) -> None:
            """Initialize the message
            
            Args:
                note_path: Path to the selected note
            """
            super().__init__()
            self.note_path = note_path
    
    def __init__(self, notes_manager: NotesManager, **kwargs):
        """Initialize the tree view
        
        Args:
            notes_manager: NotesManager instance
            **kwargs: Additional widget arguments
        """
        super().__init__("📁 Notes", **kwargs)
        self.notes_manager = notes_manager
        self.show_root = True
    
    def on_mount(self) -> None:
        """Handle mounting of the widget"""
        self.load_tree()
        # Expand root node by default
        self.root.expand()
    
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
    
    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Handle tree node selection
        
        Args:
            event: The tree node selected event
        """
        node_data = event.node.data
        
        if node_data and not node_data.get('is_dir', False):
            # It's a file, emit selection event
            note_path = Path(node_data['path'])
            self.post_message(self.NoteSelected(note_path))
    
    def refresh_tree(self) -> None:
        """Refresh the tree view to show updated files"""
        # Save expanded state
        expanded_nodes = []
        self._collect_expanded_nodes(self.root, expanded_nodes)
        
        # Clear existing tree
        self.root.remove_children()
        
        # Reload the tree
        self.load_tree()
        
        # Restore expanded state
        self._restore_expanded_nodes(self.root, expanded_nodes)
        
        # Always expand root
        self.root.expand()
    
    def _collect_expanded_nodes(self, node: TreeNode, expanded: list) -> None:
        """Collect paths of expanded nodes
        
        Args:
            node: Current tree node
            expanded: List to collect expanded node paths
        """
        if node.is_expanded and node.data:
            expanded.append(node.data.get('path'))
        
        for child in node.children:
            self._collect_expanded_nodes(child, expanded)
    
    def _restore_expanded_nodes(self, node: TreeNode, expanded: list) -> None:
        """Restore expanded state of nodes
        
        Args:
            node: Current tree node
            expanded: List of paths that should be expanded
        """
        if node.data and node.data.get('path') in expanded:
            node.expand()
        
        for child in node.children:
            self._restore_expanded_nodes(child, expanded)
