# PHASE 1 - GITHUB ISSUES/USER STORIES

**Instructions:** Copy each issue below and create as a separate GitHub issue

---

## Issue #1: Fix Dependencies and Package Configuration

**Labels:** `phase-1`, `setup`, `dependencies`, `critical`

**Title:** [Phase 1] Fix Dependencies and Package Configuration

**Description:**

### User Story
As a developer, I need all required dependencies installed so that I can run the TUI application without errors.

### Acceptance Criteria
- [ ] `requirements.txt` includes `textual>=0.40.0`
- [ ] `requirements.txt` includes `rich>=13.0.0`
- [ ] `requirements.txt` includes `pyyaml>=6.0.0`
- [ ] `requirements.txt` includes `click>=8.0.0`
- [ ] All version numbers are specified
- [ ] No conflicting dependencies
- [ ] `pip install -r requirements.txt` completes without errors

### Testing Steps
```bash
cd /home/brassy/git/notes-tui
python -m venv test_venv
source test_venv/bin/activate
pip install -r requirements.txt
# Should complete without errors
python -c "import textual; import rich; import yaml; print('Success')"
deactivate
rm -rf test_venv
```

### Definition of Done
- Dependencies file updated
- Clean installation verified
- No error messages
- All packages importable

**Priority:** Critical  
**Estimated Time:** 15 minutes

---

## Issue #2: Create Configuration System

**Labels:** `phase-1`, `configuration`, `critical`, `enhancement`

**Title:** [Phase 1] Create TUI Configuration System

**Description:**

### User Story
As a user, I need a configuration file so that I can customize the TUI to point to my notes directory and set my preferences.

### Background
The TUI needs its own configuration that points to the shared notes directory and templates, while remaining independent from the main CLI system.

### Acceptance Criteria

**File: `config/default.yaml`**
- [ ] Valid YAML syntax
- [ ] Contains `notes.directory` setting
- [ ] Contains `notes.templates` setting
- [ ] Contains `editor.default` setting (nano)
- [ ] Contains `editor.fallback` setting
- [ ] Contains `ui.layout` settings (tree_width: 30, preview_width: 70)
- [ ] Contains all keybinding configurations
- [ ] Contains behavior settings
- [ ] Comments explain each setting
- [ ] Default path: `/home/brassy/Docker/notes`

**File: `config/README.md`**
- [ ] Explains each configuration section
- [ ] Provides customization examples
- [ ] Includes troubleshooting guidance

**File: `notes_tui/core/config.py`**
- [ ] `Config.__init__(config_path=None)` - Load config from file
- [ ] `Config.get(key, default=None)` - Get value using dot notation
- [ ] `Config.validate()` - Validate critical paths exist
- [ ] `Config.get_notes_dir()` - Return Path to notes directory
- [ ] `Config.get_templates_dir()` - Return Path to templates
- [ ] `Config.get_editor()` - Return configured editor
- [ ] Loads default.yaml successfully
- [ ] Returns sensible defaults if file missing
- [ ] Provides helpful error messages

### Testing Steps
```python
from notes_tui.core.config import Config
from pathlib import Path

# Test 1: Load default config
config = Config()
assert config.get('editor.default') == 'nano'
assert config.get('ui.layout.tree_width') == 30

# Test 2: Validate paths
try:
    config.validate()
    print("✓ Paths validated")
except Exception as e:
    print(f"✗ Validation failed: {e}")

# Test 3: Get methods work
notes_dir = config.get_notes_dir()
assert notes_dir.exists(), f"Notes dir not found: {notes_dir}"
print(f"✓ Notes directory: {notes_dir}")

templates_dir = config.get_templates_dir()
assert templates_dir.exists(), f"Templates dir not found: {templates_dir}"
print(f"✓ Templates directory: {templates_dir}")

editor = config.get_editor()
assert editor in ['nano', 'vim', 'nvim']
print(f"✓ Editor: {editor}")
```

### Definition of Done
- All configuration files created
- Config class loads YAML
- Path validation works
- All tests pass
- Documentation complete

**Priority:** Critical  
**Estimated Time:** 45 minutes

---

## Issue #3: Implement Editor Manager

**Labels:** `phase-1`, `feature`, `editor`, `critical`

**Title:** [Phase 1] Implement Editor Manager for External Editor Integration

**Description:**

### User Story
As a user, I need to launch my preferred text editor (nano/vim) to edit notes so that I can modify content efficiently.

### Background
The TUI will launch external terminal editors (nano, vim) in full-screen mode, blocking until the user saves and exits, then return to the TUI with refreshed content.

### Acceptance Criteria

**File: `notes_tui/core/editor_manager.py`**
- [ ] `EditorManager.__init__(config)` - Initialize with config
- [ ] `EditorManager.launch(file_path)` - Launch editor, block until closed
- [ ] `EditorManager.get_editor_command()` - Get editor from config/env
- [ ] `EditorManager.is_editor_available(editor)` - Check if in PATH
- [ ] Launches nano successfully
- [ ] Blocks until editor closes
- [ ] Returns control to TUI after editor exit
- [ ] Handles missing editor gracefully
- [ ] Respects `$EDITOR` environment variable if set
- [ ] Falls back to nano if configured editor unavailable
- [ ] Provides helpful error messages

### Implementation Notes
```python
import subprocess
import os
import shutil
from pathlib import Path

class EditorManager:
    def __init__(self, config):
        self.config = config
    
    def get_editor_command(self):
        # Priority: $EDITOR > config > fallback
        return os.environ.get('EDITOR') or \
               self.config.get('editor.default') or \
               'nano'
    
    def is_editor_available(self, editor):
        return shutil.which(editor) is not None
    
    def launch(self, file_path):
        editor = self.get_editor_command()
        
        if not self.is_editor_available(editor):
            # Try fallback
            editor = self.config.get('editor.fallback', 'nano')
        
        # Launch and block
        result = subprocess.run([editor, str(file_path)])
        return result.returncode == 0
```

### Testing Steps
```python
from notes_tui.core.editor_manager import EditorManager
from notes_tui.core.config import Config
from pathlib import Path

config = Config()
editor_mgr = EditorManager(config)

# Test 1: Get editor command
editor = editor_mgr.get_editor_command()
print(f"Editor command: {editor}")
assert editor in ['nano', 'vim', 'nvim']

# Test 2: Check availability
assert editor_mgr.is_editor_available('nano'), "nano not available"
print("✓ nano is available")

# Test 3: Launch editor (MANUAL TEST)
# Create test file
test_file = Path('/tmp/test_note.md')
test_file.write_text('# Test Note\nEdit this file')
print(f"Launching editor for: {test_file}")
success = editor_mgr.launch(test_file)
print(f"Editor returned: {success}")
# User should edit, save, exit
# Verify file was modified
print(f"Final content:\n{test_file.read_text()}")
```

### Definition of Done
- EditorManager class implemented
- Launches nano successfully
- Blocks until editor closes
- Error handling works
- All tests pass

**Priority:** Critical  
**Estimated Time:** 30 minutes

---

## Issue #4: Update Template Manager for Shared Templates

**Labels:** `phase-1`, `refactor`, `templates`, `high`

**Title:** [Phase 1] Update Template Manager to Use Shared Templates

**Description:**

### User Story
As a developer, I need the TUI to use shared templates from the main notes project so that there's no duplication and templates stay in sync.

### Background
Currently, templates are duplicated in `notes-tui/templates/`. We need to point to the shared templates in the main notes project at `/home/brassy/Docker/notes/.templates/`.

### Acceptance Criteria

**File: `notes_tui/core/template_manager.py`**
- [ ] Update `__init__` to accept templates path from config
- [ ] Remove hardcoded local templates path
- [ ] Point to shared templates directory
- [ ] `list_templates()` works with shared path
- [ ] `get_template_content(name)` works with shared path
- [ ] `create_note_from_template()` works with shared path
- [ ] No references to local `templates/` folder remain

**File System:**
- [ ] Delete `notes-tui/templates/` directory (duplicate)
- [ ] Verify shared templates exist at configured path

### Testing Steps
```python
from notes_tui.core.template_manager import TemplateManager
from notes_tui.core.config import Config

config = Config()
templates_dir = config.get_templates_dir()
print(f"Templates directory: {templates_dir}")

tm = TemplateManager(templates_dir)

# Test 1: List templates
templates = tm.list_templates()
print(f"Found {len(templates)} templates:")
for t in templates:
    print(f"  - {t['name']}: {t['description']}")
assert len(templates) > 0
assert 'general_note' in [t['name'] for t in templates]

# Test 2: Get template content
content = tm.get_template_content('general_note')
assert content is not None
assert 'title' in content
assert '{{' in content  # Has template variables
print("✓ Template content loaded")

# Test 3: Create note from template
from pathlib import Path
test_note = Path('/tmp/test_from_template.md')
success = tm.create_note_from_template(
    'general_note',
    test_note,
    {'title': 'Test Note', 'date': '2025-10-24'}
)
assert success
assert test_note.exists()
content = test_note.read_text()
assert 'Test Note' in content
print("✓ Note created from template")
```

### Definition of Done
- Template manager updated
- Points to shared templates
- Duplicate templates folder deleted
- All tests pass
- Templates load correctly

**Priority:** High  
**Estimated Time:** 20 minutes

---

## Issue #5: Update App Integration and CLI Arguments

**Labels:** `phase-1`, `integration`, `critical`, `enhancement`

**Title:** [Phase 1] Update App Integration and Add CLI Arguments

**Description:**

### User Story
As a user, I need to launch the TUI with optional arguments so that I can specify custom notes directories or config files.

### Background
The app needs to integrate the new config system, editor manager, and support command-line arguments for flexibility.

### Acceptance Criteria

**File: `notes_tui/__main__.py`**
- [ ] Add argparse for CLI arguments
- [ ] Support `--notes-dir` argument
- [ ] Support `--config` argument
- [ ] Support `--help` argument
- [ ] Pass arguments to NotesApp
- [ ] `python -m notes_tui` launches with defaults
- [ ] `python -m notes_tui --notes-dir /path` works
- [ ] `python -m notes_tui --config /path` works
- [ ] `python -m notes_tui --help` shows usage

**File: `notes_tui/app.py`**
- [ ] Accept `notes_dir` parameter
- [ ] Accept `config_path` parameter
- [ ] Load Config with config_path
- [ ] Override notes_dir if provided via CLI
- [ ] Initialize NotesManager with configured path
- [ ] Initialize TemplateManager with configured path
- [ ] Initialize EditorManager with config
- [ ] App initializes without errors
- [ ] All managers work together

### Implementation Notes

**`__main__.py`:**
```python
import argparse
from pathlib import Path
from notes_tui.app import NotesApp

def main():
    parser = argparse.ArgumentParser(
        description='Notes TUI - Fast, keyboard-driven note capture'
    )
    parser.add_argument(
        '--notes-dir',
        type=Path,
        help='Path to notes directory (default: from config)'
    )
    parser.add_argument(
        '--config',
        type=Path,
        help='Path to config file (default: config/default.yaml)'
    )
    args = parser.parse_args()
    
    app = NotesApp(
        notes_dir=args.notes_dir,
        config_path=args.config
    )
    app.run()

if __name__ == "__main__":
    main()
```

**`app.py` updates:**
```python
class NotesApp(App):
    def __init__(self, notes_dir=None, config_path=None):
        super().__init__()
        
        # Load configuration
        self.config = Config(config_path)
        
        # Override notes_dir if provided
        if notes_dir:
            self.notes_dir = Path(notes_dir)
        else:
            self.notes_dir = self.config.get_notes_dir()
        
        # Initialize managers
        self.notes_manager = NotesManager(self.notes_dir)
        self.template_manager = TemplateManager(
            self.config.get_templates_dir()
        )
        self.editor_manager = EditorManager(self.config)
        
        # ... rest of initialization
```

### Testing Steps
```bash
# Test 1: Default launch
python -m notes_tui
# Should open TUI with config defaults

# Test 2: Custom notes directory
python -m notes_tui --notes-dir /home/brassy/Docker/notes
# Should show files from that directory

# Test 3: Help
python -m notes_tui --help
# Should show usage information

# Test 4: Custom config
echo "notes:
  directory: /tmp
editor:
  default: nano" > /tmp/test_config.yaml
python -m notes_tui --config /tmp/test_config.yaml
# Should use custom config
```

### Definition of Done
- CLI arguments implemented
- App integration complete
- All managers initialize
- Config system works
- Help text clear
- All tests pass

**Priority:** Critical  
**Estimated Time:** 30 minutes

---

## Issue #6: Fix Tree View Navigation

**Labels:** `phase-1`, `ui`, `navigation`, `high`

**Title:** [Phase 1] Fix Tree View Navigation and Integration

**Description:**

### User Story
As a user, I need to navigate the file tree with keyboard arrows so that I can browse my notes efficiently.

### Background
The tree view widget exists but needs integration fixes to work with the new config system and ensure smooth navigation.

### Acceptance Criteria

**File: `notes_tui/widgets/tree_view.py`**
- [ ] Tree loads from configured notes directory
- [ ] Tree displays folder structure correctly
- [ ] Icons display for folders (📁) and files (📄)
- [ ] Arrow ↓ moves cursor down
- [ ] Arrow ↑ moves cursor up
- [ ] Arrow → expands folder
- [ ] Arrow ← collapses folder
- [ ] Enter key selects file
- [ ] Enter key toggles folder expand/collapse
- [ ] Tree refresh works after file changes
- [ ] No crashes during navigation
- [ ] Performance is smooth (<100ms response)

### Testing Steps (Manual)
```
Launch TUI and verify:

Navigation:
1. [ ] Launch: python -m notes_tui
2. [ ] Tree displays on left side (30% width)
3. [ ] Folder structure matches notes directory
4. [ ] Icons show correctly

Arrow Keys:
5. [ ] Press ↓ - cursor moves to next item
6. [ ] Press ↑ - cursor moves to previous item
7. [ ] Press ↓ repeatedly - scrolls through all items
8. [ ] At bottom, ↓ doesn't crash

Folders:
9. [ ] Press → on collapsed folder - expands
10. [ ] Press ← on expanded folder - collapses
11. [ ] Press Enter on folder - toggles expand/collapse

Files:
12. [ ] Press Enter on file - preview shows (Issue #7)
13. [ ] Navigate between files - preview updates

Performance:
14. [ ] Navigation feels instant (<100ms)
15. [ ] No lag with 100+ files
16. [ ] No visual glitches
```

### Definition of Done
- Tree navigation works smoothly
- All keyboard shortcuts work
- Icons display correctly
- Performance is acceptable
- Manual testing passes

**Priority:** High  
**Estimated Time:** 20 minutes

---

## Issue #7: Verify Note Preview Functionality

**Labels:** `phase-1`, `ui`, `preview`, `high`

**Title:** [Phase 1] Verify Note Preview Renders Correctly

**Description:**

### User Story
As a user, I need to see a preview of selected notes so that I can read content without opening an editor.

### Background
The note preview widget exists and should work. This issue verifies it functions correctly with the updated integration.

### Acceptance Criteria

**File: `notes_tui/widgets/note_view.py`**
- [ ] Preview displays on right side (70% width)
- [ ] Selecting file shows preview
- [ ] Markdown renders correctly (headings, lists, links)
- [ ] Code blocks display with syntax
- [ ] Preview updates when selection changes
- [ ] Scrolling works for long notes
- [ ] Large files (>1MB) handle gracefully
- [ ] Empty files don't cause errors
- [ ] Preview shows helpful message when no file selected

### Testing Steps (Manual)
```
Launch TUI and test preview:

Basic Display:
1. [ ] Launch: python -m notes_tui
2. [ ] Preview pane visible on right (70% width)
3. [ ] Shows "Select a note..." when nothing selected

File Selection:
4. [ ] Select a .md file in tree
5. [ ] Preview shows content immediately
6. [ ] Content is readable

Markdown Rendering:
7. [ ] Headings render with proper style
8. [ ] Lists display correctly
9. [ ] Links are visible (blue/underlined)
10. [ ] Code blocks show with monospace font
11. [ ] Bold/italic text renders

Scrolling:
12. [ ] Long file - use mouse/keyboard to scroll
13. [ ] Scroll position resets on new file
14. [ ] Smooth scrolling (no lag)

Edge Cases:
15. [ ] Select empty file - no error
16. [ ] Select large file (>1MB) - loads or shows warning
17. [ ] Select binary file - handles gracefully
18. [ ] Switch files rapidly - no crashes
```

### Definition of Done
- Preview displays correctly
- Markdown renders properly
- Scrolling works
- Edge cases handled
- Manual testing passes

**Priority:** High  
**Estimated Time:** 15 minutes (mostly verification)

---

## Issue #8: Update Documentation for Phase 1

**Labels:** `phase-1`, `documentation`, `medium`

**Title:** [Phase 1] Update README and Add Configuration Documentation

**Description:**

### User Story
As a new user, I need clear documentation so that I can install and configure the TUI successfully.

### Background
With the new configuration system and CLI arguments, the README needs updating to guide users through setup.

### Acceptance Criteria

**File: `README.md`**
- [ ] Add "Installation" section with step-by-step instructions
- [ ] Add "Configuration" section explaining config file
- [ ] Add "Usage" section with command examples
- [ ] Add "Quick Start" for immediate use
- [ ] Include troubleshooting common issues
- [ ] Update feature list to reflect Phase 1 capabilities
- [ ] Add link to config/README.md

**File: `config/README.md`**
- [ ] Explain each configuration section
- [ ] Provide example configurations
- [ ] Show how to customize editor
- [ ] Show how to change notes directory
- [ ] Show how to adjust UI layout
- [ ] Include troubleshooting section

### Content to Include

**README.md additions:**
```markdown
## Quick Start

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sirbrasscat/notes-tui.git
   cd notes-tui
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your notes directory:
   Edit `config/default.yaml` and set:
   ```yaml
   notes:
     directory: "/path/to/your/notes"
     templates: "/path/to/your/notes/.templates"
   ```

4. Run the TUI:
   ```bash
   python -m notes_tui
   ```

### Usage

```bash
# Launch with default config
python -m notes_tui

# Specify notes directory
python -m notes_tui --notes-dir /path/to/notes

# Use custom config
python -m notes_tui --config /path/to/config.yaml

# Show help
python -m notes_tui --help
```

### Configuration

See [config/README.md](config/README.md) for detailed configuration options.

### Troubleshooting

**TUI won't launch:**
- Check dependencies: `pip list | grep textual`
- Verify Python version: `python --version` (need 3.8+)

**Can't find notes:**
- Check `notes.directory` in config/default.yaml
- Verify path exists: `ls -la /path/to/notes`

**Editor won't open:**
- Check `editor.default` in config
- Verify editor installed: `which nano`
```

### Definition of Done
- README updated with clear instructions
- Configuration guide created
- Examples provided
- Troubleshooting section complete
- Links work correctly

**Priority:** Medium  
**Estimated Time:** 30 minutes

---

## Summary

**Total Issues:** 8  
**Critical:** 5 (Issues #1, #2, #3, #5, #6)  
**High:** 2 (Issues #4, #7)  
**Medium:** 1 (Issue #8)

**Estimated Total Time:** ~3 hours

**Dependencies:**
- Issue #1 must complete first (foundation)
- Issue #2 must complete before #3, #4, #5
- Issues #6, #7 can be done in parallel after #5
- Issue #8 can be done anytime but best at end

**Recommended Order:**
1. Issue #1 (Dependencies)
2. Issue #2 (Configuration)
3. Issue #3 (Editor Manager)
4. Issue #4 (Template Manager)
5. Issue #5 (App Integration)
6. Issue #6 + #7 (Navigation + Preview - parallel)
7. Issue #8 (Documentation)

---

## Creating Issues in GitHub

For each issue above:

1. Go to https://github.com/sirbrasscat/notes-tui/issues/new
2. Copy the title
3. Copy the description (everything under "Description:")
4. Add the labels listed
5. Assign to yourself
6. Add to "Phase 1" milestone (create if needed)
7. Set project (if using GitHub Projects)

Or use GitHub CLI:
```bash
gh issue create \
  --title "[Phase 1] Fix Dependencies and Package Configuration" \
  --body "$(cat issue_1_content.md)" \
  --label "phase-1,setup,dependencies,critical"
```
