"""
Notes Manager - Core business logic for note operations
"""

from pathlib import Path
from typing import List, Dict, Optional
import yaml


class NotesManager:
    """Manages note file operations and metadata"""
    
    def __init__(self, root_dir: Path):
        """Initialize the notes manager
        
        Args:
            root_dir: Root directory containing all notes
        """
        self.root_dir = Path(root_dir)
        
        # Auto-discover categories from existing directories
        self.categories = {}
        if self.root_dir.exists():
            for item in self.root_dir.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    self.categories[item.name] = item
    
    def get_all_notes(self) -> List[Path]:
        """Get all markdown notes in the notes directory
        
        Returns:
            List of Path objects to all .md files
        """
        return list(self.root_dir.rglob('*.md'))
    
    def get_notes_by_category(self, category: str) -> List[Path]:
        """Get notes in a specific category
        
        Args:
            category: Category name (work, personal, etc)
            
        Returns:
            List of Path objects in that category
        """
        cat_dir = self.categories.get(category)
        if not cat_dir or not cat_dir.exists():
            return []
        return sorted(cat_dir.rglob('*.md'))
    
    def read_note(self, note_path: Path) -> str:
        """Read the content of a note
        
        Args:
            note_path: Path to the note file
            
        Returns:
            Content of the note as string
        """
        try:
            return note_path.read_text(encoding='utf-8')
        except Exception as e:
            return f"Error reading note: {e}"
    
    def get_directory_tree(self, directory: Optional[Path] = None) -> Dict:
        """Get a tree structure of the notes directory
        
        Args:
            directory: Directory to build tree for (defaults to root)
            
        Returns:
            Nested dictionary representing the directory structure
        """
        if directory is None:
            directory = self.root_dir
        
        tree = {
            'name': directory.name or 'notes',
            'path': str(directory),
            'is_dir': True,
            'children': []
        }
        
        try:
            items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
            
            for item in items:
                # Skip hidden files except .config
                if item.name.startswith('.') and item.name != '.config':
                    continue
                
                if item.is_dir():
                    tree['children'].append(self.get_directory_tree(item))
                elif item.suffix == '.md':
                    tree['children'].append({
                        'name': item.stem,
                        'path': str(item),
                        'is_dir': False,
                        'children': []
                    })
        except PermissionError:
            pass
        
        return tree
    
    def create_note(self, category: str, filename: str, content: str = "") -> Optional[Path]:
        """Create a new note
        
        Args:
            category: Category to create note in
            filename: Name of the note file (without .md)
            content: Initial content of the note
            
        Returns:
            Path to created note, or None if failed
        """
        cat_dir = self.categories.get(category)
        if not cat_dir:
            return None
        
        cat_dir.mkdir(parents=True, exist_ok=True)
        note_path = cat_dir / f"{filename}.md"
        
        try:
            note_path.write_text(content, encoding='utf-8')
            return note_path
        except Exception as e:
            print(f"Error creating note: {e}")
            return None
    
    def delete_note(self, note_path: Path) -> bool:
        """Delete a note file
        
        Args:
            note_path: Path to the note to delete
            
        Returns:
            True if successful, False otherwise
        """
        try:
            note_path.unlink()
            return True
        except Exception as e:
            print(f"Error deleting note: {e}")
            return False
    
    def search_notes(self, query: str) -> List[Path]:
        """Search for notes containing text
        
        Args:
            query: Search query
            
        Returns:
            List of Path objects matching the search
        """
        results = []
        for note_path in self.get_all_notes():
            try:
                content = note_path.read_text(encoding='utf-8', errors='ignore')
                if query.lower() in content.lower():
                    results.append(note_path)
            except Exception:
                pass
        return results
