"""
Entry point for the Notes TUI application
"""

import sys
from notes_tui.app import NotesApp


def main():
    """Run the Notes TUI application"""
    app = NotesApp()
    app.run()


if __name__ == "__main__":
    main()
