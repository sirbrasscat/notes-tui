# Notes Ecosystem - Web & Terminal Interfaces

Welcome to the Notes Ecosystem! This is a collection of complementary applications for managing your personal markdown notes.

## Projects

### 1. **Personal Markdown Notebook** (Web Interface)
- **Repository**: [notes](https://github.com/sirbrasscat/notes)
- **Interface**: Web-based with MkDocs Material
- **Best For**: 
  - Browsing and reading notes with beautiful formatting
  - Full-text search across notes
  - Sharing notes with others (optional)
  - Archival and long-term storage

**Features**:
- MkDocs Material web interface
- Beautiful markdown rendering
- Search functionality
- Wiki-link support
- Docker containerization

**Quick Start**:
```bash
git clone https://github.com/sirbrasscat/notes.git
cd notes
python -m scripts.cli serve
# Open http://localhost:8000
```

---

### 2. **Notes TUI** (Terminal Interface)
- **Repository**: [notes-tui](https://github.com/sirbrasscat/notes-tui)
- **Interface**: Terminal User Interface (Textual)
- **Best For**:
  - Fast navigation without leaving terminal
  - Power users and developers
  - Minimal resource usage
  - Offline-first experience

**Features**:
- Fast file browsing in terminal
- Quick note preview
- Keyboard-centric navigation
- Full-text search
- Lightweight and fast

**Quick Start**:
```bash
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui
pip install -r requirements.txt
python -m notes_tui
```

---

## Comparison

| Feature | Web (MkDocs) | TUI (Textual) |
|---------|-----|-----|
| **Interface** | Web browser | Terminal |
| **Speed** | Moderate | Fast ⚡ |
| **Resources** | Moderate | Minimal 📦 |
| **Browsing** | Visual/Graphical | Keyboard-driven |
| **Sharing** | Easy | Limited |
| **Offline** | Yes | Yes |
| **Search** | Full-text | Full-text |
| **Setup** | Python + MkDocs | Python only |
| **Learning Curve** | Easy | Beginner-friendly |

---

## Shared Note Structure

Both applications share the same note directory structure:

```
notes/
├── work/                 # Work notes and projects
├── personal/            # Personal thoughts and ideas
├── journals/
│   ├── daily/          # Daily entries (YYYY-MM-DD.md)
│   └── weekly/         # Weekly reflections
├── learning/           # Educational content
├── budgets/            # Financial notes
├── .config/            # Configuration
└── attachments/        # Media files
```

This means you can **use both interfaces simultaneously** on the same note collection!

---

## Installation & Setup

### Option 1: Web Interface Only
```bash
git clone https://github.com/sirbrasscat/notes.git
cd notes
pip install -r requirements.txt
python -m scripts.cli serve
```

### Option 2: TUI Interface Only
```bash
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui
pip install -r requirements.txt
python -m notes_tui
```

### Option 3: Both Interfaces (Recommended)
```bash
# Clone both repositories
git clone https://github.com/sirbrasscat/notes.git
git clone https://github.com/sirbrasscat/notes-tui.git

# Set up Web Interface
cd notes
pip install -r requirements.txt

# In another terminal, set up TUI
cd ../notes-tui
pip install -r requirements.txt

# Now you can run both:
# Terminal 1: Web interface
python -m scripts.cli serve

# Terminal 2: TUI interface (point to same notes dir)
python -m notes_tui --notes-dir ../notes
```

---

## Workflows

### Workflow 1: Terminal-First Developer
```
Morning:
  → Open TUI: Quick browse notes
  → Search for specific topic
  → View notes in terminal
  
When Sharing:
  → Start web server
  → Share link with team
```

### Workflow 2: Browser-First Thinker
```
Work:
  → Open web interface
  → Browse with Material design
  → Use keyboard shortcuts
  
Quick Updates:
  → Open TUI for fast editing
  → Back to web for reading
```

### Workflow 3: Hybrid Power User
```
Multi-monitor Setup:
  → Left screen: Web interface for reading
  → Right screen: Terminal with TUI
  → Edit in external editor (vim, code, etc)
  
Automation:
  → Use Python CLI tools
  → Backup scripts
  → Scheduled journals
```

---

## Feature Compatibility

### Supported in Both
- ✅ Markdown reading
- ✅ Full-text search
- ✅ Wiki-links (`[[note-name]]`)
- ✅ Category organization
- ✅ YAML frontmatter
- ✅ Code syntax highlighting

### Web Only
- 📊 Beautiful rendering
- 🎨 Theme customization
- 📤 Easy sharing
- 🔍 Advanced search UI

### TUI Only
- ⚡ Fast performance
- 🎮 Vim keybindings (planned)
- 📱 Minimal dependencies
- 🖥️ Terminal aesthetics

---

## Development

### Contributing to Web Interface
See: [notes/README.md](https://github.com/sirbrasscat/notes)

```bash
cd notes
python -m scripts.cli serve
# Makes changes to MkDocs config, themes, Python scripts
pytest tests/
```

### Contributing to TUI
See: [notes-tui/DEVELOPMENT.md](https://github.com/sirbrasscat/notes-tui/blob/main/DEVELOPMENT.md)

```bash
cd notes-tui
python -m notes_tui --dev
# Makes changes to Textual widgets, layouts, Python core logic
pytest tests/
```

---

## FAQ

**Q: Can I use both interfaces on the same notes?**
A: Yes! They share the same directory structure. Just point them to the same notes folder.

**Q: Which one should I use?**
A: Use the web interface for reading and sharing, TUI for fast browsing and development.

**Q: Can I sync notes to the cloud?**
A: Both use local Git repositories. Push to GitHub or use your preferred sync method.

**Q: What if I want to edit notes?**
A: Use your favorite text editor (vim, VS Code, Sublime, etc). Both interfaces will see the changes.

**Q: Can I run both simultaneously?**
A: Yes! Use different terminals or terminal panes.

**Q: Is there a mobile app?**
A: Not yet, but the web interface works on mobile browsers.

---

## Roadmap

### Web Interface (notes)
- ✅ MkDocs web viewer
- ✅ CLI tools
- ✅ Docker support
- 🔄 Plugin system (planned)
- 🔄 Cloud sync (planned)

### TUI (notes-tui)
- ✅ Core file browser
- 🔄 Search interface
- 🔄 Note editing
- 🔄 Vim keybindings
- 🔄 Theme system

---

## License

Both projects are licensed under the MIT License.

- [notes LICENSE](https://github.com/sirbrasscat/notes/blob/main/LICENSE)
- [notes-tui LICENSE](https://github.com/sirbrasscat/notes-tui/blob/main/LICENSE)

---

## Support & Issues

### For Web Interface Issues
Open an issue on: https://github.com/sirbrasscat/notes/issues

### For TUI Issues
Open an issue on: https://github.com/sirbrasscat/notes-tui/issues

### General Questions
Discussions: https://github.com/sirbrasscat/notes/discussions

---

## Getting Started Checklist

- [ ] Clone at least one repository
- [ ] Install Python dependencies
- [ ] Point to your notes directory
- [ ] Start exploring your notes!
- [ ] Read the project-specific documentation
- [ ] Contribute improvements back to the community

---

**Ready to get started? Pick your interface above and dive in!** 📝✨

For the **web interface**: https://github.com/sirbrasscat/notes  
For the **terminal interface**: https://github.com/sirbrasscat/notes-tui
