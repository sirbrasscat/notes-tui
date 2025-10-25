# PHASE 1: FOUNDATION - SPECIFICATION
**Goal:** Get TUI running reliably with basic functionality  
**Status:** Planning  
**Estimated Time:** 1-2 hours

---

## 📁 UPDATED FOLDER STRUCTURE

### Current Structure
```
notes-tui/
├── notes_tui/
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── notes_manager.py
│   │   ├── search.py
│   │   └── template_manager.py
│   ├── widgets/
│   │   ├── __init__.py
│   │   ├── input_dialog.py
│   │   ├── note_view.py
│   │   ├── status_bar.py
│   │   ├── template_dialog.py
│   │   └── tree_view.py
│   ├── screens/
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── templates/          # ⚠️ TO BE REMOVED (duplicate)
├── tests/
├── requirements.txt    # ⚠️ NEEDS UPDATE
├── setup.py
├── README.md
└── DEVELOPMENT.md
```

### Proposed Structure (After Phase 1)
```
notes-tui/
├── notes_tui/
│   ├── __init__.py
│   ├── __main__.py          # ✏️ UPDATE: Add CLI args
│   ├── app.py               # ✏️ UPDATE: Use new config system
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # ✏️ UPDATE: New config loading
│   │   ├── notes_manager.py # ✅ KEEP: Works as-is
│   │   ├── search.py        # ✅ KEEP: For Phase 3
│   │   ├── template_manager.py  # ✏️ UPDATE: Point to shared templates
│   │   └── editor_manager.py    # ➕ NEW: Editor integration
│   │
│   ├── widgets/
│   │   ├── __init__.py
│   │   ├── tree_view.py     # ✏️ UPDATE: Integration fixes
│   │   ├── note_view.py     # ✅ KEEP: Works as-is
│   │   ├── status_bar.py    # ✅ KEEP: Works as-is
│   │   ├── input_dialog.py  # ✅ KEEP: For Phase 2
│   │   └── template_dialog.py   # ✅ KEEP: For Phase 2
│   │
│   ├── screens/
│   │   └── __init__.py      # ✅ KEEP: For Phase 3
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py       # ✅ KEEP: Utility functions
│
├── config/                  # ➕ NEW: Configuration directory
│   ├── default.yaml         # ➕ NEW: Default TUI config
│   └── README.md            # ➕ NEW: Config documentation
│
├── tests/                   # ✅ KEEP: For Phase 4
│   ├── __init__.py
│   ├── test_notes_manager.py
│   └── test_search.py
│
├── templates/               # ❌ REMOVE: Use shared templates
│
├── requirements.txt         # ✏️ UPDATE: Add textual, pyyaml
├── setup.py                 # ✅ KEEP: Package config
├── README.md                # ✏️ UPDATE: Phase 1 setup instructions
├── DEVELOPMENT.md           # ✅ KEEP: Dev docs
├── PLANNING_SESSION.md      # ✅ KEEP: Planning docs
├── REVIEW_FINDINGS.md       # ✅ KEEP: Review docs
├── VISUAL_OVERVIEW.md       # ✅ KEEP: Overview docs
└── PHASE_1_SPECIFICATION.md # ➕ NEW: This file
```

### File Status Legend
- ✅ KEEP: No changes needed
- ✏️ UPDATE: Modify existing file
- ➕ NEW: Create new file
- ❌ REMOVE: Delete file

---

## 🎯 PHASE 1 DELIVERABLES

### Deliverable 1: Dependencies Fixed
**Files Modified:**
- `requirements.txt`

**Changes:**
```txt
# Add to existing requirements:
textual>=0.40.0
rich>=13.0.0
pyyaml>=6.0.0
click>=8.0.0  (if not already present)
```

**Acceptance Criteria:**
- [ ] File contains all required packages
- [ ] Version numbers specified
- [ ] No conflicting dependencies
- [ ] `pip install -r requirements.txt` succeeds without errors

**Testing:**
```bash
cd /home/brassy/git/notes-tui
python -m venv test_venv
source test_venv/bin/activate
pip install -r requirements.txt
# Should complete without errors
deactivate
rm -rf test_venv
```

---

### Deliverable 2: Configuration System
**Files Created:**
- `config/default.yaml`
- `config/README.md`

**Files Modified:**
- `notes_tui/core/config.py`

**Changes:**

#### A. `config/default.yaml`
```yaml
# Complete config structure (as designed earlier)
# Must include:
- notes.directory
- notes.templates
- editor.default
- editor.fallback
- ui.layout settings
- keybindings
- behavior settings
```

**Acceptance Criteria:**
- [ ] Valid YAML syntax
- [ ] All required sections present
- [ ] Sensible default values
- [ ] Comments explaining each setting
- [ ] Points to correct notes directory path

#### B. `config/README.md`
```markdown
# Configuration Guide
- Explanation of each setting
- How to customize
- Examples
```

**Acceptance Criteria:**
- [ ] Clear documentation
- [ ] Example configurations
- [ ] Troubleshooting section

#### C. `notes_tui/core/config.py`
**Current:** Basic config class (needs verification)
**Updated:** Load from YAML, provide defaults, validate paths

**Required Methods:**
```python
class Config:
    def __init__(self, config_path=None):
        """Load config from file or use defaults"""
        
    def get(self, key, default=None):
        """Get config value using dot notation"""
        
    def validate(self):
        """Validate critical paths exist"""
        
    def get_notes_dir(self):
        """Return Path to notes directory"""
        
    def get_templates_dir(self):
        """Return Path to templates directory"""
        
    def get_editor(self):
        """Return configured editor"""
```

**Acceptance Criteria:**
- [ ] Loads default.yaml successfully
- [ ] Supports user config override (optional for Phase 1)
- [ ] Validates notes directory exists
- [ ] Validates templates directory exists
- [ ] Returns sensible defaults if file missing
- [ ] Provides helpful error messages

**Testing:**
```python
from notes_tui.core.config import Config

# Test 1: Load default config
config = Config()
assert config.get('editor.default') == 'nano'
assert config.get('ui.layout.tree_width') == 30

# Test 2: Validate paths
config.validate()  # Should not raise if paths exist

# Test 3: Get methods work
notes_dir = config.get_notes_dir()
assert notes_dir.exists()
```

---

### Deliverable 3: Editor Manager
**Files Created:**
- `notes_tui/core/editor_manager.py`

**Content:**
```python
"""
Editor integration for launching external editors
"""
import subprocess
import os
from pathlib import Path

class EditorManager:
    """Manages external editor launching"""
    
    def __init__(self, config):
        """Initialize with config"""
        
    def launch(self, file_path):
        """Launch editor with file, block until closed"""
        
    def get_editor_command(self):
        """Get editor command from config/env"""
        
    def is_editor_available(self, editor):
        """Check if editor exists in PATH"""
```

**Acceptance Criteria:**
- [ ] Launches nano successfully
- [ ] Blocks until editor closes
- [ ] Returns to TUI after editor exit
- [ ] Handles missing editor gracefully
- [ ] Respects $EDITOR if set
- [ ] Falls back to nano if configured editor unavailable

**Testing:**
```python
from notes_tui.core.editor_manager import EditorManager
from notes_tui.core.config import Config

config = Config()
editor_mgr = EditorManager(config)

# Test 1: Get editor command
editor = editor_mgr.get_editor_command()
assert editor in ['nano', 'vim', 'nvim']

# Test 2: Check availability
assert editor_mgr.is_editor_available('nano')

# Test 3: Launch editor (manual test)
# Should open nano, allow editing, return on exit
test_file = Path('/tmp/test_note.md')
test_file.write_text('# Test')
editor_mgr.launch(test_file)
```

---

### Deliverable 4: Template Manager Update
**Files Modified:**
- `notes_tui/core/template_manager.py`

**Changes:**
- Update `templates_dir` to use config path
- Point to shared templates in notes directory
- Remove dependency on local templates/

**Acceptance Criteria:**
- [ ] Reads templates from configured path
- [ ] Lists templates successfully
- [ ] Creates notes from templates
- [ ] No references to local templates/ folder

**Testing:**
```python
from notes_tui.core.template_manager import TemplateManager
from notes_tui.core.config import Config

config = Config()
tm = TemplateManager(config.get_templates_dir())

# Test 1: List templates
templates = tm.list_templates()
assert len(templates) > 0
assert 'general_note' in [t['name'] for t in templates]

# Test 2: Get template content
content = tm.get_template_content('general_note')
assert content is not None
assert 'title' in content
```

---

### Deliverable 5: App Integration
**Files Modified:**
- `notes_tui/app.py`
- `notes_tui/__main__.py`

**Changes:**

#### A. `notes_tui/__main__.py`
Add command-line argument support:
```python
import argparse
from pathlib import Path
from notes_tui.app import NotesApp

def main():
    parser = argparse.ArgumentParser(description='Notes TUI')
    parser.add_argument(
        '--notes-dir',
        type=Path,
        help='Path to notes directory'
    )
    parser.add_argument(
        '--config',
        type=Path,
        help='Path to config file'
    )
    args = parser.parse_args()
    
    app = NotesApp(
        notes_dir=args.notes_dir,
        config_path=args.config
    )
    app.run()
```

**Acceptance Criteria:**
- [ ] `python -m notes_tui` launches with defaults
- [ ] `python -m notes_tui --notes-dir /path` works
- [ ] `python -m notes_tui --config /path` works
- [ ] `python -m notes_tui --help` shows usage

#### B. `notes_tui/app.py`
Update to use new config system:
```python
class NotesApp(App):
    def __init__(self, notes_dir=None, config_path=None):
        super().__init__()
        
        # Load configuration
        self.config = Config(config_path)
        
        # Override notes_dir if provided
        if notes_dir:
            self.notes_dir = notes_dir
        else:
            self.notes_dir = self.config.get_notes_dir()
        
        # Initialize managers
        self.notes_manager = NotesManager(self.notes_dir)
        self.template_manager = TemplateManager(
            self.config.get_templates_dir()
        )
        self.editor_manager = EditorManager(self.config)
```

**Acceptance Criteria:**
- [ ] App initializes without errors
- [ ] Config loads successfully
- [ ] Managers initialize correctly
- [ ] Tree view shows files
- [ ] Preview shows markdown content

---

### Deliverable 6: Basic Navigation
**Files Modified:**
- `notes_tui/widgets/tree_view.py`

**Changes:**
- Ensure tree loads from configured notes directory
- Fix any integration issues
- Verify refresh works

**Acceptance Criteria:**
- [ ] Tree displays folder structure
- [ ] Arrow keys navigate
- [ ] Enter selects file
- [ ] Icons display correctly
- [ ] Folders expand/collapse

**Testing:**
```bash
# Manual test checklist:
1. Launch TUI
2. See folder tree on left
3. Use arrow keys to navigate
4. Press Enter on folder - should expand
5. Press Enter on file - should show preview
6. All files from notes directory visible
```

---

### Deliverable 7: Note Preview
**Files Modified:**
- `notes_tui/widgets/note_view.py` (verify works)

**Acceptance Criteria:**
- [ ] Selecting file shows preview
- [ ] Markdown renders correctly
- [ ] Scrolling works
- [ ] Large files handle gracefully
- [ ] Preview updates when selection changes

---

### Deliverable 8: Documentation Update
**Files Modified:**
- `README.md`

**Changes:**
Add Phase 1 setup section:
```markdown
## Quick Start

### Installation

1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure: Edit `config/default.yaml`
4. Run: `python -m notes_tui --notes-dir /path/to/notes`

### Configuration

See `config/README.md` for detailed configuration options.
```

**Acceptance Criteria:**
- [ ] Clear installation steps
- [ ] Configuration instructions
- [ ] Usage examples
- [ ] Troubleshooting section

---

## ✅ PHASE 1 ACCEPTANCE CRITERIA

### Functional Requirements
- [ ] **FR1:** TUI launches without errors
- [ ] **FR2:** Configuration loads from YAML file
- [ ] **FR3:** Notes directory path is configurable
- [ ] **FR4:** Tree view displays folder structure
- [ ] **FR5:** Preview shows markdown content
- [ ] **FR6:** Arrow keys navigate tree
- [ ] **FR7:** Enter key selects/expands items
- [ ] **FR8:** 'q' quits application
- [ ] **FR9:** Editor manager can launch nano
- [ ] **FR10:** Template manager reads shared templates

### Non-Functional Requirements
- [ ] **NFR1:** TUI starts in under 2 seconds
- [ ] **NFR2:** Navigation is responsive (<100ms)
- [ ] **NFR3:** No crashes during normal use
- [ ] **NFR4:** Clear error messages if config invalid
- [ ] **NFR5:** Memory usage under 100MB

### Technical Requirements
- [ ] **TR1:** All dependencies install cleanly
- [ ] **TR2:** Config validates on load
- [ ] **TR3:** Paths resolve correctly
- [ ] **TR4:** Code follows existing style
- [ ] **TR5:** No duplicate templates folder

---

## 🧪 PHASE 1 TESTING PLAN

### Test Suite 1: Installation
```bash
# Test clean install
cd /home/brassy/git/notes-tui
rm -rf venv  # Clean slate
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Expected: No errors, all packages installed
```

### Test Suite 2: Configuration
```bash
# Test config loading
python -c "from notes_tui.core.config import Config; c = Config(); print(c.get('editor.default'))"
# Expected: 'nano'

# Test path validation
python -c "from notes_tui.core.config import Config; c = Config(); c.validate()"
# Expected: No errors if paths exist, clear error if not
```

### Test Suite 3: Launch
```bash
# Test default launch
python -m notes_tui
# Expected: TUI opens, shows tree and preview

# Test with custom notes dir
python -m notes_tui --notes-dir /home/brassy/Docker/notes
# Expected: TUI shows files from that directory
```

### Test Suite 4: Navigation
```
Manual test checklist:
1. [ ] Launch TUI
2. [ ] Tree displays on left (30% width)
3. [ ] Preview area on right (70% width)
4. [ ] Press ↓ - cursor moves down
5. [ ] Press ↑ - cursor moves up
6. [ ] Press → on folder - expands
7. [ ] Press ← on expanded - collapses
8. [ ] Press Enter on file - preview shows content
9. [ ] Preview shows formatted markdown
10. [ ] Press 'q' - application exits cleanly
```

### Test Suite 5: Integration
```python
# Test full integration
from pathlib import Path
from notes_tui.core.config import Config
from notes_tui.core.notes_manager import NotesManager
from notes_tui.core.template_manager import TemplateManager
from notes_tui.core.editor_manager import EditorManager

# Load config
config = Config()
assert config.validate() is None  # No errors

# Initialize managers
notes_mgr = NotesManager(config.get_notes_dir())
tmpl_mgr = TemplateManager(config.get_templates_dir())
edit_mgr = EditorManager(config)

# Test they work together
notes = notes_mgr.get_all_notes()
assert len(notes) > 0

templates = tmpl_mgr.list_templates()
assert len(templates) > 0

editor = edit_mgr.get_editor_command()
assert editor in ['nano', 'vim']
```

---

## 📊 PHASE 1 SUCCESS METRICS

### Must Pass (Go/No-Go)
- [ ] All FR1-FR10 met
- [ ] All test suites pass
- [ ] Zero crashes in 10-minute usage
- [ ] Configuration works end-to-end

### Quality Indicators
- [ ] Code is clean and documented
- [ ] Error messages are helpful
- [ ] Performance is smooth
- [ ] User can follow README to setup

### Completion Criteria
**Phase 1 is DONE when:**
1. User can install dependencies
2. User can configure notes directory
3. User can launch TUI
4. User can browse notes visually
5. User can preview note content
6. All testing passes
7. Documentation is updated

**Phase 1 is NOT done until:**
- All acceptance criteria checked ✅
- All tests pass ✅
- Code reviewed ✅
- User approves ✅

---

## 🎯 DELIVERABLES SUMMARY

| # | Deliverable | Files | Status | Priority |
|---|-------------|-------|--------|----------|
| 1 | Dependencies | requirements.txt | Not Started | Critical |
| 2 | Configuration | config/*.yaml, core/config.py | Not Started | Critical |
| 3 | Editor Manager | core/editor_manager.py | Not Started | Critical |
| 4 | Template Update | core/template_manager.py | Not Started | High |
| 5 | App Integration | app.py, __main__.py | Not Started | Critical |
| 6 | Navigation | widgets/tree_view.py | Not Started | High |
| 7 | Preview | widgets/note_view.py | Not Started | High |
| 8 | Documentation | README.md, config/README.md | Not Started | Medium |

---

## 📝 REVIEW CHECKLIST

Before starting implementation:
- [ ] Folder structure approved
- [ ] All deliverables defined
- [ ] Acceptance criteria clear
- [ ] Testing plan complete
- [ ] Success metrics agreed
- [ ] User reviewed and approved

---

## 🚦 NEXT STEPS

1. **User reviews this specification**
2. **User approves or requests changes**
3. **Begin implementation only after approval**
4. **Complete deliverables in order**
5. **Test after each deliverable**
6. **User acceptance testing at end**

---

**This specification should answer:**
- ✅ What are we building?
- ✅ How do we know it's done?
- ✅ How do we test it?
- ✅ What does success look like?

**Ready for your review!** 📋
