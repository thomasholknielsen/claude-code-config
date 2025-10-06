---
<<<<<<<< HEAD:.claude/commands/utility/save-artifact-to-markdown.md
description: "Captures Claude conversation artifacts (plans, reviews, research) and saves them to organized folders in .artifacts/"
========
description: "Captures Claude conversation artifacts (plans, reviews, research) and saves them to organized folders in .agent/artifacts/"
>>>>>>>> a263f4d (refactor: consolidate agents to domain analysts for context preservation (#17)):commands/system/save-artifact-to-markdown.md
argument-hint: "[type] [--title=\"Custom Title\"]"
allowed-tools: Write, Read, Bash
---

# Command: Save Artifact

## Purpose

Captures various types of Claude outputs (plans, reviews, research, analysis, specifications, documentation,
reports) and saves them as organized markdown files in the `.agent/artifacts/` directory with logical folder
structure.

## Usage

```bash
/artifact:save [type] [--title="Custom Title"]
```

## Arguments

- `type` (optional): Artifact type to save
  - `plan` - Planning outputs from plan mode
  - `review` - Code, security, or design review outputs
  - `research` - Research and investigation outputs
  - `analysis` - System analysis and diagnostic outputs
  - `spec` - Feature specifications and requirements
  - `docs` - Generated documentation and guides
  - `report` - Status reports and summaries
  - Auto-detected from conversation context if not specified

- `--title="Custom Title"` (optional): Custom title for filename
  - Auto-generated from content if not specified
  - Converted to kebab-case for filename

## Process

1. **Determine artifact type:**
   - Use explicitly provided `type` argument, OR
   - Auto-detect from conversation context using keywords:
     - "plan mode", "planning" → `plan`
     - "review", "code review", "security review" → `review`
     - "research", "investigation", "analyze options" → `research`
     - "analyze", "analysis", "diagnostic" → `analysis`
     - "specification", "requirements", "spec" → `spec`
     - "documentation", "guide", "readme" → `docs`
     - "report", "summary", "status" → `report`
   - Default to `report` if type cannot be determined

2. **Extract content:**
   - Capture relevant Claude output from current conversation
   - For plan mode: Extract plan content
   - For reviews: Extract review findings and recommendations
   - For research: Extract research findings and conclusions
   - Preserve formatting, code blocks, and structure

3. **Generate filename:**
   - If `--title` provided: Use custom title
   - Otherwise: Extract meaningful title from content (first heading or summary)
   - Format: `{type}-{YYYY-MM-DD}-{title-slug}.md`
   - Example: `plan-2025-09-30-authentication-feature.md`

4. **Create directory structure:**
   - Detect project root directory
   - Create `.agent/artifacts/{type}/` if it doesn't exist
   - Folder structure:

     ```text
     .agent/artifacts/
     ├── plans/           # Planning outputs
     ├── reviews/         # Code/security/design reviews
     ├── research/        # Research and analysis
     ├── analysis/        # System diagnostics
     ├── specifications/  # Feature specs
     ├── documentation/   # Generated docs
     └── reports/         # Status reports
     ```

5. **Add metadata headers:**

   ```markdown
   ---
   artifact_type: {type}
   created: {YYYY-MM-DD HH:MM:SS}
   project: {auto-detected project name}
   status: draft
   ---
   ```

6. **Save file:**
   - Write to `.agent/artifacts/{type}/{filename}.md`
   - Report saved location to user
   - Confirm successful save with full path

## Agent Integration

- **Primary Agent**: documenter - Handles artifact capture and organization
- **Tools**: Bash for directory operations, Write for file creation, Read for context analysis

## Examples

### Example 1: Save plan with auto-detection

```bash
# After creating a plan in plan mode (Shift+Tab twice)
/artifact:save

# Output: Saved to .agent/artifacts/plans/plan-2025-09-30-user-authentication.md
```

### Example 2: Save review with explicit type

```bash
# After performing a security review
/artifact:save review

# Output: Saved to .agent/artifacts/reviews/review-2025-09-30-security-audit.md
```

### Example 3: Save research with custom title

```bash
# After researching database options
/artifact:save research --title="Database Comparison Study"

# Output: Saved to .agent/artifacts/research/research-2025-09-30-database-comparison-study.md
```

### Example 4: Save specification

```bash
# After creating feature specification
/artifact:save spec --title="Payment Integration Spec"

# Output: Saved to .agent/artifacts/specifications/spec-2025-09-30-payment-integration-spec.md
```

## Output

- Confirmation message with full path to saved artifact
- Artifact saved with:
  - Metadata headers (type, created date, project, status)
  - Original content with preserved formatting
  - Organized in type-specific folder
  - Meaningful, searchable filename

## Integration Points

- **Follows**: Any Claude conversation producing valuable artifacts (plans, reviews, research, etc.)
- **Followed by**: Review saved artifacts, share with team, reference in documentation
- **Related**: `/docs:generate`, `/review:code`, `/analyze:potential-issues`, `/spec-kit:specify`

## Quality Standards

- Preserves original content structure and formatting
- Adds consistent metadata without disrupting readability
- Creates project-specific storage in `.agent/artifacts/`
- Generates meaningful, searchable, dated filenames
- Maintains artifact organization through logical folder structure
- Auto-detection accuracy for common artifact types
- Supports manual override for edge cases

## Artifact Organization

The `.agent/artifacts/` folder provides a centralized location for all Claude-generated artifacts:

**Plans** (`plans/`) - Strategic planning outputs, feature plans, implementation strategies
**Reviews** (`reviews/`) - Code quality reviews, security audits, design critiques
**Research** (`research/`) - Technology investigations, option comparisons, feasibility studies
**Analysis** (`analysis/`) - System diagnostics, performance analysis, dependency audits
**Specifications** (`specifications/`) - Feature specs, requirements documents, API contracts
**Documentation** (`documentation/`) - Generated guides, README files, API documentation
**Reports** (`reports/`) - Status reports, progress summaries, general artifacts

## Migration Note

This command replaces the previous `/plan:save-plan-to-markdown` command with broader functionality. Existing
plans saved in `.claude/.plans/` remain accessible and are not affected by this change.
