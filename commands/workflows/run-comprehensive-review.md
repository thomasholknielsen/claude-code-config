---
description: "Orchestrate comprehensive code, security, and design review using atomic slash commands"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand", "Read", "Write"]
complexity: "complex"
---

# Command: Run Comprehensive Review

## Purpose

Orchestrates comprehensive code, security, and design review by executing atomic review commands in sequence for thorough project analysis.

## Usage

```bash
/workflows:run-comprehensive-review [arguments]
```

**Arguments**: Optional parameters specific to the operation

## Process

1. **Code Quality Analysis**: Execute `/review:code` for comprehensive code quality assessment
2. **Security Assessment**: Execute `/review:security` for vulnerability analysis and security compliance
3. **Design Validation**: Execute `/review:design` for UI/UX compliance and accessibility standards
4. **Results Consolidation**: Synthesize findings from all review commands into unified report

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential execution of atomic review commands and consolidates findings

## Implementation Steps

**Sequential Command Execution:**

1. **Execute Code Review**:

   ```bash
   SlashCommand("/review:code")
   ```

2. **Execute Security Review**:

   ```bash
   SlashCommand("/review:security")
   ```

3. **Execute Design Review**:

   ```bash
   SlashCommand("/review:design")
   ```

4. **Consolidate Results**: Analyze outputs from all three review commands and create comprehensive summary

## Examples

```bash
# Run comprehensive review workflow
/workflows:run-comprehensive-review

# Example execution sequence:
# 1. SlashCommand("/review:code") - Analyzes code quality, architecture, patterns
# 2. SlashCommand("/review:security") - Checks for vulnerabilities, OWASP compliance
# 3. SlashCommand("/review:design") - Validates UI/UX, accessibility, design system
# 4. Consolidate all findings into unified review report
```

## Integration Points

- **Input**: Project codebase and configuration files
- **Dependencies**: `/review:code`, `/review:security`, `/review:design` commands
- **Output**: Comprehensive review report with prioritized findings
- **Follow-up**: Use with `/to-do:create` to capture action items from review findings
