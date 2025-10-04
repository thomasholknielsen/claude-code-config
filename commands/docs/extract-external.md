---
description: "Fetch and integrate up-to-date documentation from external sources using Context7 MCP"
argument-hint: "[libraries] [--output=<location>] [--format=<type>] [--update-existing]"
category: "docs"
tools: ["mcp__context7__resolve-library-id", "mcp__context7__get-library-docs", "Write", "Read"]
complexity: "moderate"
allowed-tools: mcp__context7__resolve-library-id, mcp__context7__get-library-docs, Write, Read
---

# Command: Extract External

## Purpose

Fetches and integrates up-to-date documentation from external sources using Context7 MCP to ensure current best practices and API references.

## Usage

```bash
/docs:extract-external $ARGUMENTS
```

**Arguments**:

- `$1` (libraries): Specific libraries to fetch docs for (comma-separated) (optional)
- `$2` (--output): Target documentation directory (default: docs/external/) (optional)
- `$3` (--format): Output format (markdown, html, json) (optional)
- `$4` (--update-existing): Update existing external docs (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "react,typescript --format=markdown"` - Extract React and TypeScript docs
- `$ARGUMENTS = "--output=docs/libs --update-existing"` - Update existing library docs
- `$ARGUMENTS = "jest,cypress --format=json"` - Extract test framework docs as JSON

## Process

1. **Parallel Library Detection**: Use Task() to identify external dependencies and documentation needs:

   ```python
   Task("scan-dependencies", "Analyze package.json, requirements.txt, etc. for external libraries"),
   Task("identify-frameworks", "Detect frameworks and major libraries in use"),
   Task("check-versions", "Verify current versions against available documentation")
   ```

2. **Context7 Integration**: Leverage MCP tools for current documentation based on $ARGUMENTS libraries:
   - Use `mcp__context7__resolve-library-id` to map package names to documentation IDs
   - Use `mcp__context7__get-library-docs` to fetch current documentation content
   - Handle multiple library documentation requests in parallel
   - Manage API rate limits and request optimization

3. **Documentation Processing**: Transform external docs for local integration:
   - Convert external formats to project documentation standards
   - Extract relevant sections (API references, best practices, examples)
   - Maintain attribution and version information
   - Create cross-references to project-specific usage

4. **Integration**: Incorporate external docs into project documentation:
   - Organize documentation by library and version
   - Create index files for easy navigation
   - Link external docs to relevant project code
   - Update table of contents and documentation maps

5. **Validation**: Ensure documentation quality and currency:
   - Verify external links and references
   - Check for documentation version consistency
   - Validate formatting and structure
   - Test example code snippets where applicable

## Agent Integration

- **Specialist Agent**: documenter - Can be spawned to handle external documentation integration with Context7 MCP for current best practices

## Parallelization Patterns

**Multi-Library Processing**: Simultaneously fetch documentation for multiple libraries to reduce total processing time.

**Parallel Integration**: Process documentation transformation and integration tasks concurrently for different libraries.

## Examples

```bash
# Extract docs for all project dependencies
/docs:extract-external

# Fetch specific library documentation
/docs:extract-external $ARGUMENTS
# where $ARGUMENTS = "react,typescript,jest"

# Update existing external documentation
/docs:extract-external $ARGUMENTS
# where $ARGUMENTS = "--update-existing"
