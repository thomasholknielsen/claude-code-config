---
description: "Manage project CHANGELOG.md by analyzing changes and maintaining professional version history"
argument-hint: "[version] [--add-entry] [--release] [--format=<style>]"
allowed-tools: Bash, Read, Edit, Grep
---

# Command: Changelog

## Purpose

Executes docs operations for changelog functionality.

## Usage

```bash
/docs:changelog $ARGUMENTS
```

**Arguments**:

- `$1` (version): Version number for release (optional)
- `$2` (--add-entry): Add new changelog entry (optional)
- `$3` (--release): Mark version as released (optional)
- `$4` (--format): Changelog format style (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "v1.2.0 --release"` - Release version 1.2.0
- `$ARGUMENTS = "--add-entry"` - Add new unreleased entry
- `$ARGUMENTS = "--format=keepachangelog"` - Use specific format

## Process

1. Analyze the current state and requirements based on $ARGUMENTS
2. Execute the changelog operation with specified parameters
3. Generate or update CHANGELOG.md following version history standards
4. Validate results and provide feedback
5. Update relevant documentation or state

## Agent Integration

- **Specialist Agent**: documenter - Can be spawned to handle changelog management and version history maintenance

## Examples

```bash
# Example usage
/docs:changelog $ARGUMENTS
```

## Quality Standards

### Change Description Quality

Ensure entries are:

- **User-focused** - Written from user perspective
- **Action-oriented** - Clear about what changed
- **Specific** - Detailed enough to understand impact
- **Consistent** - Uniform tone and structure
- **Scannable** - Easy to skim for relevant changes

### Technical Accuracy

- **Verify changes** - Ensure accuracy against actual code
- **Check links** - Validate issue and PR references
- **Date accuracy** - Correct release dates
- **Version compliance** - Follow semantic versioning rules

## Additional Information

Ensure entries are:

- **User-focused** - Written from user perspective
- **Action-oriented** - Clear about what changed
- **Specific** - Detailed enough to understand impact
- **Consistent** - Uniform tone and structure
- **Scannable** - Easy to skim for relevant changes

- **Verify changes** - Ensure accuracy against actual code
- **Check links** - Validate issue and PR references
- **Date accuracy** - Correct release dates
- **Version compliance** - Follow semantic versioning rules
