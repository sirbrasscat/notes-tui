# Development Guide for Notes TUI

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## Project Structure

```
notes-tui/
├── notes_tui/                 # Main package
│   ├── __main__.py           # Entry point for `python -m notes_tui`
│   ├── __init__.py           # Package initialization
│   ├── app.py                # Main Textual application
│   │
│   ├── core/                 # Core business logic
│   │   ├── notes_manager.py  # File operations and metadata
│   │   ├── config.py         # Configuration management
│   │   ├── search.py         # Search functionality
│   │   └── templates.py      # (Planned) Template engine
│   │
│   ├── widgets/              # Custom Textual widgets
│   │   ├── tree_view.py      # File browser tree
│   │   ├── note_view.py      # Note preview/display
│   │   └── status_bar.py     # Status bar widget
│   │
│   ├── screens/              # Different UI screens
│   │   ├── main_screen.py    # Main interface
│   │   ├── search_screen.py  # Search interface
│   │   └── editor_screen.py  # (Planned) Note editing
│   │
│   └── utils/                # Utility functions
│       └── helpers.py        # Helper functions
│
├── tests/                     # Test suite
│   ├── test_notes_manager.py
│   ├── test_search.py
│   └── test_config.py        # (Planned)
│
├── requirements.txt           # Python dependencies
├── setup.py                   # Installation script
├── README.md                  # Project documentation
├── DEVELOPMENT.md            # This file
├── LICENSE                    # MIT License
└── .gitignore               # Git ignore patterns
```

## Running the Application

```bash
# Run from current directory
python -m notes_tui

# Run with specific notes directory
python -m notes_tui --notes-dir /path/to/notes

# Run with debug mode
python -m notes_tui --debug

# Run development mode (for CSS/layout debugging)
python -m notes_tui --dev
```

## Key Bindings

| Key | Action | Status |
|-----|--------|--------|
| `↑/↓/←/→` | Navigate | ✅ Planned |
| `Enter` | Open/Select | ✅ Planned |
| `/` | Search | ⏳ In Progress |
| `n` | New note | ⏳ In Progress |
| `e` | Edit note | ⏳ In Progress |
| `d` | Delete note | ⏳ In Progress |
| `q` / `Ctrl+C` | Quit | ✅ Planned |
| `?` | Help | ⏳ In Progress |

## Architecture Overview

### Textual Application Structure

The app uses Textual's screen-based architecture:

1. **App** (in `app.py`)
   - Main application controller
   - Manages screens and event routing
   - Handles global keybindings

2. **Screens** (in `screens/`)
   - Main browsing screen with tree view and preview
   - Search results screen
   - Note editor screen (planned)

3. **Widgets** (in `widgets/`)
   - Reusable UI components
   - Custom event handlers
   - Styling with CSS

4. **Core Logic** (in `core/`)
   - Business logic separated from UI
   - File I/O operations
   - Search and filtering

### Data Flow

```
User Input
    ↓
Event Handler (in Widget/Screen)
    ↓
Action Method (in App/Screen)
    ↓
Core Logic (NotesManager, Search, etc.)
    ↓
File System
    ↓
Render Widget
    ↓
Display to Terminal
```

## Development Workflow

### 1. Creating a New Widget

```python
# In notes_tui/widgets/my_widget.py
from textual.widgets import Static
from rich.console import Console

class MyWidget(Static):
    """Description of my widget"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def render(self):
        return "Widget content"
```

### 2. Adding Core Functionality

```python
# In notes_tui/core/my_module.py
class MyManager:
    """Description of my manager"""
    
    def __init__(self, root_dir):
        self.root_dir = root_dir
    
    def do_something(self):
        # Implementation
        pass
```

### 3. Integrating with App

```python
# In notes_tui/app.py
def compose(self):
    yield MyWidget()

def on_mount(self):
    self.manager = MyManager(self.notes_dir)
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_notes_manager.py

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=notes_tui tests/
```

### Writing Tests

```python
# In tests/test_my_module.py
import pytest
from notes_tui.core.my_module import MyClass

@pytest.fixture
def my_fixture():
    return MyClass()

def test_my_function(my_fixture):
    result = my_fixture.do_something()
    assert result is not None
```

## Debugging

### Using Textual's Developer Console

```bash
python -m notes_tui --dev
```

Then press `Ctrl+Shift+D` to open the developer console.

### Logging

```python
import logging

logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

### Print Debugging

```python
from textual.logging import TextualHandler
import logging

# In your app's __init__
logging.basicConfig(handlers=[TextualHandler()])
```

## Code Style

### PEP 8 Compliance

Use `flake8` to check code style:

```bash
flake8 notes_tui/
```

### Formatting

Use `black` for code formatting:

```bash
black notes_tui/
```

### Type Hints

Always add type hints to functions:

```python
def my_function(param: str) -> int:
    """Function description"""
    return len(param)
```

## Dependencies

### Core Dependencies

- **textual**: TUI framework
- **rich**: Terminal formatting and rendering
- **pyyaml**: Configuration file parsing
- **click**: (For future CLI enhancements)
- **pygments**: Syntax highlighting

### Dev Dependencies

- **pytest**: Testing framework
- **pytest-asyncio**: Async testing support
- **black**: Code formatter
- **flake8**: Linter

## Features Roadmap

### Phase 1 (MVP - In Progress)
- [x] Project structure and setup
- [ ] Basic file browser
- [ ] Note preview with syntax highlighting
- [ ] Keyboard navigation
- [ ] Status bar and help

### Phase 2
- [ ] Note creation dialog
- [ ] Full-text search interface
- [ ] Note editing (in external editor)
- [ ] Delete functionality
- [ ] Confirm dialogs

### Phase 3
- [ ] Syntax highlighting for different markdown
- [ ] Theme customization
- [ ] Vim keybindings option
- [ ] Export to PDF/HTML
- [ ] Plugin system

### Phase 4 (Future)
- [ ] Git integration
- [ ] Sync with remote
- [ ] Collaborative editing (planned)
- [ ] Cloud backup

## Common Issues

### Import Errors

If you get import errors, make sure:
1. Virtual environment is activated
2. Dependencies are installed: `pip install -r requirements.txt`
3. You're in the project root directory

### Textual Not Running

Make sure your terminal supports the required features:
- 256 color support minimum
- Unicode support
- Sufficient size (at least 80x24)

Try running on a different terminal if issues persist.

### Port Already in Use

Notes TUI doesn't use ports by default. If you're getting this error, check if another application is conflicting.

## Contributing

1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Make your changes and commit: `git commit -m 'Add amazing feature'`
3. Run tests: `pytest`
4. Check code style: `flake8` and `black`
5. Push: `git push origin feature/amazing-feature`
6. Create Pull Request

## Resources

### Textual Documentation
- [Official Docs](https://textual.textualize.io/)
- [API Reference](https://textual.textualize.io/api/)
- [Tutorials](https://textual.textualize.io/tutorial/)

### Rich Documentation
- [Official Docs](https://rich.readthedocs.io/)
- [Console Guide](https://rich.readthedocs.io/en/latest/console.html)

### Python Resources
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Async/Await](https://docs.python.org/3/library/asyncio.html)

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues or questions:
1. Check existing GitHub issues
2. Create a new issue with details
3. Include terminal output and Python version

---

Happy coding! 🚀
