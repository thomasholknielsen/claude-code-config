#!/usr/bin/env python3
"""Fix incorrect closing code fence syntax across all markdown files."""

from pathlib import Path
import re
import sys


def fix_closing_fences(file_path: Path) -> tuple[bool, int]:
    """
    Fix closing code fences that incorrectly specify language tags.

    Args:
        file_path: Path to markdown file to fix

    Returns:
        Tuple of (was_modified, count_of_fixes)
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        original_content = content

        # Pattern: Match closing fence with language tag at end of line
        # This will match ```bash, ```text, ```yaml, etc. when they appear alone on a line
        pattern = r"^```(bash|text|yaml|python|json|plaintext|javascript|typescript|jsx|tsx|markdown|md|sh|shell|sql|graphql|html|css|scss|less|xml|dockerfile|makefile|toml|ini|properties|diff|patch)$"

        # Replace with just ```
        content = re.sub(pattern, "```", content, flags=re.MULTILINE)

        if content != original_content:
            file_path.write_text(content, encoding="utf-8")
            fixes = original_content.count("\n") - content.count("\n") + 1
            # More accurate count
            fixes = len(re.findall(pattern, original_content, flags=re.MULTILINE))
            return True, fixes
        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False, 0


def main():
    """Find and fix all markdown files with closing fence issues."""
    claude_dir = Path.home() / ".claude"

    if not claude_dir.exists():
        print("Error: ~/.claude directory not found", file=sys.stderr)
        sys.exit(1)

    # Find all markdown files
    md_files = list(claude_dir.rglob("*.md"))

    total_files_modified = 0
    total_fixes = 0

    print(f"Scanning {len(md_files)} markdown files...")

    for md_file in md_files:
        was_modified, fix_count = fix_closing_fences(md_file)
        if was_modified:
            total_files_modified += 1
            total_fixes += fix_count
            print(f"✓ Fixed {fix_count} fences in {md_file.relative_to(claude_dir)}")

    print(f"\n✅ Complete: {total_fixes} closing fences fixed in {total_files_modified} files")

    if total_files_modified == 0:
        print("No files needed fixing!")


if __name__ == "__main__":
    main()
