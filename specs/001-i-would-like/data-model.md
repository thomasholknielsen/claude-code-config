# Data Model: Slash Command Template System

**Feature**: 001-i-would-like
**Date**: 2025-10-03

## Overview

This feature manages structured documentation artifacts (markdown templates and command files) with standardized metadata.
No traditional database entities - all data is file-based.

## Entity 1: Command Template

**Purpose**: Defines the standardized structure for slash command documentation

**Attributes**:

- **template_type**: `base` | `workflow`
- **version**: Semantic version for template evolution tracking
- **required_sections**: List of mandatory section headings
- **frontmatter_schema**: YAML structure definition
- **example_content**: Sample command following template

**Validation Rules**:

- Must include all required sections from research.md Decision 3
- Frontmatter must define all 6 required fields
- Must include `allowed-tools` syntax examples
- Must document $ARGUMENTS parsing patterns

**File Locations**:

- Base template: `templates/command.md`
- Workflow template: `templates/command-workflow.md`

**Relationships**:

- **defines_structure_for** → Command File (1:N)
- **referenced_by** → CLAUDE.md Configuration (1:1)

## Entity 2: Command File

**Purpose**: Individual slash command documentation following template structure

**Attributes**:

- **category**: One of 15 defined categories (analyze, docs, git, etc.)
- **command_name**: Unique within category (e.g., "commit", "generate", "code")
- **frontmatter**: YAML metadata block
  - `description`: string
  - `argument-hint`: string
  - `category`: string
  - `tools`: array
  - `complexity`: enum[simple, moderate, complex]
  - `allowed-tools`: string (permission syntax)
- **content_sections**: Markdown headings and content
- **conformity_status**: `auto-conforming` | `simple-update` | `manual-review`

**Validation Rules**:

- Frontmatter must be valid YAML between `---` delimiters
- Category must match one of 15 existing categories
- allowed-tools must follow syntax: `Tool1, Tool2, Bash(command:*)`
- All required sections must be present (unless flagged manual-review)

**File Locations**:

- Path pattern: `commands/{category}/{command_name}.md`
- Total count: 54 existing commands

**Relationships**:

- **follows_structure** → Command Template (N:1)
- **categorized_by** → Command Category (N:1)

## Entity 3: CLAUDE.md Configuration

**Purpose**: Project-level AI assistant configuration directing template usage

**Attributes**:

- **template_reference**: Path to command templates
- **command_development_directive**: Instructions for creating/modifying commands
- **frontmatter_syntax_rules**: Allowed-tools pattern specification
- **template_variant_guidance**: When to use base vs workflow template

**Validation Rules**:

- Must reference both template files (base and workflow)
- Must specify required frontmatter fields
- Must include allowed-tools syntax examples
- Must distinguish atomic vs orchestration commands

**File Location**:

- `CLAUDE.md` (project root)

**Relationships**:

- **references** → Command Template (1:N)
- **guides_creation_of** → Command File (1:N)

## Entity 4: Command Category

**Purpose**: Organizational grouping for slash commands

**Attributes**:

- **category_name**: Directory name (analyze, clean, docs, explain, fix, git, implement, plan, prompt, refactor, review, spec-kit, to-do, workflows, utility)
- **command_count**: Number of commands in category
- **category_purpose**: High-level description

**Validation Rules**:

- Category directory must exist in `commands/`
- Category name must be lowercase, hyphenated

**File Locations**:

- Directory pattern: `commands/{category_name}/`

**Relationships**:

- **contains** → Command File (1:N)

## State Transitions

### Command File Lifecycle

```text
[New Command Request]
          ↓
    [Select Template]
     (base or workflow)
          ↓
   [Apply Template Structure]
          ↓
  [Fill Required Sections]
          ↓
  [Validate Frontmatter]
          ↓
    [Save Command File]
```

### Existing Command Migration

```text
[Existing Command]
         ↓
   [Analyze Structure]
         ↓
    /          |          \
   /           |           \
Auto-     Simple-Update   Manual-
Conforming               Review
   |            |            |
   |    [Add Missing        |
   |     Sections]          |
   |            |           |
[Validate] [Validate]  [Flag for Human]
   |            |            |
   └─────── [Complete] ──────┘
```

## Validation Rules Summary

**Template Validation**:

1. All required sections present
2. Frontmatter schema complete
3. allowed-tools syntax examples included
4. $ARGUMENTS documentation patterns shown

**Command File Validation**:

1. Valid YAML frontmatter
2. All 6 required frontmatter fields present
3. allowed-tools follows syntax pattern
4. Category matches existing directory
5. Content sections match template (unless manual-review)

**CLAUDE.md Validation**:

1. Both template paths referenced
2. Command development directive present
3. Syntax rules specified
4. Template variant guidance included

## Scale Considerations

- **54 existing commands** to review and migrate
- **15 categories** to validate
- **2 template files** to maintain
- **1 CLAUDE.md** configuration update

No performance concerns - all file-based operations, no runtime execution.

## Relationship Diagram

```text
CLAUDE.md Configuration
         │
         │ references
         ↓
Command Template ──────→ Command Template
  (base)                   (workflow)
    │                         │
    │ defines               │ defines
    │ structure              │ structure
    ↓                         ↓
Command File            Command File
(atomic: 47)           (workflow: 7)
    │                         │
    └─────────┬───────────────┘
              │
          categorized_by
              ↓
        Command Category
           (15 total)
```
