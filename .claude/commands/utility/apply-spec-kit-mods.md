---
description: "Apply cross-repository path modifications to spec-kit commands"
category: "utility"
complexity: "simple"
---

# Command: Apply Spec-Kit Modifications

## Purpose

Reapply cross-repository path modifications to spec-kit commands if they are overwritten or updated from upstream.

## Usage

/utility:apply-spec-kit-mods [--verify-only]

## Arguments

- `--verify-only`: Check if modifications are present without applying changes (optional)

## Process

1. Read all 6 spec-kit command files (specify, plan, tasks, clarify, analyze, implement)
2. For each file, check current path references
3. Apply modifications:
   - Replace `.specify/scripts/bash/` with `~/.claude/.specify/scripts/bash/`
   - Replace `.specify/templates/` with `~/.claude/.specify/templates/`
   - Leave `.specify/memory/` unchanged (project-specific constitution)
4. If `--verify-only` flag is set: Report status without making changes
5. Otherwise: Apply modifications and report results
6. Display summary of files checked and modified

## Modification Pattern

**User-scoped paths (shared across all projects):**

- Scripts: `~/.claude/.specify/scripts/bash/*`
- Templates: `~/.claude/.specify/templates/*`

**Project-scoped paths (remain in project repository):**

- Constitution: `.specify/memory/constitution.md`
- Specification files: `.specify/spec.md`, `plan.md`, `tasks.md`, etc.
- Contracts and other project artifacts: `.specify/contracts/*`, etc.

## Rationale

This modification pattern enables spec-kit commands to work in any repository context:

- User-scoped Claude config stores shared development tools
- Project repositories contain project-specific specifications and requirements
- Each project can have its own constitution and feature requirements

## Agent Integration

- **Primary Agent**: code-writer - Handles file reading and path replacement operations

## Examples

**Verify current modification status:**

```
/utility:apply-spec-kit-mods --verify-only
```

**Apply modifications to spec-kit commands:**

```
/utility:apply-spec-kit-mods
```

## Output

- Summary: Number of files checked
- Status: Modified / Already correct / Skipped
- Details: Specific path replacements made in each file
- Result: Success or error messages

## When to Use

Run this command when:

- Spec-kit commands have been overwritten
- Updating from upstream source
- Verifying modification status after changes
- Setting up a fresh clone of the command system

## Integration Points

- Works with all `/spec-kit:*` commands
- Ensures cross-repository compatibility
- Maintains separation between shared tools and project files
