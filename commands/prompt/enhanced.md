---
description: "Enhance user prompts with knowledge of available commands and agents"
category: "prompt"
agent: "task-orchestrator"
tools: ["Read", "Grep", "Glob", "TodoWrite"]
complexity: "moderate"
---

# Command: Enhanced

## Purpose

Analyzes user prompts and enhances them by leveraging knowledge of available slash commands and subagents.

## Usage

```bash
/prompt:enhanced "user prompt text"
```python

**Arguments**: Raw user prompt or task description to enhance

## Process

1. Parse user intent from the provided prompt
2. Map intent to available slash commands (54 total commands)
3. Identify optimal agent assignments from Agent Orchestra (8 agents)
4. Design execution strategy (parallel vs sequential)
5. Generate enhanced prompt with specific recommendations

## Agent Integration

- **Primary Agent**: task-orchestrator - Analyzes complexity and coordinates enhancement strategy
- **Analysis Tools**: Read, Grep, Glob for discovering available commands and agents

## Examples

### Example 1: Basic Bug Fix

```bash
/prompt:enhanced "My login form isn't working"
```text

**Enhanced Output:**

```yaml
I'll help you fix the login form issue. Here's an optimized approach:

1. **Immediate Analysis**: `/analyze:potential-issues` to identify specific problems
2. **Quick Fix**: `/fix:bug-quickly "login form not working"` for obvious issues
3. **Verification**: Test the fix to ensure it resolves the issue

**Recommended Execution:**
- Primary Agent: bug-fixer (specialized for rapid diagnosis)
- Pattern: Sequential (analyze → fix → verify)
- TodoWrite: Track each step for progress visibility

**Enhanced Prompt:**
"Use the bug-fixer agent to analyze and resolve login form issues. Start with `/analyze:potential-issues` to identify the root cause, then apply `/fix:bug-quickly` for immediate resolution."
```text

### Example 2: Code Quality Improvement

```bash
/prompt:enhanced "Make my code better"
```text

**Enhanced Output:**

```yaml
I'll help improve your code quality comprehensively. Here's a structured approach:

1. **Comprehensive Review**: `/workflows:run-comprehensive-review` for parallel analysis
2. **Targeted Improvements**: Based on review findings:
   - `/refactor:simplify-logic` for complex code
   - `/clean:improve-readability` for formatting
   - `/refactor:remove-duplication` for DRY principles

**Recommended Execution:**
- Primary Agent: task-orchestrator (coordinates multiple improvements)
- Pattern: Parallel review → Sequential improvements
- TodoWrite: Track each improvement area

**Enhanced Prompt:**
"Execute a comprehensive code improvement workflow using parallel review agents, then apply targeted refactoring based on findings."
```text

### Example 3: Feature Implementation

```bash
/prompt:enhanced "Add user authentication to my app"
```text

**Enhanced Output:**

```yaml
I'll help implement user authentication systematically. Here's the recommended approach:

1. **Planning Phase**:
   - `/spec-kit:specify` to define authentication requirements
   - `/spec-kit:plan` to create implementation strategy
2. **Implementation Phase**:
   - `/implement:spec-kit-tasks` for structured development
   - `/review:security` for authentication security validation
3. **Documentation Phase**:
   - `/docs:api` for authentication endpoints
   - `/docs:update` for user guides

**Recommended Execution:**
- Primary Agent: implementation-orchestrator (coordinates full feature)
- Pattern: Sequential phases with parallel sub-tasks
- TodoWrite: Track planning → implementation → documentation

**Enhanced Prompt:**
"Implement user authentication using the spec-kit workflow for systematic feature development, ensuring security review and comprehensive documentation."
```yaml

## Output

- **Analysis Summary**: What the user wants to accomplish
- **Command Recommendations**: Specific slash commands to use
- **Agent Assignments**: Which agents should handle each task
- **Execution Strategy**: Parallel vs sequential execution plan
- **Enhanced Prompt**: Refined version with specific technical guidance
- **TodoWrite Structure**: Suggested task breakdown for tracking

## Integration Points

- **Follows**: User's initial request or unclear task description
- **Followed by**: Execution of recommended slash commands
- **Related**: `/explain:code`, `/analyze:potential-issues`, `/workflows:*`

## Quality Standards

- Provides actionable, specific command recommendations
- Leverages full Agent Orchestra capabilities
- Optimizes for parallel execution when possible
- Includes progress tracking via TodoWrite
- Maps user intent to available system capabilities

## Additional Information

Command: Enhance User Prompt

```bash
/prompt:enhanced "My login form isn't working"
```text

**Enhanced Output:**

```yaml
I'll help you fix the login form issue. Here's an optimized approach:

1. **Immediate Analysis**: `/analyze:potential-issues` to identify specific problems
2. **Quick Fix**: `/fix:bug-quickly "login form not working"` for obvious issues
3. **Verification**: Test the fix to ensure it resolves the issue

**Recommended Execution:**
- Primary Agent: bug-fixer (specialized for rapid diagnosis)
- Pattern: Sequential (analyze → fix → verify)
- TodoWrite: Track each step for progress visibility

**Enhanced Prompt:**
"Use the bug-fixer agent to analyze and resolve login form issues. Start with `/analyze:potential-issues` to identify the root cause, then apply `/fix:bug-quickly` for immediate resolution."
```text

```bash
/prompt:enhanced "Make my code better"
```text

**Enhanced Output:**

```yaml
I'll help improve your code quality comprehensively. Here's a structured approach:

1. **Comprehensive Review**: `/workflows:run-comprehensive-review` for parallel analysis
2. **Targeted Improvements**: Based on review findings:
   - `/refactor:simplify-logic` for complex code
   - `/clean:improve-readability` for formatting
   - `/refactor:remove-duplication` for DRY principles

**Recommended Execution:**
- Primary Agent: task-orchestrator (coordinates multiple improvements)
- Pattern: Parallel review → Sequential improvements
- TodoWrite: Track each improvement area

**Enhanced Prompt:**
"Execute a comprehensive code improvement workflow using parallel review agents, then apply targeted refactoring based on findings."
```text

```bash
/prompt:enhanced "Add user authentication to my app"
```text

**Enhanced Output:**

```yaml
I'll help implement user authentication systematically. Here's the recommended approach:

1. **Planning Phase**:
   - `/spec-kit:specify` to define authentication requirements
   - `/spec-kit:plan` to create implementation strategy
2. **Implementation Phase**:
   - `/implement:spec-kit-tasks` for structured development
   - `/review:security` for authentication security validation
3. **Documentation Phase**:
   - `/docs:api` for authentication endpoints
   - `/docs:update` for user guides

**Recommended Execution:**
- Primary Agent: implementation-orchestrator (coordinates full feature)
- Pattern: Sequential phases with parallel sub-tasks
- TodoWrite: Track planning → implementation → documentation

**Enhanced Prompt:**
"Implement user authentication using the spec-kit workflow for systematic feature development, ensuring security review and comprehensive documentation."
```
