# NOTES-TUI PLANNING SESSION
**Date:** October 23, 2025  
**Goal:** Distraction-free, friction-free TUI for rapid thought capture

---

## 📋 CURRENT STATE ANALYSIS

### What You've Built (Notes System)
**Strong Foundation - Production Ready**
- ✅ Complete CLI tools (7 commands: new, journal, search, serve, links, stats, backup)
- ✅ Robust category system (work, personal, journals, learning, budgets)
- ✅ Template engine with 6 templates using Jinja2
- ✅ MkDocs web viewer with Material theme
- ✅ Wiki-links support (`[[note-name]]`)
- ✅ Comprehensive test suite
- ✅ Docker deployment ready
- ✅ Well-documented (USAGE, CONFIGURATION, TEMPLATES guides)

**Core Architecture:**
- Python CLI with Click framework
- YAML configuration system
- Template rendering with variable substitution
- Full-text search functionality
- Link validation and suggestions
- Statistics and backup automation

### What You've Built (Notes-TUI)
**Partial Implementation - Needs Focus**
- ✅ Basic Textual app structure (`app.py`)
- ✅ NotesManager core logic
- ✅ Template system (duplicated from main project)
- ✅ Tree view widget for file browsing
- ✅ Note preview widget (markdown rendering)
- ✅ Template selection dialog
- ✅ Input dialog for note names
- ✅ Status bar widget
- ⚠️ **Missing dependencies** (textual not installed)
- ⚠️ **Not tested** - unclear what works
- ⚠️ **No actual note editing** - only viewing
- ⚠️ **Search not implemented** - just placeholder
- ⚠️ **Delete not implemented** - just placeholder

---

## 🎯 YOUR VISION (CLARIFIED)

### Primary Goal
**"Distraction-free, simple, friction-free TUI to get thoughts down with zero frustration"**

### Use Case Separation
1. **TUI = Quick Capture** - Fast, keyboard-driven thought dumping
2. **MkDocs = Review & Polish** - Beautiful reading, sharing, finalizing

### Core Requirements
- **Speed:** Open → Type → Save in seconds
- **Simplicity:** Minimal UI, maximum functionality
- **Keyboard-first:** Everything via hotkeys
- **Zero friction:** No dialogs unless necessary
- **Focus mode:** Writing without distraction

---

## 🔍 KEY FINDINGS

### Strengths
1. **Solid backend** - NotesManager is well-designed
2. **Template system exists** - Can reuse from main project
3. **Clear architecture** - Good separation of concerns
4. **Textual framework** - Modern, powerful TUI library

### Issues Identified
1. **Over-engineered for capture** - Too many dialogs, steps
2. **Missing core feature** - Can't actually edit notes in TUI
3. **Dependency confusion** - Two separate projects, unclear integration
4. **Template duplication** - Same templates in two places
5. **No quick capture flow** - Current flow: `n` → select template → enter name → external editor
6. **Missing critical bindings** - No quick journal, no direct edit

### Rabbit Holes Detected
1. **Building full editor** - You don't need vim in terminal
2. **Feature parity** - Trying to match web app features
3. **Complex dialogs** - Overcomplicating quick capture
4. **Search UI** - Not needed for capture workflow

---

## 💡 PROPOSED SOLUTION

### Core Philosophy
**"The TUI is a QUICK NOTE LAUNCHER, not a full editor"**

### Simplified Workflow
```
OPTION A: Quick Capture
Press `n` → Type filename → Opens in $EDITOR → Done
(Skip template selection for speed)

OPTION B: Daily Journal  
Press `j` → Opens today's journal in $EDITOR → Done
(No prompts, just open)

OPTION C: Browse & Edit
Navigate tree → Press `e` → Opens in $EDITOR → Done
(View in TUI, edit externally)

OPTION D: Template-based
Press `N` (shift+n) → Select template → Name → Opens in $EDITOR
(For when you need structure)
```

### Key Insight
**Don't build an editor - leverage external editor (vim, nano, code, etc.)**

---

## 📐   

### Decision 1: Single Project or Two?
**Recommendation: Keep Separate but Unified**
- `notes/` - Main system with CLI, MkDocs, full tooling
- `notes-tui/` - Lightweight launcher pointing to same notes directory
- Share templates via config/symlink
- TUI focuses on launching editor, not duplicating features

### Decision 2: What Does TUI Actually Do?
**Recommendation: File Navigator + Editor Launcher**
1. Browse notes in tree view
2. Preview markdown (read-only)
3. Launch external editor on demand
4. Quick capture with hotkeys
5. Basic search (grep-based, simple)

### Decision 3: Template System
**Recommendation: Reuse, Don't Duplicate**
- Point TUI to main project's `.templates/` folder
- Use same template engine
- Share configuration via `config.yaml`

### Decision 4: Editor Strategy
**Recommendation: Shell Out to $EDITOR**
```python
# In TUI, when user presses 'e' or 'n'
subprocess.run([editor, note_path])
# When they exit editor, refresh TUI view
```

---

## 🗺️ IMPLEMENTATION PLAN

### Phase 1: Fix Foundation (1-2 hours)
**Goal: Get TUI running and stable**

1. **Install dependencies**
   - Add textual, rich to requirements.txt
   - Set up proper venv
   - Test basic launch

2. **Configuration integration**
   - Point to main notes directory
   - Read main project's config.yaml
   - Share template directory

3. **Core widget fixes**
   - Fix tree view refresh
   - Test note preview rendering
   - Ensure status bar updates

4. **Basic navigation**
   - Arrow keys work
   - Enter to preview
   - Q to quit

### Phase 2: Quick Capture (2-3 hours)
**Goal: Make note creation instant**

1. **Implement `n` - Quick note**
   ```
   User presses 'n'
   → Prompt for filename (simple input)
   → Create in 'personal' by default
   → Open in $EDITOR immediately
   → Refresh tree when editor closes
   ```

2. **Implement `j` - Instant journal**
   ```
   User presses 'j'
   → Check if today's journal exists
   → If not, create from daily_journal template
   → Open in $EDITOR immediately
   → No questions asked
   ```

3. **Implement `e` - Edit selected**
   ```
   User navigates to note
   → Press 'e'
   → Open that note in $EDITOR
   → Refresh view when done
   ```

4. **Implement `N` - Template-based creation**
   ```
   User presses Shift+N
   → Show template dialog (existing code)
   → Get filename
   → Create from template
   → Open in $EDITOR
   ```

### Phase 3: Essential Features (2-3 hours)
**Goal: Polish the experience**

1. **Config-driven editor**
   - Read `default_editor` from config.yaml
   - Support environment variable $EDITOR
   - Fallback to sensible default (nano/vim)

2. **Category selection**
   - Quick picker for category (optional)
   - Or smart defaults (personal for `n`, journals for `j`)

3. **Recent files**
   - Show recently modified notes at top
   - Or add `r` to see recent list

4. **Basic search**
   - Press `/` → Enter query
   - Use grep under the hood
   - Show results in tree view
   - Jump to file on select

5. **Delete functionality**
   - Press `d` on selected note
   - Confirm with y/n
   - Move to trash or delete

### Phase 4: Polish (1-2 hours)
**Goal: Make it beautiful and smooth**

1. **Status messages**
   - "Created: note-name.md"
   - "Opening in editor..."
   - "Note updated"

2. **Keyboard help**
   - Press `?` for help screen
   - Show all keybindings

3. **Error handling**
   - Graceful editor failures
   - Invalid filename handling
   - Missing template warnings

4. **Theme/Colors**
   - Use Textual CSS for clean look
   - Minimal, distraction-free aesthetic
   - Good contrast for reading

---

## ⚠️ WHAT TO AVOID

### Anti-Patterns
1. ❌ **Building text editor in TUI** - Use external editor
2. ❌ **Complex template wizard** - Keep it fast
3. ❌ **Feature parity with web** - Different use cases
4. ❌ **Advanced search UI** - Simple grep is enough
5. ❌ **Settings dialogs** - Use config file
6. ❌ **Git integration** - Handle externally
7. ❌ **Sync features** - Out of scope
8. ❌ **Preview editing** - Read-only preview only

### Rabbit Holes to Skip
- Markdown WYSIWYG editing
- Collaborative features
- Mobile support
- Web server integration
- Plugin system
- Theme customization UI
- Tag management UI
- Statistics dashboard

---

## 🎯 SUCCESS CRITERIA

### Must Have (MVP)
- [ ] Launch TUI in under 1 second
- [ ] Press `n` → filename → opens in editor in under 5 seconds
- [ ] Press `j` → today's journal opens immediately
- [ ] Navigate tree with arrow keys smoothly
- [ ] Preview notes without lag
- [ ] Edit existing notes with `e`
- [ ] Delete notes with `d` + confirmation
- [ ] All keybindings visible in footer
- [ ] Zero crashes during normal use

### Nice to Have (Polish)
- [ ] Press `/` for simple search
- [ ] Press `r` to see recent notes
- [ ] Press `?` for help
- [ ] Smart category defaults
- [ ] Template picker (Shift+N)
- [ ] Status messages for feedback
- [ ] Configurable editor via config.yaml
- [ ] Tree auto-refresh after edits

### Success Metrics
**Time to capture a thought:**
- Current (web): ~30 seconds (open browser, click, type, save)
- Current (CLI): ~20 seconds (terminal, command, type, enter editor)
- **Target (TUI): <10 seconds** (already open, press 'n', type)

---

## 🔄 ITERATION PLAN

### Week 1: Foundation
- Fix dependencies and configuration
- Get TUI running reliably
- Basic tree navigation working
- Preview working smoothly

### Week 2: Core Features
- Quick capture (`n`)
- Instant journal (`j`)
- Edit existing (`e`)
- Delete with confirm (`d`)

### Week 3: Polish
- Simple search (`/`)
- Help screen (`?`)
- Status messages
- Error handling
- Clean up UI

### Week 4: Integration
- Test with real workflow
- Document TUI usage
- Update README with workflows
- Video/GIF demo
- Gather feedback

---

## 🤔 OPEN QUESTIONS

### Configuration
**Q:** Single config.yaml or separate for TUI?  
**A:** Share main project's config, TUI-specific in `[tui]` section

**Q:** Where should TUI templates live?  
**A:** Point to main project's `.templates/` directory

### User Experience
**Q:** Default category for quick notes?  
**A:** Start with 'personal', make configurable

**Q:** Should `j` check for existing journal?  
**A:** Yes, open if exists, create if not

**Q:** Template picker - modal or inline?  
**A:** Keep modal for `N`, skip for `n`

### Technical
**Q:** How to detect editor closed?  
**A:** `subprocess.run()` blocks until editor exits

**Q:** Auto-refresh tree after edit?  
**A:** Yes, watch for file mtime changes

**Q:** Handle vim/nano/code differently?  
**A:** No, treat all editors the same via shell

---

## 📝 LESSONS LEARNED (PRE-IMPLEMENTATION)

### What Went Well
1. **Solid foundation** - Main CLI project is excellent
2. **Clear use cases** - Web vs TUI separation makes sense
3. **Good tooling** - Textual is right framework choice
4. **Template system** - Reusable, well-designed

### What Needs Change
1. **Over-engineering** - Current TUI too complex for capture
2. **Scope creep** - Trying to duplicate web features
3. **Missing core** - No actual editing capability
4. **Duplication** - Templates and logic in two places

### Key Insights
1. **Editor is better external** - Don't reinvent vim/code
2. **Speed is everything** - Each dialog adds friction
3. **Smart defaults beat options** - Don't ask, just do
4. **Simple wins** - Grep-based search > fancy UI

---

## 🎬 NEXT STEPS

### Immediate Actions
1. **Review this plan** together
2. **Clarify any questions** you have
3. **Prioritize features** if needed
4. **Start with Phase 1** - Fix foundation

### Before Writing Code
- [ ] Agree on editor strategy (external vs built-in)
- [ ] Confirm keybinding scheme
- [ ] Decide on category defaults
- [ ] Review template sharing approach
- [ ] Validate success criteria

### Ready to Code When
- [ ] Plan approved
- [ ] Questions answered
- [ ] Priorities clear
- [ ] Test environment ready

---

## 💭 FINAL THOUGHTS

### Your Strength
You've built an excellent markdown note system with professional-grade CLI tools. The foundation is rock solid.

### The Opportunity  
A TUI that's a **lightning-fast launcher** for your existing system, not a duplicate of it.

### The Risk
Getting lost in building features that slow down the core workflow: **capturing thoughts instantly**.

### The Path Forward
Keep it simple. Keep it fast. Leverage what you've built. Launch editors, don't replace them.

---

**Remember:** Perfect is the enemy of good. A simple, fast TUI that you actually use daily is infinitely better than a feature-complete one you avoid because it's too complex.

Ready to build this? Let's start with Phase 1! 🚀
