# Notes TUI - Omarchy OS Setup Guide

> Complete setup instructions for configuring Notes TUI in Omarchy OS

## Overview

This guide will help you set up Notes TUI as a native application in Omarchy OS, making it accessible from the application launcher and integrated into your workflow.

## Prerequisites

- Omarchy OS installed and configured
- Python 3.8+ (usually pre-installed)
- Git (for cloning the repository)
- Access to terminal

## Installation

### 1. Clone the Repository

```bash
# Navigate to your preferred installation directory
cd ~/git
# Or create it if it doesn't exist
mkdir -p ~/git && cd ~/git

# Clone the repository
git clone https://github.com/sirbrasscat/notes-tui.git
cd notes-tui
```

### 2. Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Notes TUI

Create your configuration directory and file:

```bash
# Create config directory
mkdir -p ~/.config/notes-tui

# Copy default configuration
cp config/default.yaml ~/.config/notes-tui/config.yaml
```

Edit the configuration file to match your setup:

```bash
# Open with your preferred editor
nvim ~/.config/notes-tui/config.yaml
# or
nano ~/.config/notes-tui/config.yaml
```

**Key configuration settings to update:**

```yaml
# Path to your notes directory (adjust to your actual path)
notes_directory: "/home/yourusername/Docker/notes"

# Path to templates directory
templates_directory: "/home/yourusername/Docker/notes/.templates"

# Editor settings (recommended: nvim for Omarchy)
editor:
  default: "nvim"
  alternatives:
    - "vim"
    - "vi"
    - "nano"
  args: []
```

### 4. Create Templates Directory

If you don't already have a templates directory:

```bash
# Navigate to your notes directory
cd ~/Docker/notes  # Adjust to your path

# Create templates directory
mkdir -p .templates

# Copy the sample template
cp ~/git/notes-tui/templates/general_note.md .templates/
```

## Omarchy Integration

### Option 1: Desktop Entry (Recommended)

Create a desktop entry file to launch Notes TUI from the application launcher.

```bash
# Create .desktop file
nano ~/.local/share/applications/notes-tui.desktop
```

Add the following content (adjust paths to match your setup):

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Notes TUI
Comment=Distraction-free markdown note taking
Exec=/home/yourusername/git/notes-tui/venv/bin/python -m notes_tui
Icon=text-editor
Terminal=true
Categories=Utility;TextEditor;
Keywords=notes;markdown;tui;
```

**Important:** Replace `/home/yourusername/` with your actual home directory path.

After creating the file:

```bash
# Update desktop database
update-desktop-database ~/.local/share/applications/
```

Now you can launch Notes TUI from your application launcher!

### Option 2: Shell Alias

Add an alias to your shell configuration for quick terminal access:

```bash
# For bash users
echo 'alias notes-tui="/home/yourusername/git/notes-tui/venv/bin/python -m notes_tui"' >> ~/.bashrc
source ~/.bashrc

# For zsh users
echo 'alias notes-tui="/home/yourusername/git/notes-tui/venv/bin/python -m notes_tui"' >> ~/.zshrc
source ~/.zshrc
```

Now you can launch with just: `notes-tui`

### Option 3: Symbolic Link

Create a symbolic link for system-wide access:

```bash
# Create local bin directory if it doesn't exist
mkdir -p ~/.local/bin

# Create wrapper script
cat > ~/.local/bin/notes-tui << 'EOF'
#!/bin/bash
/home/yourusername/git/notes-tui/venv/bin/python -m notes_tui "$@"
EOF

# Make executable
chmod +x ~/.local/bin/notes-tui

# Ensure ~/.local/bin is in PATH (add to .bashrc or .zshrc if needed)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Important:** Replace `/home/yourusername/` with your actual home directory path.

Now you can run: `notes-tui` from anywhere!

## Verification

Test your installation:

```bash
# Run notes-tui
notes-tui

# Or with full path
/home/yourusername/git/notes-tui/venv/bin/python -m notes_tui
```

You should see:
- Tree view on the left showing your notes directory
- Preview pane on the right
- Status bar at the bottom with keybinding hints

## Quick Start Guide

### Essential Keybindings

| Key | Action | Description |
|-----|--------|-------------|
| `j` | Quick Journal | Open today's journal instantly |
| `n` | New Note | Create a new note with template |
| `N` | Template Note | Create note with template selection |
| `e` | Edit Note | Edit selected note in nvim |
| `Tab` | Switch Pane | Navigate between tree and preview |
| `↑/↓` | Navigate | Move through file tree |
| `Enter` | Preview | Preview selected note |
| `q` | Quit | Exit application |
| `?` | Help | Show help screen |

### Typical Workflow

1. **Launch Notes TUI**
   ```bash
   notes-tui
   ```

2. **Quick Journal Entry** (Daily workflow)
   - Press `j`
   - Starts editing today's journal: `journals/daily/YYYY-MM-DD.md`
   - Template auto-applied with date, tags, etc.
   - Write your thoughts
   - Save and quit (`:wq` in nvim)
   - Back to TUI

3. **Create Quick Note**
   - Press `n`
   - Enter note name
   - Starts editing immediately
   - Save and close editor
   - Note appears in tree

4. **Browse and Edit Existing Notes**
   - Use `↑/↓` to navigate tree
   - Press `Enter` to preview
   - Press `Tab` to switch to preview pane
   - Press `e` to edit in nvim
   - Press `Tab` to return to tree

## Customization

### Custom Keybindings

Edit `~/.config/notes-tui/config.yaml`:

```yaml
keybindings:
  new_note: "n"
  edit_note: "e"
  delete_note: "d"
  search: "/"
  toggle_preview: "p"
  refresh: "r"
  quit: "q"
  help: "?"
```

Change any key to your preference!

### UI Layout

Adjust the UI layout in config:

```yaml
ui:
  show_tree: true
  show_preview: true
  tree_width: 30        # Percentage of screen
  preview_width: 50     # Percentage of remaining space
  theme: "dark"
```

### Quick Capture Settings

Configure quick capture behavior:

```yaml
quick_capture:
  instant_edit: true              # Open editor immediately
  default_category: "personal"    # Default folder for quick notes
  default_template: "general_note"  # Default template
  auto_timestamp: false           # Add timestamp to note names
```

## Troubleshooting

### Editor Not Found

**Error:** `No suitable editor found`

**Solution:**
```bash
# Verify nvim is installed
which nvim

# Install if missing
sudo pacman -S neovim  # Arch-based (Omarchy)

# Or use fallback editor
nano ~/.config/notes-tui/config.yaml
# Change: editor.default: "vim"
```

### Config File Not Loaded

**Error:** `No configuration file found`

**Solution:**
```bash
# Verify config exists
ls -la ~/.config/notes-tui/config.yaml

# If missing, copy default
mkdir -p ~/.config/notes-tui
cp ~/git/notes-tui/config/default.yaml ~/.config/notes-tui/config.yaml
```

### Notes Directory Not Found

**Error:** `Notes directory does not exist`

**Solution:**
```bash
# Create your notes directory
mkdir -p ~/Docker/notes

# Update config to point to correct location
nano ~/.config/notes-tui/config.yaml
# Set: notes_directory: "/home/yourusername/Docker/notes"
```

### Templates Not Working

**Error:** Template variables not substituted

**Solution:**
```bash
# Verify templates directory exists
ls -la ~/Docker/notes/.templates/

# Copy sample templates if needed
cp ~/git/notes-tui/templates/general_note.md ~/Docker/notes/.templates/

# Verify config points to correct location
grep templates_directory ~/.config/notes-tui/config.yaml
```

### Virtual Environment Issues

**Error:** `ModuleNotFoundError: No module named 'textual'`

**Solution:**
```bash
# Recreate virtual environment
cd ~/git/notes-tui
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Updates

To update Notes TUI to the latest version:

```bash
# Navigate to repository
cd ~/git/notes-tui

# Pull latest changes
git pull origin main

# Activate virtual environment
source venv/bin/activate

# Update dependencies
pip install -r requirements.txt --upgrade
```

## Advanced Configuration

### Multiple Note Directories

You can create different configurations for different note collections:

```bash
# Work notes
notes-tui -c ~/.config/notes-tui/work.yaml

# Personal notes
notes-tui -c ~/.config/notes-tui/personal.yaml
```

### Custom Templates

Create your own templates in `.templates/`:

```bash
# Create new template
nano ~/Docker/notes/.templates/my_template.md
```

Template format (supports Jinja2-like variables):

```markdown
---
title: "{{ title }}"
date: "{{ date }}"
tags: {{ tags|default(['note']) }}
---

# {{ title }}

Created: {{ date }}

## Content

Your content here...
```

## Integration with Existing Workflows

### Use with Main Notes CLI

Notes TUI works seamlessly with the main notes CLI:

- **TUI**: Quick capture and browsing
- **CLI**: Scripting and automation
- **MkDocs**: Publishing and sharing

All share the same notes directory and templates!

### Git Integration

Add version control to your notes:

```bash
cd ~/Docker/notes
git init
git add .
git commit -m "Initial notes commit"
```

Notes TUI automatically updates the tree view when files change.

## Support

- 📖 Documentation: See `/docs` folder in repository
- 🐛 Issues: https://github.com/sirbrasscat/notes-tui/issues
- 💡 Feature Requests: Open an issue with the enhancement label

## Tips for Omarchy Users

1. **Use nvim/LazyVim**: Notes TUI integrates perfectly with LazyVim's capabilities
2. **Create keyboard shortcuts**: Omarchy allows custom shortcuts - bind one to launch notes-tui
3. **Terminal multiplexer**: Use tmux/zellij with Notes TUI for advanced workflows
4. **Quick access**: Keep Notes TUI in a dedicated workspace for instant access

---

*Happy note-taking in Omarchy! 📝✨*
