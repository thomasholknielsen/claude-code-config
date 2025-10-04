---
description: "<Single clear sentence describing command purpose>"
argument-hint: "[arg1] [--flag=value]"
category: "<category-name>"
tools: ["Tool1", "Tool2", "Tool3"]
complexity: "simple|moderate|complex"
allowed-tools: Tool1, Tool2, Bash(command:*), Bash(another-cmd:*)
---

# Command: <Action Verb> <Object>

## Purpose

<Single sentence describing the primary function of this command>

## Usage

```bash
/<category>:<command-name> $ARGUMENTS
```

**Arguments**:

- `$1` (<name>): <Description> (optional/required)
- `$2` (<flag>): <Description> (optional)
- `$3` (<flag>): <Description> (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "value1"` - <Description of what this does>
- `$ARGUMENTS = "value1 --flag=value2"` - <Description with flag>
- `$ARGUMENTS = "--flag-only"` - <Description>

## Process

1. **Step 1**: <Clear action description>
   - <Sub-step or detail>
   - <Sub-step or detail>

2. **Step 2**: <Next action>
   - <Sub-step or detail>

3. **Step 3**: <Final outcome>
   - <Sub-step or detail>

## Agent Integration

- **Specialist Options**: <agent-name> can be spawned to <describe role and coordination>
- **Primary Agent**: <agent-name> - <Role description>
- **Coordination**: <How agent coordinates with other specialists if applicable>

## Examples

### Example 1: <Scenario Name>

```bash
/<category>:<command> $ARGUMENTS
# where $ARGUMENTS = "<specific values>"

# Expected behavior:
→ <What happens>
→ <Result>
```

### Example 2: <Another Scenario>

```bash
/<category>:<command> $ARGUMENTS
# where $ARGUMENTS = "<different values>"

# Expected behavior:
→ <What happens>
→ <Result>
```

## Parallelization Patterns (Optional)

*Include this section if the command supports parallel execution*

**Use Case**: <When parallel execution is beneficial>

```python
# Example parallel task coordination
Task("Parallel task 1 description")
Task("Parallel task 2 description")
Task("Parallel task 3 description")
```

**Coordination Strategy**:

- <How tasks are coordinated>
- <Dependencies between parallel tasks>
- <Result aggregation approach>

## Integration Points

- **Follows**: <Commands that typically run before this one>
- **Followed by**: <Commands that typically run after this one>
- **Related**: <Related commands in the same domain>

## Quality Standards

- <Quality criterion 1>
- <Quality criterion 2>
- <Quality criterion 3>
- <Success validation approach>
- <Error handling expectations>

## Output

- <What this command produces>
- <What feedback is provided to the user>
- <What files/artifacts are created or modified>
