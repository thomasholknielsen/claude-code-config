---
description: "Enhance user prompts with knowledge of available commands and agents"
argument-hint: "\"user prompt text\""
category: "prompt"
tools: ["Read", "Grep", "Glob", "TodoWrite"]
complexity: "moderate"
---

# Command: Enhanced

## Purpose

Analyzes user prompts and enhances them by leveraging knowledge of available slash commands and subagents.

## Usage

```bash
/prompt:enhanced $ARGUMENTS
```

**Arguments**:

- `$1` (user-prompt): Raw user prompt or task description to enhance (required)
- `$2` (--complexity): Expected complexity level for enhancement (simple, moderate, complex) (optional)
- `$3` (--focus): Focus area for enhancement (commands, agents, parallelization) (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "My login form isn't working"` - Basic bug report enhancement
- `$ARGUMENTS = "Make my code better --complexity=complex"` - Complex code improvement enhancement
- `$ARGUMENTS = "Add user authentication --focus=parallelization"` - Feature with parallelization focus

## Process

1. Extract and parse user prompt from $ARGUMENTS
2. Parse user intent from the provided prompt
3. Map intent to available slash commands (54 total commands)
4. Identify optimal agent assignments from Agent Orchestra (8 agents)
5. Design execution strategy (main thread parallelization vs sequential)
6. Recommend Task tool usage for parallel research opportunities
7. Generate enhanced prompt with specific parallelization-aware recommendations

## Agent Integration

- **Specialist Options**: task-analysis-specialist can be spawned to analyze complexity and coordinate enhancement strategy
- **Analysis Tools**: Read, Grep, Glob for discovering available commands and agents

## Examples

### Example 1: Basic Bug Fix

```bash
/prompt:enhanced $ARGUMENTS
# where $ARGUMENTS = "My login form isn't working"
```

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
/prompt:enhanced $ARGUMENTS
# where $ARGUMENTS = "Make my code better"
```

**Enhanced Output:**

```markdown
I'll help improve your code quality comprehensively. Here's a parallelization-optimized approach:

1. **Parallel Research Phase**: Use main thread Task tool to spawn multiple analysis tasks:
   Task("Analyze code quality and design patterns across codebase")
   Task("Perform security vulnerability assessment")
   Task("Evaluate performance bottlenecks and optimization opportunities")
   Task("Review test coverage and identify testing gaps")

2. **Sequential Implementation Phase**: Based on parallel research findings:
   - `/refactor:simplify-logic` for complex code
   - `/clean:improve-readability` for formatting
   - `/refactor:remove-duplication` for DRY principles

**Recommended Execution:**
- Research: Main thread parallelization (4 concurrent tasks)
- Coordination: task-analysis-specialist provides strategic recommendations
- Implementation: Sequential refactoring based on consolidated findings
- Pattern: Parallel research → Sequential improvements

**Enhanced Prompt:**
"Execute comprehensive code quality improvement using main thread parallelization for research, then apply targeted refactoring sequentially based on consolidated findings."
```

### Example 3: Feature Implementation

```bash
/prompt:enhanced $ARGUMENTS
# where $ARGUMENTS = "Add user authentication to my app"
```

**Enhanced Output:**

```markdown
I'll help implement user authentication systematically. Here's a parallelization-optimized approach:

1. **Parallel Research Phase**: Use main thread Task tool for comprehensive analysis:
   Task("Research authentication best practices and security requirements")
   Task("Analyze existing codebase architecture and integration points")
   Task("Investigate performance implications of authentication systems")
   Task("Explore testing strategies for authentication flows")

2. **Planning Phase**: Based on research findings:
   - `/spec-kit:specify` to define authentication requirements
   - `/spec-kit:plan` to create implementation strategy

3. **Sequential Implementation Phase**:
   - `/implement:spec-kit-tasks` for structured development
   - Implementation-strategy-specialist provides dependency coordination

4. **Parallel Quality Assurance**:
   Task("Perform comprehensive security review of authentication")
   Task("Execute testing and validation of auth flows")
   Task("Generate API documentation and user guides")

**Recommended Execution:**
- Research: Main thread parallelization (4 concurrent tasks)
- Planning: Sequential spec-kit workflow
- Implementation: Sequential with dependency coordination
- Quality: Main thread parallelization (3 concurrent tasks)
- Pattern: Parallel research → Sequential planning → Sequential implementation → Parallel QA

**Enhanced Prompt:**
"Implement user authentication using main thread parallelization for research and quality phases, with sequential implementation coordinated by implementation-strategy-specialist."
```

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
- Leverages full Agent Specialist Framework capabilities correctly (analysis specialists provide strategic guidance)
- Optimizes for main thread parallelization using Task tool when appropriate
- Recommends parallel research phases followed by sequential implementation
- Includes progress tracking via TodoWrite
- Maps user intent to available system capabilities with parallelization awareness
- Distinguishes between parallel research opportunities and sequential implementation requirements

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
- Primary Agent: task-analysis-specialist (coordinates multiple improvements)
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
- Primary Agent: implementation-strategy-specialist (coordinates full feature)
- Pattern: Sequential phases with parallel sub-tasks
- TodoWrite: Track planning → implementation → documentation

**Enhanced Prompt:**
"Implement user authentication using the spec-kit workflow for systematic feature development, ensuring security review and comprehensive documentation."
```
