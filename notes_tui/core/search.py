"""
Search functionality for notes
"""

from pathlib import Path
from typing import List, Dict


class Search:
    """Handles full-text search in notes"""
    
    def __init__(self, root_dir: Path):
        """Initialize search
        
        Args:
            root_dir: Root directory for notes
        """
        self.root_dir = Path(root_dir)
    
    def search(self, query: str) -> List[Dict]:
        """Search for text in notes
        
        Args:
            query: Search query
            
        Returns:
            List of dictionaries containing search results
        """
        results = []
        
        for note_path in self.root_dir.rglob('*.md'):
            try:
                content = note_path.read_text(encoding='utf-8', errors='ignore')
                
                # Case-insensitive search
                if query.lower() in content.lower():
                    # Find line numbers containing the query
                    lines = content.split('\n')
                    matching_lines = []
                    
                    for i, line in enumerate(lines, 1):
                        if query.lower() in line.lower():
                            matching_lines.append((i, line.strip()))
                    
                    results.append({
                        'file': note_path,
                        'relative_path': note_path.relative_to(self.root_dir),
                        'matches': len(matching_lines),
                        'lines': matching_lines[:5]  # Show first 5 matches
                    })
            except Exception:
                pass
        
        return sorted(results, key=lambda x: x['matches'], reverse=True)
