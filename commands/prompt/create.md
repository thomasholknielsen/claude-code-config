---
description: "Enhance user prompts with knowledge of available commands and agents"
category: "prompt"
agent: "task-orchestrator"
tools: ["Read", "Grep", "Glob", "TodoWrite"]
complexity: "moderate"
---

# Command: Create Enhanced Prompt

## Purpose
Analyzes user prompts and enhances them by leveraging knowledge of available slash commands and subagents.

## Usage
```
/prompt:create "user prompt text"
```

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

## Enhancement Logic

### Intent Analysis
- **Development Tasks**: Maps to `/implement`, `/code-writer` agent
- **Bug Fixes**: Maps to `/fix:bug-quickly`, `/analyze:potential-issues`, `bug-fixer` agent
- **Code Quality**: Maps to `/review:code`, `/refactor:*`, `reviewer` agent
- **Documentation**: Maps to `/docs:*`, `documenter` agent
- **Testing**: Maps to test-related commands, `test-writer` agent

### Command Discovery
Dynamically scans the commands directory to:
- Identify all available slash commands by category
- Match user intent to appropriate command patterns
- Suggest command sequences for complex tasks
- Recommend parallel execution opportunities

### Agent Orchestration
Based on Agent Orchestra Framework:
- **Orchestrators**: For complex, multi-step coordination
- **Workers**: For specific, focused execution
- **Parallel Patterns**: When tasks are independent
- **Sequential Patterns**: When tasks have dependencies

## Examples

### Example 1: Basic Bug Fix
```bash
/prompt:create "My login form isn't working"
```

**Enhanced Output:**
```
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
```

### Example 2: Code Quality Improvement
```bash
/prompt:create "Make my code better"
```

**Enhanced Output:**
```
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
```

### Example 3: Feature Implementation
```bash
/prompt:create "Add user authentication to my app"
```

**Enhanced Output:**
```
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