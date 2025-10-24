"""
Entry point for the Notes TUI application
"""

import sys
import argparse
from pathlib import Path
from notes_tui.app import NotesApp


def main():
    """Run the Notes TUI application"""
    parser = argparse.ArgumentParser(
        description="Notes TUI - Personal Markdown Notebook",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  notes-tui                     # Use default config
  notes-tui -c custom.yaml      # Use custom config file
  notes-tui --version           # Show version
        """
    )
    
    parser.add_argument(
        '-c', '--config',
        type=Path,
        metavar='FILE',
        help='Path to custom configuration file'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Notes TUI 0.1.0 (Phase 1)'
    )
    
    args = parser.parse_args()
    
    try:
        app = NotesApp(config_path=args.config)
        app.run()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
