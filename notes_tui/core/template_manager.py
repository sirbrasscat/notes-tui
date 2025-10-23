"""
Template manager for creating notes from templates
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import re


class TemplateManager:
    """Manages note templates and creation from templates"""
    
    def __init__(self, templates_dir: Optional[Path] = None):
        """Initialize the template manager
        
        Args:
            templates_dir: Directory containing template files
        """
        if templates_dir is None:
            # Default to templates directory in project root
            self.templates_dir = Path(__file__).parent.parent.parent / "templates"
        else:
            self.templates_dir = Path(templates_dir)
        
        self.templates_dir.mkdir(exist_ok=True)
    
    def list_templates(self) -> List[Dict[str, str]]:
        """Get list of available templates
        
        Returns:
            List of dicts with template info (name, path, description)
        """
        templates = []
        
        if not self.templates_dir.exists():
            return templates
        
        for template_file in sorted(self.templates_dir.glob("*.md")):
            templates.append({
                "name": template_file.stem,
                "filename": template_file.name,
                "path": str(template_file),
                "description": self._get_template_description(template_file)
            })
        
        return templates
    
    def _get_template_description(self, template_path: Path) -> str:
        """Extract description from template frontmatter
        
        Args:
            template_path: Path to template file
            
        Returns:
            Description of the template
        """
        # Map template names to friendly descriptions
        descriptions = {
            "budget_entry": "Budget tracking with income, expenses, and savings",
            "daily_journal": "Daily reflection and logging",
            "general_note": "General purpose note template",
            "learning_note": "Learning and educational content",
            "meeting_notes": "Meeting notes with agenda and action items",
            "project": "Project planning and tracking"
        }
        
        return descriptions.get(template_path.stem, "Note template")
    
    def get_template_content(self, template_name: str) -> Optional[str]:
        """Get the raw content of a template
        
        Args:
            template_name: Name of the template (without .md extension)
            
        Returns:
            Template content or None if not found
        """
        template_path = self.templates_dir / f"{template_name}.md"
        
        if not template_path.exists():
            return None
        
        return template_path.read_text(encoding="utf-8")
    
    def create_note_from_template(
        self, 
        template_name: str, 
        output_path: Path,
        variables: Optional[Dict[str, str]] = None
    ) -> bool:
        """Create a new note from a template
        
        Args:
            template_name: Name of the template to use
            output_path: Path where the new note will be created
            variables: Dict of variables to substitute in the template
            
        Returns:
            True if successful, False otherwise
        """
        template_content = self.get_template_content(template_name)
        
        if template_content is None:
            return False
        
        # Default variables
        default_vars = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "title": output_path.stem.replace("-", " ").replace("_", " ").title(),
        }
        
        # Merge with provided variables
        if variables:
            default_vars.update(variables)
        
        # Process template (simple Jinja2-like variable substitution)
        processed_content = self._process_template(template_content, default_vars)
        
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the new note
        output_path.write_text(processed_content, encoding="utf-8")
        
        return True
    
    def _process_template(self, content: str, variables: Dict[str, str]) -> str:
        """Process template by substituting variables
        
        Args:
            content: Template content
            variables: Variables to substitute
            
        Returns:
            Processed content
        """
        # Simple variable substitution for {{ variable }} patterns
        for key, value in variables.items():
            # Handle simple variables: {{ variable }}
            content = content.replace(f"{{{{ {key} }}}}", str(value))
            
        # Handle variables with default values: {{ variable|default('value') }}
        def replace_with_default(match):
            var_name = match.group(1).strip()
            default_value = match.group(2).strip().strip("'\"")
            
            return variables.get(var_name, default_value)
        
        # Pattern: {{ variable|default('value') }} or {{ variable|default("value") }}
        content = re.sub(
            r'\{\{\s*(\w+)\s*\|\s*default\(["\']([^"\']*?)["\']\)\s*\}\}',
            replace_with_default,
            content
        )
        
        # Handle array defaults: {{ tags|default(['tag1', 'tag2']) }}
        def replace_array_default(match):
            var_name = match.group(1).strip()
            default_array = match.group(2).strip()
            
            if var_name in variables:
                return variables[var_name]
            return default_array
        
        content = re.sub(
            r'\{\{\s*(\w+)\s*\|\s*default\((\[.*?\])\)\s*\}\}',
            replace_array_default,
            content
        )
        
        return content
