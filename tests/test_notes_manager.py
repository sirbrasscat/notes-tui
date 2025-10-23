"""
Tests for Notes Manager
"""

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from notes_tui.core.notes_manager import NotesManager


@pytest.fixture
def temp_notes_dir():
    """Create a temporary notes directory for testing"""
    with TemporaryDirectory() as tmpdir:
        # Create directory structure
        tmpdir = Path(tmpdir)
        (tmpdir / 'work').mkdir()
        (tmpdir / 'personal').mkdir()
        (tmpdir / 'journals').mkdir()
        
        # Create some test notes
        (tmpdir / 'work' / 'project.md').write_text('# Work Project\nThis is a test')
        (tmpdir / 'personal' / 'thoughts.md').write_text('# My Thoughts\nPersonal notes')
        
        yield tmpdir


def test_notes_manager_initialization(temp_notes_dir):
    """Test NotesManager initialization"""
    manager = NotesManager(temp_notes_dir)
    assert manager.root_dir == temp_notes_dir


def test_get_all_notes(temp_notes_dir):
    """Test getting all notes"""
    manager = NotesManager(temp_notes_dir)
    notes = manager.get_all_notes()
    assert len(notes) == 2


def test_get_notes_by_category(temp_notes_dir):
    """Test getting notes by category"""
    manager = NotesManager(temp_notes_dir)
    work_notes = manager.get_notes_by_category('work')
    assert len(work_notes) == 1
    assert work_notes[0].name == 'project.md'


def test_read_note(temp_notes_dir):
    """Test reading note content"""
    manager = NotesManager(temp_notes_dir)
    note_path = (temp_notes_dir / 'work' / 'project.md')
    content = manager.read_note(note_path)
    assert 'Work Project' in content


def test_create_note(temp_notes_dir):
    """Test creating a new note"""
    manager = NotesManager(temp_notes_dir)
    note_path = manager.create_note('work', 'new_note', '# New Note\nContent')
    
    assert note_path is not None
    assert note_path.exists()
    assert 'New Note' in note_path.read_text()


def test_delete_note(temp_notes_dir):
    """Test deleting a note"""
    manager = NotesManager(temp_notes_dir)
    note_path = (temp_notes_dir / 'work' / 'project.md')
    
    assert note_path.exists()
    manager.delete_note(note_path)
    assert not note_path.exists()


def test_search_notes(temp_notes_dir):
    """Test searching notes"""
    manager = NotesManager(temp_notes_dir)
    results = manager.search_notes('test')
    assert len(results) == 1
    assert 'project.md' in str(results[0])
