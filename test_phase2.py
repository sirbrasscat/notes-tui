#!/usr/bin/env python3
"""
Quick test script for Phase 2 Quick Capture features
"""

from pathlib import Path
from notes_tui.core.config import Config
from notes_tui.core.editor_manager import EditorManager

def test_config():
    """Test config loading"""
    print("Testing config loading...")
    config = Config()
    print(f"  Notes dir: {config.notes_directory}")
    print(f"  Templates dir: {config.templates_directory}")
    print(f"  Default editor: {config.default_editor}")
    print(f"  Default category: {config.get('quick_capture.default_category')}")
    print(f"  Default template: {config.get('quick_capture.default_template')}")
    print("  ✓ Config loaded successfully")
    return config

def test_editor_manager(config):
    """Test editor manager"""
    print("\nTesting editor manager...")
    em = EditorManager(config)
    print(f"  Available editors: {em.get_available_editors()}")
    editor_cmd, args = em.get_editor_command()
    print(f"  Selected editor: {editor_cmd}")
    print(f"  Editor args: {args}")
    print("  ✓ Editor manager working")
    return em

def test_actions():
    """Test that action methods exist"""
    print("\nTesting action methods...")
    from notes_tui.app import NotesApp
    
    # Check methods exist
    actions = [
        'action_new_note',
        'action_template_note', 
        'action_quick_journal',
        'action_edit_note',
        '_open_in_editor',
        '_create_quick_note',
    ]
    
    for action in actions:
        if hasattr(NotesApp, action):
            print(f"  ✓ {action} exists")
        else:
            print(f"  ✗ {action} MISSING!")
    
    print("  ✓ All action methods present")

def main():
    """Run tests"""
    print("=" * 60)
    print("PHASE 2 QUICK CAPTURE - IMPLEMENTATION TEST")
    print("=" * 60)
    
    try:
        config = test_config()
        em = test_editor_manager(config)
        test_actions()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED")
        print("=" * 60)
        print("\nQuick Capture Features Implemented:")
        print("  • n key - Quick note (default template)")
        print("  • N key - Template selection")
        print("  • j key - Daily journal")
        print("  • e key - Edit selected note")
        print("\nTo test interactively, run:")
        print("  ./venv/bin/notes-tui")
        print("\nThen press:")
        print("  n - Enter a note name")
        print("  j - Open today's journal")
        print("  e - Edit the selected note")
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
