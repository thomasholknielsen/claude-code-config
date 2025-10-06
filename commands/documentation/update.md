---
description: "Intelligently update existing project documentation by analyzing changes and keeping content current"
argument-hint: "[target] [--scope=<area>] [--validate-links]"
allowed-tools: Read, Edit, Bash, Grep
---

# Command: Update

## Purpose

Executes docs operations for update functionality.

## Usage

```bash
/docs:update $ARGUMENTS
```

**Arguments**:

- `$1` (target): Specific documentation to update (optional)
- `$2` (--scope): Area of documentation to update (optional)
- `$3` (--validate-links): Check and validate documentation links (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "README.md --validate-links"` - Update README with link validation
- `$ARGUMENTS = "--scope=api"` - Update only API documentation
- `$ARGUMENTS = "docs/user-guide.md --scope=installation"` - Update specific section

## Process

1. Analyze the current state and documentation changes needed based on $ARGUMENTS target
2. Update existing documentation files with current information
3. **README.md Synchronization**: Review and update README.md for consistency
4. Validate documentation links and cross-references
5. Ensure README links match actual documentation structure
6. Validate results and provide feedback

## Mermaid Diagram Updates

See [Mermaid Guidance Template](/templates/documentation/mermaid-guidance.md) for comprehensive diagram standards.

**When updating documentation, refresh Mermaid diagrams when**:

- Component relationships have changed
- New data flows introduced
- Process workflows modified
- System architecture evolved

**Best Practice**: Keep diagrams synchronized with code changes to prevent documentation drift

## Agent Integration

- **Specialist Agent**: documenter - Can be spawned to handle documentation updates and coordination

## Examples

```bash
# Example usage
/docs:update $ARGUMENTS
```

## Integration Points

Works with other commands:

- After `/implement` or `/scaffold` - Document new features
- After `/fix bug-quickly` - Update CHANGELOG and troubleshooting
- After `/refactor` - Update architecture and migration docs
- After `/test` - Update test documentation coverage
- After `/review security` - Update security documentation
