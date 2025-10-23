# Quick Start Guide - Notes TUI

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the App

### Basic Usage
```bash
python -m notes_tui
```

### With Custom Notes Directory
```bash
python -m notes_tui --notes-dir /path/to/your/notes
```

### Development Mode
```bash
python -m notes_tui --dev
```

## Key Features (Current & Planned)

✅ = Ready | 🔄 = In Development | ⏳ = Planned

| Feature | Status | Hotkey |
|---------|--------|--------|
| Navigate files | ✅ | Arrow keys |
| View notes | ✅ | Enter |
| Search notes | 🔄 | `/` |
| Create note | ⏳ | `n` |
| Delete note | ⏳ | `d` |
| Edit note | ⏳ | `e` |
| Quit app | ✅ | `q` / `Ctrl+C` |
| Help | ⏳ | `?` |

## Project Structure

```
notes_tui/
├── app.py              # Main application
├── core/
│   ├── notes_manager.py   # File operations
│   ├── config.py          # Configuration
│   └── search.py          # Search functionality
├── widgets/
│   ├── tree_view.py       # File browser
│   ├── note_view.py       # Note display
│   └── status_bar.py      # Status info
└── utils/
    └── helpers.py         # Helper functions
```

## Next Steps

1. **Review Documentation**
   - [README.md](README.md) - Full project overview
   - [DEVELOPMENT.md](DEVELOPMENT.md) - Development guide
   - [ECOSYSTEM.md](ECOSYSTEM.md) - Integration with web interface

2. **Run Tests**
   ```bash
   pytest tests/
   ```

3. **Explore the Code**
   - Start with `notes_tui/app.py`
   - Check `notes_tui/core/` for business logic
   - Look at `notes_tui/widgets/` for UI components

4. **Make Changes**
   - Create a feature branch
   - Make improvements
   - Run tests
   - Submit pull request

## Troubleshooting

### ImportError: No module named 'textual'
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Terminal not rendering properly
**Solution**: Try a different terminal application (Ensure 256-color support)

### Can't find notes directory
**Solution**: Use `--notes-dir` flag to specify the path
```bash
python -m notes_tui --notes-dir ~/my-notes
```

## Resources

- **Textual Docs**: https://textual.textualize.io/
- **Rich Docs**: https://rich.readthedocs.io/
- **GitHub Issues**: https://github.com/sirbrasscat/notes-tui/issues
- **Original Web App**: https://github.com/sirbrasscat/notes

---

Ready to start? Run `python -m notes_tui` and explore! 🚀
