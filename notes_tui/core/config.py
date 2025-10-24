"""
Configuration management for Notes TUI
"""

from pathlib import Path
from typing import Dict, Any, Optional
import yaml
import os


class Config:
    """Manages application configuration"""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize configuration
        
        Args:
            config_path: Optional path to custom config file.
                        If None, will use default locations:
                        1. ~/.config/notes-tui/config.yaml (user config)
                        2. <app_dir>/config/default.yaml (default config)
        """
        self.config = self._load_config(config_path)
        self._validate_config()
    
    def _load_config(self, config_path: Optional[Path] = None) -> Dict[str, Any]:
        """Load configuration from file
        
        Args:
            config_path: Optional custom config file path
            
        Returns:
            Configuration dictionary
        """
        # Try custom config path first
        if config_path and config_path.exists():
            return self._read_yaml(config_path)
        
        # Try user config (~/.config/notes-tui/config.yaml)
        user_config = Path.home() / '.config' / 'notes-tui' / 'config.yaml'
        if user_config.exists():
            return self._read_yaml(user_config)
        
        # Fall back to default config
        app_dir = Path(__file__).parent.parent.parent
        default_config = app_dir / 'config' / 'default.yaml'
        if default_config.exists():
            return self._read_yaml(default_config)
        
        raise FileNotFoundError(
            "No configuration file found. Expected one of:\n"
            f"  - {config_path}\n"
            f"  - {user_config}\n"
            f"  - {default_config}"
        )
    
    def _read_yaml(self, path: Path) -> Dict[str, Any]:
        """Read and parse YAML file
        
        Args:
            path: Path to YAML file
            
        Returns:
            Parsed YAML as dictionary
        """
        try:
            with open(path, 'r') as f:
                config = yaml.safe_load(f)
                if not isinstance(config, dict):
                    raise ValueError(f"Config file must contain a dictionary, got {type(config)}")
                return self._expand_paths(config)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML in {path}: {e}")
        except Exception as e:
            raise ValueError(f"Error reading config from {path}: {e}")
    
    def _expand_paths(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Expand ~ and environment variables in path strings
        
        Args:
            config: Configuration dictionary
            
        Returns:
            Configuration with expanded paths
        """
        expanded = {}
        for key, value in config.items():
            if isinstance(value, dict):
                expanded[key] = self._expand_paths(value)
            elif isinstance(value, str) and ('/' in value or '~' in value):
                # Expand ~ and environment variables
                expanded[key] = os.path.expandvars(os.path.expanduser(value))
            else:
                expanded[key] = value
        return expanded
    
    def _validate_config(self) -> None:
        """Validate configuration and check required paths exist"""
        # Check required fields
        required_fields = ['notes_directory', 'templates_directory']
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Required configuration field missing: {field}")
        
        # Check notes directory exists
        notes_dir = Path(self.config['notes_directory'])
        if not notes_dir.exists():
            raise ValueError(f"Notes directory does not exist: {notes_dir}")
        
        # Check templates directory exists
        templates_dir = Path(self.config['templates_directory'])
        if not templates_dir.exists():
            raise ValueError(f"Templates directory does not exist: {templates_dir}")
        
        # Validate editor configuration
        if 'editor' not in self.config:
            raise ValueError("Editor configuration missing")
        if 'default' not in self.config['editor']:
            raise ValueError("Default editor not specified in configuration")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation
        
        Args:
            key: Configuration key (dot notation supported, e.g., 'editor.default')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
            
        Examples:
            >>> config.get('notes_directory')
            '/home/user/notes'
            >>> config.get('editor.default')
            'nano'
            >>> config.get('ui.tree_width', 30)
            30
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    @property
    def notes_directory(self) -> Path:
        """Get notes directory as Path object"""
        return Path(self.config['notes_directory'])
    
    @property
    def templates_directory(self) -> Path:
        """Get templates directory as Path object"""
        return Path(self.config['templates_directory'])
    
    @property
    def default_editor(self) -> str:
        """Get default editor command"""
        return self.config['editor']['default']
    
    @property
    def alternative_editors(self) -> list:
        """Get list of alternative editors"""
        return self.config['editor'].get('alternatives', [])
    
    @property
    def editor_args(self) -> list:
        """Get additional editor arguments"""
        return self.config['editor'].get('args', [])
    
    def get_keybinding(self, action: str) -> str:
        """Get keybinding for an action
        
        Args:
            action: Action name (e.g., 'new_note', 'edit_note')
            
        Returns:
            Key binding string
        """
        return self.config.get('keybindings', {}).get(action, '')
    
    def __repr__(self) -> str:
        """String representation of config"""
        return f"Config(notes={self.notes_directory}, templates={self.templates_directory})"
