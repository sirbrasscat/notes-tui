"""
Configuration management for Notes TUI
"""

from pathlib import Path
from typing import Dict, Any
import yaml


class Config:
    """Manages application configuration"""
    
    DEFAULT_CONFIG = {
        'app': {
            'theme': 'default',
            'font_size': 12,
        },
        'notes': {
            'categories': ['work', 'personal', 'journals', 'learning', 'budgets'],
        }
    }
    
    def __init__(self, notes_root: Path):
        """Initialize configuration
        
        Args:
            notes_root: Root directory for notes
        """
        self.notes_root = Path(notes_root)
        self.config_dir = self.notes_root / '.config'
        self.config_file = self.config_dir / 'config.yaml'
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults
        
        Returns:
            Configuration dictionary
        """
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return yaml.safe_load(f) or self.DEFAULT_CONFIG
            except Exception as e:
                print(f"Error loading config: {e}")
                return self.DEFAULT_CONFIG
        return self.DEFAULT_CONFIG
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value
        
        Args:
            key: Configuration key (dot notation supported)
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        
        return value if value is not None else default
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value
        
        Args:
            key: Configuration key (dot notation supported)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self._save_config()
    
    def _save_config(self) -> None:
        """Save configuration to file"""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        try:
            with open(self.config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except Exception as e:
            print(f"Error saving config: {e}")
