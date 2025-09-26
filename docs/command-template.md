# Command Template - Standard Format

This template should be used for all new commands and as a reference for standardizing existing commands.

## Standard Command Format

```markdown
---
description: "Single clear sentence describing what this command does"
category: "primary_category"
agent: "primary-agent-that-executes-this"
tools: ["Tool1", "Tool2", "Tool3"]
complexity: "simple|moderate|complex"
---

# Command: {Action Verb} {Object}

## Purpose
Single sentence describing the command's primary function.

## Usage
```
/{category}:{command-name} [arguments]
```

**Arguments**: Description of expected arguments (if any)

## Process
1. Step 1: What the command does first
2. Step 2: What happens next
3. Step 3: Final outcome

## Agent Integration
- **Primary Agent**: {agent-name} - {brief role description}
- **Secondary Agents**: {if-any} - {brief role description}

## Examples
```bash
# Basic usage
/{category}:{command-name}

# With arguments
/{category}:{command-name} "specific target"

# Advanced usage
/{category}:{command-name} --option value
```

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
```

## Standardization Rules

### 1. Header Format
- Always use: `# Command: {Action Verb} {Object}`
- Examples: "# Command: Analyze Performance", "# Command: Generate Documentation"

### 2. YAML Frontmatter (Required)
```yaml
---
description: "Single clear sentence under 100 characters"
category: "folder_name_where_command_exists"
agent: "primary-agent-name"
tools: ["Tool1", "Tool2"]  # Claude tools used
complexity: "simple|moderate|complex"
---
```

### 3. Section Structure (Consistent Order)
1. **Purpose** - Single sentence
2. **Usage** - Command syntax
3. **Process** - Numbered steps
4. **Agent Integration** - Primary/secondary agents
5. **Examples** - Real usage examples
6. **Output** - Expected results
7. **Integration Points** - Related commands

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
- **Primary Agent**: The orchestrator or worker that executes the command
- **Secondary Agents**: Any agents called during execution
- **Agent Selection**: Based on Agent Orchestra Framework roles

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
agent: "bug-fixer"
tools: ["Read", "Edit", "Bash"]
complexity: "simple"
---

# Command: Fix Bug Quickly

## Purpose
Identifies and fixes obvious bugs with rapid diagnosis and immediate resolution.

## Usage
```
/fix:bug-quickly "login button not working"
```

**Arguments**: Description of the bug or error message

## Process
1. Reproduce the issue to understand the problem
2. Isolate the root cause using targeted analysis
3. Apply the fix with minimal code changes
4. Verify the fix resolves the issue

## Agent Integration
- **Primary Agent**: bug-fixer - Handles complete bug resolution workflow

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
```

### Complex Command Example
```markdown
---
description: "Orchestrates comprehensive multi-perspective code review process"
category: "workflows"
agent: "task-orchestrator"
tools: ["Task", "SlashCommand", "TodoWrite"]
complexity: "complex"
---

# Command: Run Comprehensive Review

## Purpose
Executes parallel code review across security, quality, and design perspectives.

## Usage
```
/workflows:run-comprehensive-review [scope]
```

**Arguments**: Optional scope (file pattern, directory, or "all")

## Process
1. Coordinate parallel review streams using research-orchestrator
2. Execute security, code quality, and design reviews simultaneously
3. Consolidate findings from all review types
4. Generate prioritized recommendations
5. Create action plan for addressing issues

## Agent Integration
- **Primary Agent**: task-orchestrator - Coordinates entire review process
- **Secondary Agents**: research-orchestrator - Manages parallel reviews
- **Workers**: reviewer - Executes individual review types

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
```