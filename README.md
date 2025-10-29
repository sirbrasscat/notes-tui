# Notes TUI - Personal Markdown Notebook

> A distraction-free, friction-free terminal user interface for rapid thought capture and note management.

**Version:** 0.1.0 (Phase 1)  
**Built with:** [Textual](https://textual.textualize.io/) - Modern Python TUI framework

## Overview

`notes-tui` is a lightning-fast terminal interface designed for one purpose: **getting your thoughts down with zero frustration**. It acts as a quick-capture launcher for your markdown notes, seamlessly integrating with external editors (nano, vim, nvim) for actual editing.

**Why Notes TUI?**
- ⚡ **< 10 second capture time** from thought to editing
- 🎯 **Zero distractions** - just you and your notes
- 🔧 **Your editor, your way** - uses nano, vim, or nvim
- 📁 **Browse and navigate** - tree view of all your notes
- 👀 **Preview markdown** - rich rendering with syntax highlighting
- 🎨 **Template system** - consistent note structure

## ✨ Features (Phase 1)

- ✅ **YAML-based configuration** - Customize everything
- ✅ **External editor integration** - nano, vim, nvim support
- ✅ **Tree navigation** - Browse your notes directory
- ✅ **Markdown preview** - Rich rendering with code highlighting
- ✅ **Template system** - 6 built-in templates
- ✅ **Quick capture** - Instant note creation with auto-edit
- ✅ **Customizable keybindings** - Make it yours
- ✅ **Shared templates** - Works with main notes CLI

## 🚀 Quick Start

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

Create your configuration file:

```bash
mkdir -p ~/.config/notes-tui
cp config/default.yaml ~/.config/notes-tui/config.yaml
```

Edit `~/.config/notes-tui/config.yaml` to set your notes directory:

```yaml
# Path to your main notes directory
notes_directory: "/home/yourusername/notes"

# Path to templates (use shared templates from main notes project)
templates_directory: "/home/yourusername/notes/.templates"

# Editor settings
editor:
  default: "nano"  # Change to "nvim" or "vim" if preferred
  alternatives:
    - "nvim"
    - "vim"
    - "vi"
```

See [config/README.md](config/README.md) for full configuration options.

### Running

```bash
# Use default config
python -m notes_tui

# Use custom config
python -m notes_tui -c /path/to/custom/config.yaml

# Show version
python -m notes_tui --version

# Show help
python -m notes_tui --help
```

## 📖 Usage

### Quick Capture Workflow

The **< 10 second capture time** workflow:

1. Launch: `python -m notes_tui`
2. Press `n` (new note)
3. Select template (arrow keys + Enter)
4. Type note name
5. **Editor opens immediately** - start writing!
6. Save and close editor
7. Note appears in tree, preview updates

That's it. From launch to writing in seconds.

### Keyboard Shortcuts

| Key | Action | Description |
|-----|--------|-------------|
| `n` | New Note | Create new note (instant edit if configured) |
| `e` | Edit Note | Open selected note in editor |
| `↑` / `↓` | Navigate | Move through tree |
| `←` / `→` | Expand/Collapse | Folders in tree |
| `Enter` | Select | View note in preview |
| `p` | Toggle Preview | Show/hide preview pane |
| `r` | Refresh | Reload tree view |
| `/` | Search | Coming in Phase 2 |
| `?` | Help | Show keybinding help |
| `q` | Quit | Exit application |
| `Ctrl+C` | Quit | Exit application |

**Note:** All keybindings are customizable in config.yaml!

### Template System

#### Available Templates

The TUI uses shared templates from your main notes project:

1. **budget_entry.md** - Budget tracking with income, expenses, and savings
2. **daily_journal.md** - Daily reflection and logging
3. **general_note.md** - General purpose note template
4. **learning_note.md** - Learning and educational content
5. **meeting_notes.md** - Meeting notes with agenda and action items
6. **project.md** - Project planning and tracking

#### Template Variables

Templates support Jinja2-like variable substitution:

```markdown
---
title: "{{ title }}"
date: "{{ date }}"
tags: {{ tags|default(['note']) }}
---

# {{ title }}

Created on {{ date }}
```

Variables:
- `{{ title }}` - Auto-generated from filename
- `{{ date }}` - Current date (YYYY-MM-DD format)
- `{{ custom }}` - Add your own variables

## 📁 Project Structure

```text
notes-tui/
├── config/
│   ├── default.yaml         # Default configuration
│   └── README.md           # Configuration documentation
├── notes_tui/
│   ├── __init__.py
│   ├── __main__.py         # CLI entry point
│   ├── app.py              # Main Textual application
│   ├── core/
│   │   ├── config.py       # Configuration loader
│   │   ├── editor_manager.py  # External editor integration
│   │   ├── notes_manager.py   # File operations
│   │   ├── template_manager.py # Template handling
│   │   └── search.py       # Search (Phase 2)
│   └── widgets/
│       ├── input_dialog.py    # Input dialog
│       ├── note_view.py       # Markdown preview
│       ├── status_bar.py      # Status bar
│       ├── template_dialog.py # Template selector
│       └── tree_view.py       # File tree browser
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
└── README.md             # This file
```

## 🔧 Troubleshooting

### No editor found

**Error:** `No suitable editor found. Please install one of: nano, nvim, vim`

**Solution:**
```bash
# Install nano (easiest for beginners)
sudo apt install nano      # Debian/Ubuntu
sudo dnf install nano      # Fedora
sudo pacman -S nano        # Arch

# Or install neovim (recommended)
sudo apt install neovim    # Debian/Ubuntu
sudo dnf install neovim    # Fedora
sudo pacman -S neovim      # Arch
```

### Configuration file not found

**Error:** `No configuration file found`

**Solution:**
```bash
# Copy default config
mkdir -p ~/.config/notes-tui
cp config/default.yaml ~/.config/notes-tui/config.yaml

# Edit with your paths
nano ~/.config/notes-tui/config.yaml
```

### Templates directory does not exist

**Error:** `Templates directory does not exist: /path/to/templates`

**Solution:**
1. Make sure your main notes project is set up
2. Update `templates_directory` in config.yaml to point to your templates
3. Or create templates directory: `mkdir -p /path/to/notes/.templates`

### Notes directory does not exist

**Error:** `Notes directory does not exist: /path/to/notes`

**Solution:**
```bash
# Create your notes directory
mkdir -p ~/notes

# Update config
nano ~/.config/notes-tui/config.yaml
# Set: notes_directory: "/home/yourusername/notes"
```

### Editor won't launch

**Problem:** Editor doesn't open when creating/editing notes

**Solutions:**
1. Check editor is in PATH: `which nano` or `which nvim`
2. Try different editor in config: `editor.default: "nvim"`
3. Check editor alternatives list in config
4. Run editor manually to test: `nano test.md`

## 🔗 Integration with Main Notes CLI

This TUI complements the [main notes CLI system](https://github.com/sirbrasscat/notes). Both share:

- **Templates** - Same template files (`.templates/`)
- **Notes structure** - Same directory layout
- **Markdown format** - Compatible note format
- **Configuration** - Separate but compatible configs

**Workflow:**
- Use **TUI** for quick capture and browsing
- Use **CLI** for scripting, search, and automation  
- Use **MkDocs** for polished documentation and sharing

## 🛠️ Development

See [DEVELOPMENT.md](DEVELOPMENT.md) for development guidelines.

### Running Tests

```bash
# Run all tests
pytest tests/

# With coverage
pytest --cov=notes_tui tests/
```

### Project Status

**Phase 1** (Current - v0.1.0):
- ✅ Configuration system
- ✅ External editor integration
- ✅ Tree navigation
- ✅ Preview pane
- ✅ Template system
- ✅ Quick capture workflow

**Phase 2** (Planned):
- 🔄 Full-text search
- 🔄 Note deletion
- 🔄 Tag filtering
- 🔄 Note statistics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Textual](https://textual.textualize.io/)** - The amazing Python TUI framework that makes this possible
- **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal formatting and markdown rendering
- **[PyYAML](https://pyyaml.org/)** - YAML configuration parsing
- **[Click](https://click.palletsprojects.com/)** - CLI argument handling

## 📚 Resources

- 📖 [Configuration Guide](config/README.md) - Full configuration documentation
- 🚀 [Quick Start](QUICK_START.md) - Get started in 5 minutes
- 🔧 [Development Guide](DEVELOPMENT.md) - Development setup and guidelines
- 🌐 [Ecosystem Overview](ECOSYSTEM.md) - How TUI fits with web and CLI
- 📋 [Planning Docs](PLANNING_SESSION.md) - Architecture and design decisions

## 💬 Support & Feedback

- 🐛 [Report Issues](https://github.com/sirbrasscat/notes-tui/issues)
- 💡 [Request Features](https://github.com/sirbrasscat/notes-tui/issues/new)
- ⭐ Star this repo if you find it useful!

---

*Built with ❤️ for distraction-free note-taking*

