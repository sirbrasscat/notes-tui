"""
Tests for Search functionality
"""

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from notes_tui.core.search import Search


@pytest.fixture
def temp_notes_with_search():
    """Create temporary notes for search testing"""
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create test notes with specific content
        (tmpdir / 'note1.md').write_text('# Python Tutorial\nPython is great')
        (tmpdir / 'note2.md').write_text('# JavaScript Guide\nJavaScript basics')
        (tmpdir / 'note3.md').write_text('# Python Advanced\nAdvanced Python topics')
        
        yield tmpdir


def test_search_initialization(temp_notes_with_search):
    """Test Search initialization"""
    search = Search(temp_notes_with_search)
    assert search.root_dir == temp_notes_with_search


def test_search_basic(temp_notes_with_search):
    """Test basic search functionality"""
    search = Search(temp_notes_with_search)
    results = search.search('Python')
    
    assert len(results) == 2
    assert all('python' in r['relative_path'].name.lower() or 
               any('Python' in line[1] for line in r['lines']) 
               for r in results)


def test_search_case_insensitive(temp_notes_with_search):
    """Test case-insensitive search"""
    search = Search(temp_notes_with_search)
    
    results_upper = search.search('PYTHON')
    results_lower = search.search('python')
    
    assert len(results_upper) == len(results_lower)


def test_search_no_results(temp_notes_with_search):
    """Test search with no results"""
    search = Search(temp_notes_with_search)
    results = search.search('NonExistentQuery')
    
    assert len(results) == 0


def test_search_results_sorted(temp_notes_with_search):
    """Test that search results are sorted by match count"""
    search = Search(temp_notes_with_search)
    results = search.search('Python')
    
    # First result should have more matches
    if len(results) > 1:
        assert results[0]['matches'] >= results[1]['matches']
