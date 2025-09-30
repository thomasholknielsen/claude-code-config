# Command Template - Standard Format

This template should be used for all new commands and as a reference for standardizing existing commands.

## Standard Command Format

```markdown
---
description: "Single clear sentence describing what this command does"
category: "primary_category"
tools: ["Tool1", "Tool2", "Tool3"]
complexity: "simple|moderate|complex"
argument-hint: "Brief description of expected arguments (optional)"
model: "opus|sonnet (optional - only if command requires specific model)"
---

# Command: {Action Verb} {Object}

## Purpose
Single sentence describing the command's primary function.

## Usage
```bash
/{category}:{command-name} $ARGUMENTS
```

**Arguments**: $ARGUMENTS placeholder will be replaced with user input

## Process

1. Step 1: What the command does first
2. Step 2: What happens next
3. Step 3: Final outcome

## Agent Integration

- **Primary Agent**: {agent-name} - Specialist that can be spawned to execute this command
- **Secondary Agents**: {if-any} - Additional specialists that may be spawned during execution

## Implementation

- **Tool Usage**: Use Task() for consulting specialist agents, SlashCommand() for executing other commands
- **Argument Handling**: $ARGUMENTS placeholder is automatically replaced with user input

## Examples

```bash
# Basic usage
/{category}:{command-name}

# With arguments
/{category}:{command-name} "specific target"

# Advanced usage
/{category}:{command-name} --option value
```yaml

## Output

Description of what the user can expect as output.

## Integration Points

- **Follows**: Commands that should precede this one
- **Followed by**: Commands that typically come after
- **Related**: Similar or complementary commands

## Quality Standards

- Validation criteria the command meets
- Success indicators
- Error handling approach

## $ARGUMENTS Placeholder System

Commands use the `$ARGUMENTS` placeholder which is automatically replaced with user input:

- **Purpose**: Standardized way to handle user input in command templates
- **Usage**: Include `$ARGUMENTS` in Usage section: `/{category}:{command-name} $ARGUMENTS`
- **Replacement**: The system automatically replaces `$ARGUMENTS` with actual user input
- **Benefits**: Consistent argument handling across all commands

**Example:**
- Template: `/fix:bug-quickly $ARGUMENTS`
- User input: `login button not working`
- Executed: `/fix:bug-quickly login button not working`

## Tool Usage Patterns

### Task() vs SlashCommand()

- **Task()**: Use to consult specialist agents for advisory guidance
  - `Task("consult bug-fixer specialist for debugging approach", specialists=["bug-fixer"])`
- **SlashCommand()**: Use to delegate to other commands
  - `SlashCommand("/review:code")`

## Standardization Rules

### 1. Header Format
- Always use: `# Command: {Action Verb} {Object}`
- Examples: "# Command: Analyze Performance", "# Command: Generate Documentation"

### 2. YAML Frontmatter (Required)
```yaml
---
description: "Single clear sentence under 100 characters"
category: "folder_name_where_command_exists"
tools: ["Tool1", "Tool2"]  # Claude tools used
complexity: "simple|moderate|complex"
argument-hint: "Brief description of expected arguments (optional)"
model: "opus|sonnet (optional - only if command requires specific model)"
---
```

### 3. Section Structure (Consistent Order)

1. **Purpose** - Single sentence
2. **Usage** - Command syntax with $ARGUMENTS placeholder
3. **Process** - Numbered steps
4. **Agent Integration** - Primary/secondary agents that can be spawned
5. **Implementation** - Tool usage patterns and argument handling
6. **Examples** - Real usage examples
7. **Output** - Expected results
8. **Integration Points** - Related commands

### 4. Description Standards

- **Purpose**: Maximum 1 sentence, clear action
- **Process**: 3-5 numbered steps maximum
- **Examples**: Include at least 2 examples
- **Integration**: Show command relationships

### 5. Language Consistency

- Use active voice: "Analyzes performance" not "Performance is analyzed"
- Use present tense: "Generates documentation" not "Will generate documentation"
- Be specific: "Formats JavaScript and TypeScript" not "Formats code"
- Avoid redundancy: Don't repeat the same information in multiple sections

### 6. Agent Integration Standards

- **Primary Agent**: The specialist that can be spawned to execute the command
- **Secondary Agents**: Additional specialists that may be spawned during execution
- **Agent Selection**: Based on Agent Orchestra Framework roles
- **Spawning Pattern**: Commands describe which specialists CAN be spawned, not which they run IN

### 7. Complexity Classification

- **Simple**: Single agent, single action, predictable output
- **Moderate**: Multiple steps, some analysis required, may involve multiple tools
- **Complex**: Multiple agents, coordination required, analysis and decision-making

## Examples of Standardized Commands

### Simple Command Example

```markdown
---
description: "Fixes obvious bugs quickly with minimal analysis"
category: "fix"
tools: ["Read", "Edit", "Bash"]
complexity: "simple"
argument-hint: "Description of the bug or error message"
---

# Command: Fix Bug Quickly

## Purpose
Identifies and fixes obvious bugs with rapid diagnosis and immediate resolution.

## Usage
```bash
/fix:bug-quickly $ARGUMENTS
```

**Arguments**: $ARGUMENTS placeholder will be replaced with user input

## Process

1. Reproduce the issue to understand the problem
2. Isolate the root cause using targeted analysis
3. Apply the fix with minimal code changes
4. Verify the fix resolves the issue

## Agent Integration

- **Primary Agent**: bug-fixer - Specialist that can be spawned to handle complete bug resolution workflow

## Implementation

- **Tool Usage**: Use Task() to consult bug-fixer specialist for advisory guidance
- **Argument Handling**: $ARGUMENTS placeholder is automatically replaced with user bug description

## Examples

```bash
# Fix specific bug
/fix:bug-quickly "404 error on user profile page"

# Fix with error message
/fix:bug-quickly "TypeError: Cannot read property 'map' of undefined"
```

## Output

- Fixed code with explanation of changes made
- Brief description of root cause
- Confirmation that fix resolves the issue

## Integration Points

- **Follows**: /analyze:potential-issues (for complex bugs)
- **Followed by**: /test (to verify fix)
- **Related**: /review:code, /docs:update

### Complex Command Example

```markdown
---
description: "Orchestrates comprehensive multi-perspective code review process"
category: "workflows"
tools: ["Task", "SlashCommand", "TodoWrite"]
complexity: "complex"
argument-hint: "Optional scope (file pattern, directory, or 'all')"
model: "opus"
---

# Command: Run Comprehensive Review

## Purpose
Executes parallel code review across security, quality, and design perspectives.

## Usage
```bash
/workflows:run-comprehensive-review $ARGUMENTS
```

**Arguments**: $ARGUMENTS placeholder will be replaced with user input

## Process

1. Coordinate parallel review streams using research-analysis-specialist
2. Execute security, code quality, and design reviews simultaneously
3. Consolidate findings from all review types
4. Generate prioritized recommendations
5. Create action plan for addressing issues

## Agent Integration

- **Primary Agent**: task-analysis-specialist - Advisory specialist for coordinating entire review strategy
- **Secondary Agents**: research-analysis-specialist - Advisory specialist for parallel review planning
- **Technical Specialists**: reviewer - Advisory specialist for individual review guidance

## Implementation

- **Tool Usage**: Use Task() to consult specialist agents, SlashCommand() to execute review commands
- **Argument Handling**: $ARGUMENTS placeholder is automatically replaced with user scope specification

## Examples

```bash
# Review entire codebase
/workflows:run-comprehensive-review

# Review specific directory
/workflows:run-comprehensive-review "src/components/"

# Review recent changes
/workflows:run-comprehensive-review "*.js"
```

## Output

- Consolidated review report with findings from all perspectives
- Prioritized list of issues requiring attention
- Recommended action plan with timeline
- Individual detailed reports from each review type

## Integration Points

- **Follows**: Major code changes, before releases
- **Followed by**: /fix:*, /refactor:*, /clean:*
- **Related**: /review:security, /review:code, /review:design

```text
```
