---
description: "Execute comprehensive project overhaul by orchestrating all workflows in intelligent sequence for maximum improvement"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/workflows:*)
---

# Command: Run Complete Overhaul

## Purpose

Execute comprehensive project overhaul by orchestrating all available workflow commands in intelligent sequence for maximum improvement and quality assurance.

## Usage

```bash
/workflows:run-complete-overhaul
```

## Process

1. **Security Foundation**: Execute security audit to identify and fix vulnerabilities first
   - Use SlashCommand to run `/workflows:run-security-audit`

2. **Code Quality Review**: Perform comprehensive review of code, security, and design
   - Use SlashCommand to run `/workflows:run-comprehensive-review`

3. **Optimization Phase**: Apply performance and efficiency improvements
   - Use SlashCommand to run `/workflows:run-optimization`

4. **Refactoring Phase**: Apply systematic code improvements and restructuring
   - Use SlashCommand to run `/workflows:run-refactor-workflow`

5. **Cleanup Phase**: Clean development artifacts and improve code readability
   - Use SlashCommand to run `/workflows:run-cleanup-workflow`

6. **Documentation Phase**: Update and generate comprehensive documentation
   - Use SlashCommand to run `/workflows:run-docs-workflow`

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates execution of multiple workflow commands in optimal sequence

## Examples

```bash
# Execute complete project overhaul
/workflows:run-complete-overhaul

# This will automatically execute the following sequence:
# 1. /workflows:run-security-audit
# 2. /workflows:run-comprehensive-review
# 3. /workflows:run-optimization
# 4. /workflows:run-refactor-workflow
# 5. /workflows:run-cleanup-workflow
# 6. /workflows:run-docs-workflow
```

## Integration Points

This command orchestrates the following workflow commands:

- **Security First**: `/workflows:run-security-audit` - Establishes secure foundation
- **Quality Assessment**: `/workflows:run-comprehensive-review` - Identifies improvement areas
- **Performance**: `/workflows:run-optimization` - Enhances system performance
- **Code Structure**: `/workflows:run-refactor-workflow` - Improves code organization
- **Cleanliness**: `/workflows:run-cleanup-workflow` - Removes development artifacts
- **Knowledge**: `/workflows:run-docs-workflow` - Ensures comprehensive documentation

Each workflow command is executed in sequence, with each phase building upon the previous improvements for maximum project enhancement.
