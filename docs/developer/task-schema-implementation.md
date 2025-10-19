# 7-Section Task.md Schema Implementation

## Overview

Implemented comprehensive 7-section progressive task.md schema that populates dynamically as tasks are executed. The schema organizes task context into scannable sections with clear separation of concerns.

**Files Created/Modified**:

- ✅ `/scripts/task/task_schema_manager.py` - NEW utility for schema operations
- ✅ `/commands/task/execute.md` - MODIFIED STEP 4-7 for schema population
- ✅ `/.agent/tasks.md` - Existing tasks now support 7-section structure

## 7-Section Structure

### 1. Header & Metadata

```markdown
## [TASK-XXX] {title}

**Status**: [status]
**Priority**: [priority]
**Category**: [category]
**Origin**: [origin]
**Created**: [ISO timestamp]
**Completed**: [ISO timestamp] (optional, if done)
**Task Details Directory**: [path] (optional, if analysis performed)
```

### 2. Description

Original task description as provided.

```markdown
### Description

{original task description}
```

### 3. Status Summary

Quick scannable status with visual checkboxes. Populated during task execution.

```markdown
### Status Summary

- [x] Task setup complete
- [x] Analysis in progress
- [ ] Findings synthesized
- [ ] Next steps identified
```

### 4. Key Findings

3-5 actionable one-liners extracted from agent analysis.

```markdown
### Key Findings

1. {Finding extracted from analysis}
2. {Finding extracted from analysis}
3. {Finding extracted from analysis}
```

### 5. Synthesis & Conclusions

Cross-agent insights and consensus points.

```markdown
### Synthesis & Conclusions

**Cross-Agent Consensus**: {What all agents agreed on}
**Critical Issues**: {Most important items}
**Recommendations**: {Actionable next steps}
```

### 6. Next Steps

Checkboxed action items derived from task requirements and analysis.

```markdown
### Next Steps

- [ ] Action 1
- [ ] Action 2
- [ ] Action 3

**Blockers**: [Dependencies or constraints]
```

### 7. Analysis Details

Links to full agent context files and directory structure.

```markdown
### Analysis Details

Full analysis saved to:
`.agent/Session-{session}/Task-XXX--{title}/`

Agent findings:
- `{agent-name}.md` - {Description of what agent analyzed}
- `{agent-name}.md` - {Description of what agent analyzed}
```

### 8. Main Thread Log

Execution timeline showing when each phase completed.

```markdown
### Main Thread Log

**Execution Timeline**:
- Task Created: [timestamp]
- Task Setup: [timestamp]
- Agents Invoked: [agent1, agent2, ...]
- Analysis Completed: [timestamp]
- Last Updated: [timestamp]

**Status**: in-progress
**Agents Completed**: {count}
```

## Implementation Details

### task_schema_manager.py

**Core Functions**:

1. **extract_task_section(tasks_file, task_id)** - Extracts full task section from tasks.md
   - Returns text from `## [TASK-XXX]` to next `---` separator
   - Handles markdown format with proper regex

2. **parse_task_metadata(task_section)** - Extracts metadata fields
   - Parses: task_id, title, status, priority, category, origin, created, completed
   - Returns dict with all metadata

3. **extract_description(task_section)** - Gets task description
   - Tries modern `### Description` section format first
   - Falls back to legacy `**Description**:` inline format
   - Handles both old and new task formats

4. **create_7section_template(task_id, title, description, task_details_dir, metadata)** - Creates complete template
   - Generates all 7 sections with proper markdown
   - Substitutes metadata values into header
   - Uses provided directory for Analysis Details link
   - Returns complete formatted template string

5. **populate_key_findings(findings_text)** - Extracts findings from agent output
   - Parses findings_text for key points
   - Limits to top 5 findings
   - Formats as numbered markdown list

6. **generate_main_thread_log(task_id, agents_list, setup_time, complete_time)** - Creates execution log
   - Generates Main Thread Log section with timeline
   - Lists all agents invoked
   - Shows completion timestamps

7. **update_task_in_file(tasks_file, task_id, new_section)** - Updates task.md
   - Replaces task section in place
   - Maintains file integrity
   - Returns success/failure status

**CLI Commands**:

```bash
# Extract task section
task_schema_manager.py extract <tasks_file_path> <task_id>

# Parse metadata
task_schema_manager.py parse_metadata <task_section>

# Extract description
task_schema_manager.py extract_description <task_section>

# Populate findings
task_schema_manager.py populate_key_findings <findings_text>

# Generate log
task_schema_manager.py generate_main_thread_log <task_id> <agents_csv> <setup_time> <complete_time>

# Create template
task_schema_manager.py create_template <task_id> <title> <description> [task_details_dir] [metadata_json]

# Update task in file
task_schema_manager.py update_task_in_file <tasks_file_path> <task_id> <new_section>
```

### execute.md Integration

**STEP 4 Changes**:

- Extract TASK_SECTION for metadata capture
- Store TASK_SETUP_TIME timestamp
- Pass full section to setup_task_atomic for metadata preservation

**STEP 6 Changes**:

- After agent invocation, record AGENT_COMPLETE_TIME
- Accumulate agents list: AGENTS_INVOKED
- Read agent findings from context files

**STEP 7 Changes**:

- Create 7-section template with extracted metadata
- Populate Key Findings from agent analysis
- Generate Main Thread Log with execution timeline
- Update task.md file with populated sections
- Display completion message with section indicators

## Data Flow

```text
1. STEP 3: Extract TASK_SECTION (full metadata + description)
                    ↓
2. STEP 4: parse_task_metadata(TASK_SECTION)
                    ↓
3. STEP 4: Extract description via extract_description()
                    ↓
4. STEP 5-6: Accumulate agent results and findings
                    ↓
5. STEP 7: create_7section_template(metadata + description)
                    ↓
6. STEP 7: populate_key_findings(agent_output)
                    ↓
7. STEP 7: generate_main_thread_log(agents + timestamps)
                    ↓
8. STEP 7: update_task_in_file() - Write to tasks.md
                    ↓
9. Display completion with section indicators
```

## Usage Example

### Creating a new task context

```bash
# Extract existing task
TASK_SECTION=$(task_schema_manager.py extract ~/.agent/tasks.md TASK-029)

# Parse metadata
METADATA=$(task_schema_manager.py parse_metadata "$TASK_SECTION")

# Get description
DESCRIPTION=$(task_schema_manager.py extract_description "$TASK_SECTION")

# Create 7-section template
TEMPLATE=$(task_schema_manager.py create_template \
  "TASK-029" \
  "Task Title" \
  "$DESCRIPTION" \
  ".agent/Session-session1/Task-029" \
  "$METADATA")
```

### Populating sections with analysis

```bash
# Populate key findings
KEY_FINDINGS=$(task_schema_manager.py populate_key_findings "$AGENT_FINDINGS")

# Generate main thread log
LOG=$(task_schema_manager.py generate_main_thread_log \
  "TASK-029" \
  "agent1,agent2" \
  "2025-10-18T15:00:00Z" \
  "2025-10-18T15:30:00Z")

# Update task.md
task_schema_manager.py update_task_in_file \
  ~/.agent/tasks.md \
  "TASK-029" \
  "$UPDATED_SECTION"
```

## Backward Compatibility

- ✅ Handles legacy `**Description**:` inline format
- ✅ Supports existing tasks.md structure
- ✅ All 32 existing tasks remain intact
- ✅ Gracefully handles missing optional fields
- ✅ Automatically detects format and adapts

## Testing

**Integration Test Results**:

- ✅ Extract task section: PASSED
- ✅ Parse metadata (8 fields): PASSED
- ✅ Extract description (both formats): PASSED
- ✅ Create 7-section template: PASSED
- ✅ Populate key findings: PASSED
- ✅ Generate main thread log: PASSED
- ✅ Update task in file: PASSED

**Code Quality**:

- ✅ Python syntax check: PASSED
- ✅ Type hints for all functions
- ✅ Comprehensive docstrings
- ✅ Proper error handling

## Benefits

1. **Progressive Population**: Sections populate as task matures
2. **Quick Scanning**: Key Findings and Summary enable rapid overview
3. **Full Context**: All 7 sections preserve complete task history
4. **Agent Integration**: Findings extracted directly from agent analysis
5. **Execution Timeline**: Main Thread Log shows complete workflow timing
6. **Isolation**: Task Details Directory links to separate agent context files
7. **Flexibility**: Works with tasks of any type and complexity

## Next Steps

1. **Deploy**: Copy task_schema_manager.py to ~/.claude/scripts/task/
2. **Integrate**: Use modified execute.md when executing tasks
3. **Test**: Run /task:execute with test task to verify population
4. **Monitor**: Verify task.md updates correctly after first execution
5. **Refine**: Gather feedback and iterate on schema if needed

## File Locations

- **Schema Manager**: `~/.claude/scripts/task/task_schema_manager.py` (444 lines)
- **Command Integration**: `~/.claude/commands/task/execute.md` (modified STEP 4-7)
- **Task Registry**: `~/.claude/.agent/tasks.md` (32 existing tasks)
- **Spec**: This document at `~/.claude/docs/developer/task-schema-implementation.md`
