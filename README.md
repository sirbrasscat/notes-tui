# notes-tui
Terminal User Interface (TUI) for the Personal Markdown Notebook System - built with Textual

## Overview

`notes-tui` is a powerful terminal-based interface for managing your personal markdown notes. Built with [Textual](https://textual.textualize.io/), it provides a modern, intuitive TUI experience for creating, browsing, and managing markdown notes with template support.

## Features

✅ **Currently Implemented:**
- 📁 Browse notes in a tree view
- 👀 Preview markdown notes with rich formatting
- 🎨 Create notes from pre-built templates
- ⌨️ Keyboard-driven navigation
- 🎯 Template-based note creation with variables

🔄 **In Progress:**
- 🔍 Full-text search across notes
- 📝 Edit notes in external editor
- 🗑️ Delete notes

⏳ **Planned:**
- ✏️ Built-in markdown editor
- 🏷️ Tag management
- 📊 Note statistics
- 🔗 Backlink support

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the App

```bash
python -m notes_tui
```

With custom notes directory:
```bash
python -m notes_tui --notes-dir /path/to/your/notes
```

## Using Templates

### Available Templates

The app comes with 6 built-in templates:

1. **Budget Entry** - Track income, expenses, and savings
2. **Daily Journal** - Daily reflection and logging
3. **General Note** - All-purpose note template
4. **Learning Note** - Educational content and learning notes
5. **Meeting Notes** - Meeting agenda and action items
6. **Project** - Project planning and tracking

### Creating a Note from Template

1. Press `n` to open the template selection dialog
2. Use arrow keys to select a template
3. Press `Enter` to confirm selection
4. Enter a name for your note
5. The note is created and appears in the tree view

### Template Variables

Templates support variable substitution:

- `{{ title }}` - Auto-generated from filename
- `{{ date }}` - Current date (YYYY-MM-DD format)
- Custom variables can be added in the template

Example template snippet:
```markdown
---
title: {{ title }}
date: {{ date }}
tags: {{ tags|default(['note']) }}
---

# {{ title }}

Created on {{ date }}
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `↑` / `↓` | Navigate notes |
| `Enter` | Select/view note |
| `n` | Create new note from template |
| `d` | Delete note (coming soon) |
| `e` | Edit note (coming soon) |
| `/` | Search notes (coming soon) |
| `?` | Show help (coming soon) |
| `q` / `Ctrl+C` | Quit application |

## Project Structure

```
notes_tui/
├── app.py                    # Main application
├── core/
│   ├── config.py            # Configuration management
│   ├── notes_manager.py     # File operations
│   ├── search.py            # Search functionality
│   └── template_manager.py  # Template handling
├── widgets/
│   ├── input_dialog.py      # Input dialog for note names
│   ├── note_view.py         # Note preview widget
│   ├── status_bar.py        # Status bar widget
│   ├── template_dialog.py   # Template selection dialog
│   └── tree_view.py         # File tree widget
└── utils/
    └── helpers.py           # Helper functions

templates/                   # Note templates
├── budget_entry.md
├── daily_journal.md
├── general_note.md
├── learning_note.md
├── meeting_notes.md
└── project.md
```

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for development guidelines and [ECOSYSTEM.md](ECOSYSTEM.md) for integration with the web interface.

### Running Tests

```bash
pytest tests/
```

### Code Style

This project follows PEP 8 style guidelines. Use `black` for code formatting:

```bash
black notes_tui/
```

## Integration with Web App

This TUI complements the [web-based notes application](https://github.com/sirbrasscat/notes). Both share:
- Template format and structure
- Markdown note format
- Directory organization
- Tag system (coming soon)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Textual](https://textual.textualize.io/) - Amazing TUI framework
- Uses [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting
- Inspired by modern note-taking applications

## Support

- 📖 [Full Documentation](QUICK_START.md)
- 🐛 [Report Issues](https://github.com/sirbrasscat/notes-tui/issues)
- 💡 [Request Features](https://github.com/sirbrasscat/notes-tui/issues/new)

---

**Happy Note-Taking! 📝✨**

