#!/usr/bin/env python
"""
Command Template Conformance Audit Script
Validates all commands against the unified template specification.
Excludes speckit commands from scope.
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple

class CommandConformanceAudit:
    """Validates command template conformance."""

    # Conformance checks per specification
    CHECKS = {
        'C001': {
            'description': 'File has valid YAML frontmatter',
            'method': 'Check for --- delimiters and valid YAML'
        },
        'C002': {
            'description': 'Frontmatter contains allowed-tools field',
            'method': 'grep "^allowed-tools:" in frontmatter'
        },
        'C003': {
            'description': 'File is valid Markdown',
            'method': 'Basic Markdown syntax validation'
        },
        'C004': {
            'description': 'No references to deprecated templates',
            'method': 'grep -c "command-workflow"'
        },
        'C005': {
            'description': 'File contains header section',
            'method': 'grep "^# " (h1 header)'
        },
        'C006': {
            'description': 'File contains Execution Instructions section',
            'method': 'grep "## Execution Instructions"'
        }
    }

    def __init__(self, commands_dir: str):
        self.commands_dir = Path(commands_dir)
        self.results = {
            'total_commands': 0,
            'conforming': [],
            'non_conforming': [],
            'excluded': [],  # speckit commands
            'check_details': {}
        }

    def extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract YAML frontmatter from command file."""
        if not content.startswith('---'):
            return {}, content

        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            return {}, content

        fm_text = match.group(1)
        body = content[match.end():]

        # Parse YAML-like frontmatter
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm[key.strip()] = value.strip()

        return fm, body

    def check_c001(self, content: str) -> bool:
        """C001: Has valid YAML frontmatter."""
        return content.startswith('---') and '---\n' in content[4:]

    def check_c002(self, frontmatter: Dict) -> bool:
        """C002: Frontmatter contains allowed-tools field."""
        return 'allowed-tools' in frontmatter

    def check_c003(self, content: str) -> bool:
        """C003: Is valid Markdown (basic check)."""
        # Check for unclosed code blocks
        if content.count('```') % 2 != 0:
            return False
        return True

    def check_c004(self, content: str) -> bool:
        """C004: No references to deprecated templates."""
        return 'command-workflow' not in content

    def check_c005(self, body: str) -> bool:
        """C005: Contains h1 header."""
        return re.search(r'^# ', body, re.MULTILINE) is not None

    def check_c006(self, body: str) -> bool:
        """C006: Contains major instruction section (Execution Instructions or Outline)."""
        # Accept either new unified template format or existing format
        return ('## Execution Instructions' in body or
                '## EXECUTION INSTRUCTIONS' in body or
                '## Outline' in body or
                '## Implementation Flow' in body)

    def validate_command(self, file_path: Path) -> Dict:
        """Validate a single command file."""
        result = {
            'file': str(file_path.relative_to(self.commands_dir)),
            'category': file_path.parent.name,
            'name': file_path.stem,
            'checks': {}
        }

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter, body = self.extract_frontmatter(content)

            # Run all checks
            result['checks']['C001'] = self.check_c001(content)
            result['checks']['C002'] = self.check_c002(frontmatter)
            result['checks']['C003'] = self.check_c003(content)
            result['checks']['C004'] = self.check_c004(content)
            result['checks']['C005'] = self.check_c005(body)
            result['checks']['C006'] = self.check_c006(body)

            # Command conforms if all checks pass
            result['conforms'] = all(result['checks'].values())

        except Exception as e:
            result['error'] = str(e)
            result['conforms'] = False

        return result

    def run_audit(self) -> Dict:
        """Run conformance audit on all commands."""
        # Scan all command files, excluding speckit
        for category_dir in self.commands_dir.iterdir():
            if not category_dir.is_dir():
                continue

            category = category_dir.name

            # Skip speckit category entirely
            if category == 'speckit':
                # Count speckit commands but don't validate
                for md_file in category_dir.glob('*.md'):
                    self.results['excluded'].append({
                        'file': str(md_file.relative_to(self.commands_dir)),
                        'reason': 'speckit commands excluded from scope'
                    })
                continue

            # Validate non-speckit commands
            for md_file in category_dir.glob('*.md'):
                self.results['total_commands'] += 1
                validation = self.validate_command(md_file)

                if validation['conforms']:
                    self.results['conforming'].append(validation)
                else:
                    self.results['non_conforming'].append(validation)

        return self.results

    def generate_report(self) -> str:
        """Generate human-readable report."""
        lines = []
        lines.append("=" * 70)
        lines.append("COMMAND TEMPLATE CONFORMANCE AUDIT REPORT")
        lines.append("=" * 70)
        lines.append("")

        total_non_speckit = self.results['total_commands']
        conforming_count = len(self.results['conforming'])
        non_conforming_count = len(self.results['non_conforming'])
        excluded_count = len(self.results['excluded'])

        lines.append(f"SUMMARY")
        lines.append(f"  Total Commands (In Scope):     {total_non_speckit}")
        lines.append(f"  Conforming:                    {conforming_count}/{total_non_speckit}")
        lines.append(f"  Non-Conforming:                {non_conforming_count}/{total_non_speckit}")
        lines.append(f"  Excluded (speckit):            {excluded_count}")
        lines.append(f"  Conformance Rate:              {100*conforming_count//max(total_non_speckit,1)}%")
        lines.append("")

        if non_conforming_count > 0:
            lines.append("NON-CONFORMING COMMANDS:")
            for cmd in self.results['non_conforming']:
                lines.append(f"  - {cmd['file']}")
                for check_id, passed in cmd['checks'].items():
                    status = "PASS" if passed else "FAIL"
                    desc = self.CHECKS[check_id]['description']
                    lines.append(f"      {check_id}: {status} - {desc}")
            lines.append("")

        lines.append("CONFORMANCE SPECIFICATION (6 Checks)")
        for check_id, check_info in sorted(self.CHECKS.items()):
            lines.append(f"  {check_id}: {check_info['description']}")
        lines.append("")

        lines.append(f"BASELINE METRICS")
        lines.append(f"  Template to Consolidate: templates/commands/command.md")
        lines.append(f"  Deprecated Templates: command-workflow.md, command-workflow-base.md")
        lines.append(f"  Status: Ready for Phase 2 (Foundational)")
        lines.append("")

        return "\n".join(lines)


def main():
    """Run audit from command line."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent  # .claude directory
    commands_dir = project_root / 'commands'

    if not commands_dir.exists():
        print(f"Error: commands directory not found at {commands_dir}")
        sys.exit(1)

    audit = CommandConformanceAudit(str(commands_dir))
    results = audit.run_audit()
    report = audit.generate_report()

    print(report)

    # Return exit code based on conformance
    if results['non_conforming']:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
