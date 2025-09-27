---
description: "Uses Claude plan mode with Opus to create comprehensive plans and save to .specify folder"
category: "plan"
agent: "task-orchestrator"
tools: ["ExitPlanMode", "Write", "Read", "Bash"]
complexity: "moderate"
---

# Command: Plan to Markdown

## Purpose
Leverages Claude's plan mode with Opus model to create detailed implementation plans and save them as markdown files in the .specify folder.

## Usage
```
/plan:to-markdown "task description"
```

**Arguments**: Description of the task or feature that needs planning

## Process
1. Enter Claude's plan mode to analyze the task requirements
2. Use Opus model's advanced reasoning to create comprehensive plan
3. Generate structured markdown plan with implementation steps
4. Save the plan file to .specify folder with timestamp
5. Exit plan mode and present the completed plan

## Agent Integration
- **Primary Agent**: task-orchestrator - Coordinates plan generation and file management
- **Secondary Agents**: None (uses plan mode directly)

## Examples
```bash
# Plan a new feature
/plan:to-markdown "Add user authentication with OAuth2"

# Plan refactoring work
/plan:to-markdown "Migrate from REST to GraphQL API"

# Plan infrastructure changes
/plan:to-markdown "Implement CI/CD pipeline with GitHub Actions"
```

## Output
- Comprehensive markdown plan saved to .specify/plan-{timestamp}.md
- Structured implementation steps with dependencies
- Resource requirements and timeline estimates
- Risk assessment and mitigation strategies

## Integration Points
- **Follows**: Initial task conception, requirements gathering
- **Followed by**: /spec-kit:tasks (for task breakdown), /spec-kit:implement
- **Related**: /spec-kit:plan, /spec-kit:analyze, /spec-kit:specify

## Quality Standards
- Plans include clear objectives and success criteria
- Implementation steps are sequenced with dependencies
- Resource and timeline estimates are realistic
- Risk factors are identified with mitigation strategies
- Plans are saved with proper formatting and timestamps