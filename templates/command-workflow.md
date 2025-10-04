---
description: "<Orchestrate [action] using atomic slash commands>"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand", "Read", "Write"]
complexity: "moderate|complex"
allowed-tools: SlashCommand(/command:*), Read, Write
---

# Command: Run <Workflow Name>

## Purpose

<Single sentence describing the orchestration workflow and its overall goal>

## Usage

```bash
/workflows:<workflow-name> $ARGUMENTS
```

**Arguments**: <Optional parameters specific to the workflow operation>

## Implementation Steps

1. **Execute Command 1**: <Which command and why>

   ```bash
   SlashCommand("/<category>:<command>")
   ```

2. **Execute Command 2**: <Next command in sequence>

   ```bash
   SlashCommand("/<category>:<command> $ARGUMENTS")
   ```

3. **Execute Command 3**: <Final command>

   ```bash
   SlashCommand("/<category>:<command>")
   ```

4. **Results Consolidation**: <How outputs are aggregated or synthesized>

## Sequential Command Execution

**Orchestration Pattern**:

```python
# Step 1: First command
SlashCommand("/<category>:<command1>")

# Step 2: Second command (depends on step 1)
SlashCommand("/<category>:<command2>")

# Step 3: Third command (depends on step 2)
SlashCommand("/<category>:<command3>")

# Step 4: Synthesize results
<consolidation logic>
```

**Command Dependencies**:

- <Command 1> must complete before <Command 2>
- <Command 2> must complete before <Command 3>
- <Final consolidation> depends on all commands

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential execution of atomic slash commands and consolidates findings
- **Coordination**: Ensures proper command sequencing, error handling, and result aggregation

## Examples

### Example 1: <Workflow Scenario>

```bash
/workflows:<workflow-name> $ARGUMENTS
# where $ARGUMENTS = "<specific parameters if any>"

# Execution sequence:
# 1. SlashCommand("/<category>:<command1>") - <Purpose>
# 2. SlashCommand("/<category>:<command2>") - <Purpose>
# 3. SlashCommand("/<category>:<command3>") - <Purpose>
# 4. <Consolidate results and provide summary>
```

### Example 2: <Another Workflow Scenario>

```bash
/workflows:<workflow-name>

# Execution sequence:
# 1. SlashCommand("/<category>:<command1>") - <Purpose>
# 2. SlashCommand("/<category>:<command2>") - <Purpose>
# 3. <Result aggregation>
```

## Integration Points

- **Input**: <What this workflow requires to start>
- **Dependencies**: <Which atomic commands this workflow uses>
- **Output**: <What comprehensive result is produced>
- **Follow-up**: <Suggested next steps after workflow completes>

## Quality Standards

- <Orchestration quality criterion>
- <Error handling across commands>
- <Result consolidation completeness>
- <Sequential execution validation>

## Output

- <Consolidated workflow results>
- <Summary of executed commands>
- <Any generated artifacts or reports>
- <Next steps or recommendations>
