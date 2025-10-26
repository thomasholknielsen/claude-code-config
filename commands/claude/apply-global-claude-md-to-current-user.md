---
description: "Sync CLAUDE-GLOBAL.md template to user CLAUDE.md with intelligent conflict detection and swift resolution"
argument-hint: "[--show-diff]"
allowed-tools: Read, Write, Edit, Bash(python:*)
---

# Command: Apply Config to User CLAUDE.md

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Safely merge CLAUDE-GLOBAL.md template into user's global CLAUDE.md with intelligent conflict detection.

**Claude Code MUST execute this workflow:**
1. ✓ Validate CLAUDE-GLOBAL.md and user CLAUDE.md both exist
2. ✓ Create backup with timestamp before any modifications
3. ✓ Parse and compare sections from both files
4. ✓ Present batch decision options (Apply All, Interactive, Keep Current)
5. ✓ Apply selected changes based on user choice
6. ✓ Verify result is valid Markdown
7. ✓ Display before/after metrics

**Claude Code MUST NOT:**
- ✗ Skip backup creation
- ✗ Modify files without user confirmation
- ✗ Leave the user file in invalid state

---

## Purpose

Safely merge CLAUDE-GLOBAL.md (repository template) into user's global CLAUDE.md with intelligent conflict detection and streamlined resolution using batch decisions.

**Cross-Platform Support**: Works on macOS, Linux, and Windows using `pathlib.Path` for OS-agnostic file operations.

- **macOS/Linux**: `~/CLAUDE.md` → `/Users/{username}/CLAUDE.md` or `/home/{username}/CLAUDE.md`
- **Windows**: `~/CLAUDE.md` → `C:\Users\{username}\CLAUDE.md` (via `Path.home()`)

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| **A** | Default workflow | **← Recommended** |
| **B** | Alternative approach | For different use case |
| **C** | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output/results | Check generated content |
| 2 | Iterate or refine | Run command again with adjustments ← Recommended |
| 3 | Continue workflow | Proceed to next step in your workflow |
| 4 | Get help | Use `/claude:guru` for guidance |

What would you like to do next?


## Usage

```
/claude:apply-config-to-user-claude-md [--show-diff]
```

**Arguments**:

- `--show-diff` (optional): Show detailed diff of changes before applying

**Examples**:

- `/claude:apply-config-to-user-claude-md` - Standard sync with batch decision
- `/claude:apply-config-to-user-claude-md --show-diff` - Show changes before prompting

## Process

1. **Validation**
   - Verify CLAUDE-GLOBAL.md exists in repository (`.claude/CLAUDE-GLOBAL.md`)
   - Verify user CLAUDE.md exists using `Path.home() / "CLAUDE.md"` (or offer to create from template)
   - Create backup: `{user_home}/CLAUDE.md.backup-{timestamp}` (OS-agnostic path handling)

2. **Parse and Analyze**
   - Parse both files into sections by `##` headers
   - Compare sections to categorize changes:
     - **NEW**: Section exists in template, not in user file
     - **UPDATED**: Section exists in both but content differs
     - **UNCHANGED**: Section exists in both with identical content
     - **USER_ONLY**: Section exists in user file, not in template
   - Count changes in each category

3. **Present Batch Decision** (Streamlined A/B/C Choice)
   - Show summary: X new sections, Y updated sections, Z user-only sections
   - Present ONE consolidated decision table:

   ```markdown
   ## CLAUDE.md Sync Analysis

   Template updates available:
   - {count} new sections to add
   - {count} sections with updates
   - {count} user-only sections (will be preserved)

   | Option | Description | What Happens |
   |--------|-------------|--------------|
   | A | Apply all template changes | Accept all new + updated sections, preserve user-only |
   | B | Interactive review | Auto-add new sections, choose for each updated section |
   | C | Keep current file | No changes applied, exit safely |

   Your choice: _
   ```

   - Validate input (A/B/C, case-insensitive)
   - Invalid input: re-prompt once, default to C

4. **Apply Changes Based on Selection**

   **Option A (Apply All)**:
   - Merge all NEW sections into user file
   - Replace all UPDATED sections with template versions
   - Preserve all USER_ONLY sections
   - Show summary: "Applied X new sections, updated Y sections, preserved Z custom sections"

   **Option B (Interactive)**:
   - Auto-add all NEW sections (show progress: "Adding 5 new sections...")
   - For each UPDATED section, show A/B choice:

   ```markdown
   ## Section: {section_name}

   | Option | Description |
   |--------|-------------|
   | A | Use template version |
   | B | Keep your version |

   Your choice: _
   ```

   - Preserve all USER_ONLY sections
   - Show summary after each decision

   **Option C (Keep Current)**:
   - Exit without changes
   - Backup file remains for reference

5. **Validation and Completion**
   - Verify user CLAUDE.md is valid after merge (Markdown syntax check)
   - Show before/after metrics (section counts, character counts)
   - Display backup location with OS-appropriate path format
   - Remind: "Restart Claude Code to load new configuration"

## Interactive Selection Format

Uses standard A/B/C table format for batch decision and optional per-section choices:

**Batch Decision (Always Shown)**:

- `A` - Apply all template changes (fastest)
- `B` - Interactive review of conflicts (more control)
- `C` - Keep current file unchanged (safest)

**Per-Section Choice (Only in Option B)**:

- `A` - Use template version
- `B` - Keep your current version

**Validation**:

- Case-insensitive (a, A, b, B, c, C all work)
- Invalid input re-prompts once, then defaults to safest option (C for batch, B for sections)
- Ctrl+C to exit at any time

## Merge Algorithm

**Cross-Platform Path Handling**:

```python
from pathlib import Path
import datetime

# OS-agnostic paths (works on Windows, macOS, Linux)
user_home = Path.home()
user_claude = user_home / "CLAUDE.md"
claude_global = Path.cwd() / ".claude" / "CLAUDE-GLOBAL.md"

# Create backup with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = user_home / f"CLAUDE.md.backup-{timestamp}"
```

**Section Parsing**:

```python
# Parse file into sections by ## headers
sections = {}
current_section = None
current_content = []

for line in file_lines:
    if line.startswith('## '):
        if current_section:
            sections[current_section] = ''.join(current_content)
        current_section = line[3:].strip()
        current_content = [line]
    else:
        current_content.append(line)
```

**Change Categorization**:

```python
template_sections = parse_sections(CLAUDE_GLOBAL)
user_sections = parse_sections(USER_CLAUDE)

NEW = set(template_sections.keys()) - set(user_sections.keys())
USER_ONLY = set(user_sections.keys()) - set(template_sections.keys())
COMMON = set(template_sections.keys()) & set(user_sections.keys())

UPDATED = {s for s in COMMON if template_sections[s] != user_sections[s]}
UNCHANGED = {s for s in COMMON if template_sections[s] == user_sections[s]}
```

**Merge Strategy (Option A)**:

```python
merged_sections = {}

# Add all sections from template (NEW + UPDATED)
for section in template_sections:
    merged_sections[section] = template_sections[section]

# Preserve user-only sections
for section in USER_ONLY:
    merged_sections[section] = user_sections[section]

# Write merged content maintaining original order (pathlib handles OS differences)
user_claude.write_text('\n'.join(merged_sections.values()), encoding='utf-8')
```

## Agent Integration

- **Optional Agent**: docs-analyst can be invoked if merge reveals quality issues
- **Coordination**: Command handles all merge logic directly (no agent needed for standard sync)
- **Post-Merge**: User can run `/system:claude-review` to validate merged file quality

**Coordination Pattern**:

- Command has full main thread access (unrestricted)
- Direct file operations (no agent spawning needed)
- Focused on efficiency and speed

## Examples

### Example 1: Standard Sync with Batch Decision

```
/claude:apply-config-to-user-claude-md

# Expected behavior:
→ Reading CLAUDE-GLOBAL.md from repository...
→ Reading ~/CLAUDE.md...
→ Creating backup: ~/CLAUDE.md.backup-20250114-152033

## CLAUDE.md Sync Analysis

Template updates available:
- 3 new sections to add:
  • Parallelization
  • Review & Quality Assurance
  • CLAUDE.md Disambiguation Protocol

- 2 sections with updates:
  • Tool & File Operations (added Glob examples)
  • Communication Protocols (added Interactive User Input)

- 1 user-only section (will be preserved):
  • My Custom Workflows

| Option | Description | What Happens |
|--------|-------------|--------------|
| A | Apply all template changes | Accept all 3 new + 2 updated sections, preserve custom section |
| B | Interactive review | Auto-add 3 new sections, choose for 2 updated sections |
| C | Keep current file | No changes applied, exit safely |

Your choice: _

→ User enters: A
→ Validated: Applying all template changes

## Applying Changes

✓ Added section: Parallelization
✓ Added section: Review & Quality Assurance
✓ Added section: CLAUDE.md Disambiguation Protocol
✓ Updated section: Tool & File Operations
✓ Updated section: Communication Protocols
✓ Preserved section: My Custom Workflows

## Results

✅ Sync completed successfully
📊 Before: 8 sections, 3,421 characters
📊 After: 11 sections, 4,687 characters
💾 Backup: ~/CLAUDE.md.backup-20250114-152033

⚠️  Restart Claude Code to load new configuration
```

### Example 2: Interactive Review of Conflicts

```
/claude:apply-config-to-user-claude-md

→ User selects: B (Interactive review)

## Adding New Sections

✓ Added: Parallelization
✓ Added: Review & Quality Assurance
✓ Added: CLAUDE.md Disambiguation Protocol

## Reviewing Updated Sections (2 conflicts)

### Section 1 of 2: Tool & File Operations

Template adds Glob pattern examples and cross-references.
Your version has custom tool preferences.

| Option | Description |
|--------|-------------|
| A | Use template version (with new examples) |
| B | Keep your version (with custom preferences) |

Your choice: _

→ User enters: A
✓ Updated: Tool & File Operations

### Section 2 of 2: Communication Protocols

Template adds Interactive User Input subsection.
Your version has custom response style.

| Option | Description |
|--------|-------------|
| A | Use template version (with interactive pattern) |
| B | Keep your version (with custom style) |

Your choice: _

→ User enters: A
✓ Updated: Communication Protocols

## Results

✅ Sync completed successfully
📊 Applied: 3 new sections + 2 updated sections
💾 Backup: ~/CLAUDE.md.backup-20250114-152109

⚠️  Restart Claude Code to load new configuration
```

### Example 3: Show Diff Before Decision

```
/claude:apply-config-to-user-claude-md --show-diff

→ Analyzing changes...

## Detailed Changes

**NEW SECTIONS (3)**:

+++ Parallelization
[Shows first 3 lines of new content...]

+++ Review & Quality Assurance
[Shows first 3 lines of new content...]

+++ CLAUDE.md Disambiguation Protocol
[Shows first 3 lines of new content...]

**UPDATED SECTIONS (2)**:

~~~ Tool & File Operations
- Old: "Use Glob for file patterns, Grep for content"
+ New: "Use Glob for file patterns (`**/*.ts`, `src/**/*.js`), Grep for content (with regex)"
[Shows 5 lines of context...]

~~~ Communication Protocols
+ Added: Interactive User Input (Standard Pattern) subsection
[Shows new content...]

**PRESERVED (1)**:

=== My Custom Workflows (user-only, will be preserved)

## How would you like to proceed?

| Option | Description | What Happens |
|--------|-------------|--------------|
| A | Apply all template changes | Accept all 3 new + 2 updated sections |
| B | Interactive review | Choose for each updated section |
| C | Keep current file | No changes applied |

Your choice: _
```

## Safety Features

**Automatic Backups**:

- Before ANY changes: `{user_home}/CLAUDE.md.backup-{timestamp}`
- macOS/Linux example: `/Users/username/CLAUDE.md.backup-20250114-152033`
- Windows example: `C:\Users\username\CLAUDE.md.backup-20250114-152033`

**Cross-Platform Manual Restore**:

```python
# Python (works on all platforms)
from pathlib import Path
import shutil

user_home = Path.home()
backup = user_home / "CLAUDE.md.backup-20250114-152033"
target = user_home / "CLAUDE.md"
shutil.copy2(backup, target)
```

Or using bash/python one-liner:

```bash
# macOS/Linux/Windows (via python)
python -c "from pathlib import Path; import shutil; shutil.copy2(Path.home() / 'CLAUDE.md.backup-20250114-152033', Path.home() / 'CLAUDE.md')"
```

**Error Handling**:

- If merge fails, automatically restores from backup using `shutil.copy2()`
- Shows clear error message with what failed
- Backup always preserved for manual recovery

**Validation**:

- After merge, verifies file is valid Markdown
- Checks for malformed sections or broken syntax
- Shows before/after metrics for transparency

**Progressive Application** (Option B only):

- Sections applied one at a time with progress indicator
- User can Ctrl+C to stop (partial changes kept, backup available)
- Clear summary after all decisions made

## Quality Standards

- **Swift Execution**: Batch decision minimizes user interaction (1-2 prompts vs 8+ per-section)
- **Safety First**: Always create backups, validate after merge, restore on errors
- **Smart Defaults**: Option A fastest, Option B for control, Option C safest
- **Clear Communication**: Show what will happen before applying, summarize what happened after
- **User Control**: Can choose interactive review if needed, but defaults to batch
- **Preservation**: Always preserves user-only sections, never loses custom content

## Integration Points

- **Follows**: Manual edits to CLAUDE-GLOBAL.md (repository template)
- **Followed by**: `/system:claude-review` (validate merged file quality)
- **Related**:
  - `/system:claude-review` - Review CLAUDE.md quality after merge
  - `/claude:guru` - Context-aware guidance using updated config

## Output

- **Backup Location**: OS-appropriate path displayed (e.g., `/Users/username/CLAUDE.md.backup-{timestamp}` or `C:\Users\username\CLAUDE.md.backup-{timestamp}`)
- **Change Summary**: Counts of new/updated/preserved sections with examples
- **Before/After Metrics**: Section counts, character counts for transparency
- **Reminder**: "Restart Claude Code to load new configuration"
- **Validation**: Clear success/failure status with error details if needed

## Cross-Platform Implementation Notes

**Path Handling**: All file operations use `pathlib.Path` for cross-platform compatibility:

- `Path.home()` resolves to user directory on all platforms
- `Path` object handles forward/backward slashes automatically
- `Path.cwd()` gets current working directory (OS-agnostic)
- `.write_text()` and `.read_text()` handle encoding consistently

**Backup/Restore**: Uses `shutil.copy2()` instead of shell commands (`cp`/`copy`) for cross-platform file operations

**Timestamps**: Uses `strftime("%Y%m%d-%H%M%S")` format which is filesystem-safe on all platforms (no colons)
