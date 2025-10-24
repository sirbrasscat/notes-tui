# Configuration Guide

The Notes TUI uses a YAML-based configuration system that allows you to customize every aspect of the application.

## Configuration File Location

The default configuration is located at `config/default.yaml`. You can also create a user-specific configuration at `~/.config/notes-tui/config.yaml` that will override the defaults.

## Configuration Sections

### Notes Directory
```yaml
notes_directory: "/path/to/your/notes"
```
The root directory where your markdown notes are stored. This should point to your main notes project.

### Templates Directory
```yaml
templates_directory: "/path/to/templates"
```
The directory containing your note templates. By default, this points to the shared templates in your main notes project.

### Editor Settings
```yaml
editor:
  default: "nano"
  alternatives:
    - "vim"
    - "vi"
  args: []
```
- `default`: The primary editor to use for editing notes
- `alternatives`: Fallback editors if the default is not available
- `args`: Additional command-line arguments to pass to the editor

### UI Layout
```yaml
ui:
  show_tree: true
  show_preview: true
  tree_width: 30
  preview_width: 50
  theme: "dark"
```
- `show_tree`: Show the directory tree on startup
- `show_preview`: Show the markdown preview pane
- `tree_width`: Width of tree view as percentage of screen
- `preview_width`: Width of preview as percentage of remaining space
- `theme`: Color theme (dark, light, or custom)

### Keybindings
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
Customize keyboard shortcuts for all actions. Use single characters or key combinations.

### Quick Capture
```yaml
quick_capture:
  instant_edit: true
  default_category: "personal"
  default_template: "general_note.md"
  auto_timestamp: false
```
- `instant_edit`: Open editor immediately after entering note name
- `default_category`: Default folder for new notes
- `default_template`: Default template to use
- `auto_timestamp`: Add timestamp to note filenames automatically

### File Watching
```yaml
watch:
  enabled: true
  debounce: 1.0
```
- `enabled`: Automatically refresh when files change
- `debounce`: Wait time in seconds before refreshing

## User Configuration

To create your own configuration:

1. Create directory: `mkdir -p ~/.config/notes-tui`
2. Copy default config: `cp config/default.yaml ~/.config/notes-tui/config.yaml`
3. Edit your configuration: `nano ~/.config/notes-tui/config.yaml`

User configuration values will override defaults.

## Path Expansion

All paths in the configuration support:
- Absolute paths: `/home/user/notes`
- Home directory expansion: `~/notes`
- Environment variables: `$HOME/notes`

## Validation

The TUI validates your configuration on startup and will display helpful error messages if:
- Required directories don't exist
- Editor is not available
- Configuration syntax is invalid
- Required fields are missing

## Examples

### Vim User Configuration
```yaml
editor:
  default: "vim"
  args: ["+set", "wrap"]
```

### Minimal UI
```yaml
ui:
  show_tree: false
  show_preview: false
```

### Custom Keybindings
```yaml
keybindings:
  new_note: "c"  # Change from 'n' to 'c' for create
  edit_note: "enter"
  quit: "ctrl+q"
```
