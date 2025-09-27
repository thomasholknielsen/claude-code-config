---
description: "Comprehensive documentation workflow that analyzes, generates, updates, and validates all project documentation"
category: "workflow"
agent: "task-orchestrator"
tools: ["TodoWrite", "Task", "Bash"]
complexity: "complex"
---

# Command: Run Docs Workflow

## Purpose

Executes workflows operations for run docs workflow functionality.

## Usage

```bash
/workflows:run-docs-workflow [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Analyze the current state and requirements
2. Execute the workflows operation
3. Validate results and provide feedback
4. Update relevant documentation or state

## Agent Integration

- **Primary Agent**: task-orchestrator - Handles workflows operations and coordination

## Examples

```bash

## Integration Points
### **Development Workflow Integration**
- Run after major feature implementation
- Include in pre-commit hooks for documentation updates
- Integrate with CI/CD for automated doc validation
- Schedule regular documentation health checks

### **Quality Assurance & Architecture Compliance**
- Validate all generated/updated documentation
- Ensure GitHub-friendly structure: concise README.md + comprehensive docs/
- Check README links to docs/ sections work correctly
- Verify mobile-friendly GitHub rendering
- Ensure examples work and code samples are accurate
- Maintain consistent style and formatting across README and docs/

### **Team Collaboration**
- Generate onboarding documentation for new team members
- Create handoff documentation for project transfers
- Maintain consistent documentation standards across team
- Support multiple documentation formats and audiences

## Additional Information
- Run after major feature implementation
- Include in pre-commit hooks for documentation updates
- Integrate with CI/CD for automated doc validation
- Schedule regular documentation health checks


- Validate all generated/updated documentation
- Ensure GitHub-friendly structure: concise README.md + comprehensive docs/
- Check README links to docs/ sections work correctly
- Verify mobile-friendly GitHub rendering
- Ensure examples work and code samples are accurate
- Maintain consistent style and formatting across README and docs/


- Generate onboarding documentation for new team members
- Create handoff documentation for project transfers
- Maintain consistent documentation standards across team
- Support multiple documentation formats and audiences
