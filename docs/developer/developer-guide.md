# Developer Guide - Claude Code Command System

## Architecture Overview

The Claude Code Command System is built on the **Agent Specialist Framework**, a task-focused coordination system that
replaces traditional domain-based agents with specialized analysis and execution specialists.

### System Components

```mermaid
graph TB
    subgraph "Claude Code System"
        Settings[settings.json]
        Claude[CLAUDE.md]
        Scripts[scripts/]

        subgraph "Agent Specialist Framework"
            AnalysisSpecialists[3 Strategic Specialists]
            ExecutionSpecialists[5 Technical Specialists]
        end

        subgraph "Commands"
            Analyze[analyze/]
            Clean[clean/]
            Docs[docs/]
            Fix[fix/]
            Git[git/]
            Review[review/]
            SpecKit[spec-kit/]
            Workflows[workflows/]
        end

        subgraph "Hooks System"
            PromptLog[Prompt Logging]
            Notifications[Smart Notifications]
            SearchUpdate[Search Updates]
        end
    end

    User --> Settings
    Settings --> AnalysisSpecialists
    AnalysisSpecialists --> ExecutionSpecialists
    ExecutionSpecialists --> Commands
    Commands --> Hooks
```python

## Agent Specialist Framework

### Analysis Specialists (Advisory Layer)

**Note**: Only the main Claude Code thread can orchestrate parallelization. Strategic specialists are advisory consultants that provide recommendations and strategic planning guidance.

#### 1. task-analysis-specialist

**Purpose**: General task analysis and strategic recommendations

- Analyzes task complexity
- Recommends appropriate technical specialists for consultation
- Provides TodoWrite planning guidance
- Advises on SlashCommand selection

#### 2. research-analysis-specialist

**Purpose**: Information gathering strategy and planning

- Designs research strategies for main thread execution
- Plans breadth-first search patterns using parallel tools
- Provides guidance for aggregating findings from parallel operations
- Advises on optimal tool selection for parallel information gathering

#### 3. implementation-strategy-specialist

**Purpose**: Implementation strategy and execution planning

- Analyzes file dependencies
- Provides guidance on proper execution order
- Advises on state consistency approaches
- Recommends strategies for complex multi-file changes

### Technical Specialists (Advisory Layer)

#### 1. code-writer

- **Focus**: Code generation advice and patterns
- **Advises on**: `/refactor:large-scale`, `/implement` command usage
- **Specializes in**: Implementation patterns, code structure, architectural guidance

#### 2. test-writer

- **Focus**: Testing strategy and implementation guidance
- **Advises on**: `/test`, `/spec-kit:tasks` command usage
- **Specializes in**: Test framework selection, coverage strategies, testing patterns

#### 3. bug-fixer

- **Focus**: Debugging strategy and troubleshooting guidance
- **Advises on**: `/fix:bug-quickly`, `/analyze:potential-issues` command usage
- **Specializes in**: Root cause analysis approaches, systematic debugging strategies

#### 4. reviewer

- **Focus**: Code quality and security analysis guidance
- **Advises on**: `/review:code`, `/review:security` command usage
- **Specializes in**: Review strategies, quality assessment patterns, security best practices

#### 5. documenter

- **Focus**: Documentation strategy and format guidance
- **Advises on**: `/docs:generate`, `/docs:api` command usage
- **Specializes in**: Documentation patterns, format selection, content organization

## Development Standards

### Creating New Commands

#### 1. Command Structure

```text
commands/{category}/{command-name}.md
```text

#### 2. Command Format

```markdown
# Command: {action-verb} {object}

## Purpose
Single clear sentence describing what this command does.

## Usage
```text

{command-name} [arguments]

```yaml

## Agent Integration
- Primary agent: {agent-name}
- Secondary agents: {if-any}

## Examples
{Real usage examples}

## Integration Points
{How this connects to other commands}
```yaml

#### 3. Naming Conventions

- **Action verb + clear object**: `analyze:performance`, `clean:code-comments`
- **No redundant prefixes**: Use category folders, not command prefixes
- **Consistent patterns**: Follow existing commands in the same category

#### 4. Categories (16 total)

- `analyze/` - Analysis and investigation
- `build/` - Building and packaging
- `clean/` - Cleanup operations
- `create/` - Code generation
- `debug/` - Debugging tools
- `deploy/` - Deployment operations
- `docs/` - Documentation
- `explain/` - Code understanding
- `fix/` - Bug fixes
- `git/` - Git operations
- `operations/` - File operations
- `review/` - Code review
- `spec-kit/` - Feature workflow
- `test/` - Testing
- `to-do/` - Task management
- `workflows/` - Multi-step workflows

### Creating New Agents

#### 1. Agent Types

- **Strategic Specialists**: Provide strategic planning and coordination guidance for complex tasks
- **Technical Specialists**: Provide domain-specific advisory guidance
- **Domain Specialists**: Specialized domain expertise (rare, for specific use cases)

#### 2. Agent File Structure

```text
agents/{type}/{agent-name}.md
```

**Directory Structure:**

- `agents/strategic-specialists/` - Strategic planning and coordination advisors
- `agents/technical-specialists/` - Domain-specific advisory specialists

#### 3. Agent Definition Format

```markdown
# Agent: {agent-name}

## Role
{Single sentence describing purpose}

## Capabilities
- {Specific capability 1}
- {Specific capability 2}

## Commands
- {Primary slash commands this agent uses}

## Model Requirements
- **Model**: {opus/sonnet/haiku}
- **Reasoning**: {Why this model level}

## Think Commands Support
- **think**: {Basic analysis}
- **think hard**: {Deep analysis}
- **ultra think**: {Comprehensive planning}

## Integration
{How this agent works with others}

## Usage Patterns
{Common workflows using this agent}
```yaml

#### 4. Agent Constraints

- **Single Responsibility**: Each agent has one clear focus
- **No Overlap**: Agents should not duplicate functionality
- **Clear Boundaries**: Well-defined interaction points
- **Tool Integration**: Provide guidance on SlashCommand selection and usage

### Hook Development

#### 1. Hook Types (3 supported)

- **UserPromptSubmit**: Triggered on every user input
- **Stop**: Triggered when tasks complete
- **PreToolUse**: Triggered before specific tools

#### 2. Hook Implementation

```python
# scripts/{hook-name}.py
import os
import sys
from datetime import datetime

def execute_hook():
    """Hook implementation"""
    try:
        # Your hook logic here
        pass
    except Exception as e:
        print(f"Hook error: {e}", file=sys.stderr)

if __name__ == "__main__":
    execute_hook()
```text

#### 3. Hook Registration (settings.json)

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "python -c \"import os; exec(open(os.path.expanduser('~/.claude/scripts/hooks/your-hook.py')).read())\""
      }]
    }]
  }
}
```yaml

#### 4. Hook Best Practices

- **Fast execution**: Hooks should complete quickly
- **Error handling**: Always catch and log exceptions
- **Resource cleanup**: Clean up temporary files
- **Security**: Never log sensitive information

### Security Guidelines

#### 1. Permission Management

```json
{
  "permissions": {
    "allow": ["Safe operations"],
    "deny": ["Sensitive patterns"]
  }
}
```bash

#### 2. Git Operations Constraints

- **CRITICAL**: Only `/git/*` commands can perform Git operations
- **All specialists**: Provide advisory guidance on Git operations, actual execution via SlashCommand in main thread
- **No direct Git**: Agents cannot call git commands directly
- **Explicit consent**: All Git operations require user approval

#### 3. Secret Protection

- **Blocked patterns**: `.env*`, `*.key`, `*.pem`, `secrets/`, `credentials/`
- **No logging**: Never log API keys, tokens, or passwords
- **Environment variables**: Use secure environment variable patterns

### Testing Guidelines

#### 1. Command Testing

```bash
# Test command existence
ls commands/{category}/{command}.md

# Test command format
grep -E "^# Command:" commands/{category}/{command}.md

# Test agent integration
grep -E "Primary agent:" commands/{category}/{command}.md
```text

#### 2. Agent Testing

```bash
# Test agent definitions
ls agents/{type}/{agent}.md

# Test model requirements
grep -E "Model:" agents/{type}/{agent}.md

# Test integration points
grep -E "Commands:" agents/{type}/{agent}.md
```yaml

#### 3. Integration Testing

- Test Agent Specialist Framework consultation patterns
- Verify specialist advisory guidance is properly integrated
- Ensure Git constraints are enforced in main thread
- Validate hook execution

## Advanced Customization

### Model Selection Strategy

- **Opus**: Planning-heavy strategic specialists (task-analysis, research-analysis, implementation-strategy)
- **Sonnet**: Balanced technical specialists (code-writer, reviewer)
- **Haiku**: Simple technical specialists (bug-fixer for obvious issues)

### Think Commands Integration

```markdown
## Think Commands Support
- **think**: Basic analysis and straightforward problem solving
- **think hard**: Deep analysis, complex reasoning, multi-step problems
- **ultra think**: Comprehensive planning, architectural decisions, complex debugging
```text

### Specialist Advisory Logic

```python
# Pseudocode for specialist advisory recommendations
def recommend_task_strategy(task_complexity, task_type):
    if complexity == "simple":
        return direct_technical_specialist_consultation()
    elif complexity == "moderate":
        return sequential_command_execution_with_specialist_guidance()
    elif complexity == "complex":
        return parallel_tool_execution_with_multiple_specialist_consultation()
```

### Extension Points

#### 1. New Command Categories

1. Create new category folder: `commands/{new-category}/`
2. Add category to CLAUDE.md command list
3. Update documentation
4. Create first command in category

#### 2. New Agent Types

1. Define in appropriate folder: `agents/{type}/`
2. Follow Agent Specialist Framework patterns
3. Ensure no overlap with existing agents
4. Document integration points

#### 3. Custom Workflows

1. Create in `commands/workflows/`
2. Use `run-{workflow-name}.md` format
3. Orchestrate multiple commands
4. Document step dependencies

## Quality Standards

### Code Quality

- **Consistency**: Follow existing patterns
- **Documentation**: Every command and agent documented
- **Testing**: Validate functionality before deployment
- **Security**: Enforce permission and Git constraints

### Documentation Quality

- **Clear Purpose**: Every component has obvious purpose
- **Usage Examples**: Real-world usage patterns
- **Integration Points**: How components work together
- **Troubleshooting**: Common issues and solutions

### Maintenance

- **Regular Reviews**: Audit commands and agents for overlap
- **Performance Monitoring**: Track command execution times
- **User Feedback**: Incorporate usage patterns
- **Security Updates**: Keep permissions current

## Migration Patterns

### From MECE to Agent Specialist Framework

1. **Identify domain agent**: Map old MECE agent to new specialist pattern
2. **Extract responsibilities**: Break into strategic/technical specialist advisory roles
3. **Update references**: Change agent execution calls to specialist consultation calls
4. **Test integration**: Ensure advisory consultation works properly
5. **Update documentation**: Reflect new advisory patterns

### Command Evolution

1. **Deprecation**: Mark old commands as deprecated
2. **Migration path**: Provide clear upgrade instructions
3. **Backward compatibility**: Maintain for transition period
4. **Documentation**: Update all references
5. **Cleanup**: Remove deprecated commands after transition

This guide provides the foundation for extending and
customizing the Claude Code Command System. Follow these patterns to maintain consistency and quality across the system.
