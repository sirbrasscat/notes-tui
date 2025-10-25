"""
Editor Manager for Notes TUI

Handles launching external editors (nano, vim, etc.) for note editing.
"""

import subprocess
import shutil
from pathlib import Path
from typing import Optional, List, Tuple


class EditorManager:
    """Manages external editor launching and availability checking"""
    
    def __init__(self, config):
        """Initialize editor manager
        
        Args:
            config: Config object containing editor preferences
        """
        self.config = config
        self.default_editor = config.default_editor
        self.alternatives = config.alternative_editors
        self.editor_args = config.editor_args
    
    def is_editor_available(self, editor: str) -> bool:
        """Check if an editor is available on the system
        
        Args:
            editor: Editor command name (e.g., 'nano', 'vim')
            
        Returns:
            True if editor is found in PATH, False otherwise
        """
        return shutil.which(editor) is not None
    
    def get_editor_command(self) -> Tuple[Optional[str], List[str]]:
        """Get the best available editor command
        
        Returns:
            Tuple of (editor_path, additional_args) or (None, []) if no editor found
            
        Examples:
            >>> ('nano', [])
            >>> ('vim', ['+set', 'wrap'])
            >>> (None, [])  # No editor available
        """
        # Try default editor first
        if self.is_editor_available(self.default_editor):
            editor_path = shutil.which(self.default_editor)
            return (editor_path, self.editor_args)
        
        # Try alternatives
        for alt_editor in self.alternatives:
            if self.is_editor_available(alt_editor):
                editor_path = shutil.which(alt_editor)
                return (editor_path, self.editor_args)
        
        # No editor found
        return (None, [])
    
    def launch(self, file_path: Path, create_if_missing: bool = True) -> bool:
        """Launch editor for a file
        
        Args:
            file_path: Path to file to edit
            create_if_missing: Create file if it doesn't exist
            
        Returns:
            True if editor launched and exited successfully, False otherwise
            
        Raises:
            FileNotFoundError: If file doesn't exist and create_if_missing is False
            RuntimeError: If no suitable editor is available
        """
        file_path = Path(file_path)
        
        # Check if file exists
        if not file_path.exists():
            if create_if_missing:
                # Create parent directories if needed
                file_path.parent.mkdir(parents=True, exist_ok=True)
                # Create empty file
                file_path.touch()
            else:
                raise FileNotFoundError(f"File does not exist: {file_path}")
        
        # Get editor command
        editor_cmd, editor_args = self.get_editor_command()
        
        if editor_cmd is None:
            available = ', '.join([self.default_editor] + self.alternatives)
            raise RuntimeError(
                f"No suitable editor found. Please install one of: {available}"
            )
        
        # Build command
        cmd = [editor_cmd] + editor_args + [str(file_path)]
        
        try:
            # Launch editor and wait for it to exit
            # We use subprocess.run instead of Popen because we want to:
            # 1. Block until editor exits (synchronous)
            # 2. Return editor's exit code
            # 3. Give editor full control of terminal
            result = subprocess.run(cmd, check=False)
            
            # Return True if editor exited successfully (exit code 0)
            return result.returncode == 0
            
        except KeyboardInterrupt:
            # User pressed Ctrl+C, that's fine
            return True
        except Exception as e:
            # Log error but don't crash
            print(f"Error launching editor: {e}")
            return False
    
    def get_available_editors(self) -> List[str]:
        """Get list of all available editors on the system
        
        Returns:
            List of available editor names
        """
        available = []
        
        # Check default
        if self.is_editor_available(self.default_editor):
            available.append(self.default_editor)
        
        # Check alternatives
        for editor in self.alternatives:
            if self.is_editor_available(editor):
                available.append(editor)
        
        return available
    
    def __repr__(self) -> str:
        """String representation"""
        available = self.get_available_editors()
        if available:
            return f"EditorManager(default={self.default_editor}, available={available})"
        else:
            return f"EditorManager(default={self.default_editor}, available=[])"
