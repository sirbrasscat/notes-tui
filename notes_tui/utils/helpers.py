"""
Utility helper functions
"""

from pathlib import Path
from typing import List


def get_relative_path(file_path: Path, base_path: Path) -> str:
    """Get relative path from base
    
    Args:
        file_path: File path
        base_path: Base directory path
        
    Returns:
        Relative path as string
    """
    try:
        return str(file_path.relative_to(base_path))
    except ValueError:
        return str(file_path)


def format_file_size(bytes: int) -> str:
    """Format file size for display
    
    Args:
        bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} TB"


def get_file_count(directory: Path) -> int:
    """Count markdown files in directory
    
    Args:
        directory: Directory to count files in
        
    Returns:
        Number of markdown files
    """
    return len(list(directory.rglob('*.md')))
