# Command Audit Report

## Executive Summary

Audit of 47 commands across 16 categories revealed significant inconsistencies in format, structure, and documentation standards. This report outlines findings and provides a standardization roadmap.

## Audit Findings

### Format Inconsistencies

#### YAML Frontmatter
- **Inconsistent presence**: 23 commands have frontmatter, 24 don't
- **Inconsistent fields**: Different field names and formats used
- **Missing standards**: No consistent schema for metadata

**Examples of variations:**
```yaml
# Variation 1
---
description: Performance bottleneck analysis with optimization recommendations
category: performance
tools: Bash, Read, Grep
---

# Variation 2
---
description: Automated code formatting using project's configured formatter
domain: code
boundary: Automated formatting tools only
---

# Variation 3 (none)
# Documentation Generator
(No frontmatter at all)
```

#### Header Formats
- **Inconsistent naming**: Mixed patterns across commands
- **No standard structure**: Some descriptive, others action-oriented

**Examples:**
- `# Performance Profiling` (noun-based)
- `# Documentation Generator` (role-based)
- `# Auto Format Code` (action-based)
- `# Command: {Name}` (structured - only 2 commands)

### Content Structure Issues

#### Description Patterns
- **Length variation**: From single sentences to multiple paragraphs
- **Voice inconsistency**: Mix of first person ("I'll analyze") and third person ("Analyzes")
- **Purpose confusion**: Some describe what user gets, others what command does

#### Process Documentation
- **Missing process steps**: 31 commands lack clear step-by-step process
- **Inconsistent numbering**: Some use bullets, others numbers, some prose
- **Implementation details**: Some commands contain actual code, others just descriptions

### Category Analysis

#### Command Distribution
| Category | Count | Consistency Level | Issues |
|----------|-------|------------------|--------|
| spec-kit | 7 | Low | Implementation details mixed with descriptions |
| workflows | 7 | Medium | Consistent naming but varied content |
| refactor | 6 | Medium | Good structure but missing agent info |
| docs | 6 | Low | Mixed formats, no agent assignment |
| clean | 4 | Medium | Consistent purpose but format varies |
| analyze | 3 | Medium | Good technical focus but format issues |
| to-do | 4 | Low | Unclear purpose boundaries |
| review | 3 | Medium | Clear purpose but missing integration |
| fix | 2 | High | Most consistent category |
| explain | 2 | Medium | Good content but format issues |
| implement | 2 | Medium | Clear purpose, needs agent assignment |
| git | 1 | High | Well structured |

### Agent Integration Issues

#### Missing Agent Assignment
- **41 commands** lack clear agent assignment
- **6 commands** have agent information
- **No consistent mapping** between commands and Agent Orchestra roles

#### Integration Gaps
- **Commands don't specify** which orchestrator should handle them
- **No documentation** of agent collaboration patterns
- **Missing handoff protocols** between commands

### Quality Standards Issues

#### Documentation Quality
- **Inconsistent examples**: Some have none, others have many
- **Missing integration points**: Commands exist in isolation
- **No success criteria**: Unclear what constitutes successful execution
- **Poor discoverability**: Hard to find related commands

#### Technical Specification
- **Missing tool requirements**: Not all commands specify needed tools
- **No complexity classification**: Can't determine resource requirements
- **Unclear dependencies**: No documentation of prerequisite commands

## Standardization Recommendations

### Phase 1: Template Implementation (Immediate)
1. **Apply standard template** to all commands using the created template
2. **Add required YAML frontmatter** with consistent schema
3. **Standardize headers** to "# Command: {Action} {Object}" format
4. **Add agent assignments** based on Agent Orchestra framework

### Phase 2: Content Standardization (Short-term)
1. **Rewrite descriptions** to consistent length and voice
2. **Add process steps** to all commands (3-5 numbered steps)
3. **Include integration points** showing command relationships
4. **Add quality examples** for each command

### Phase 3: Agent Integration (Medium-term)
1. **Map all commands** to appropriate orchestrators/workers
2. **Document coordination patterns** between agents and commands
3. **Add complexity classifications** for resource planning
4. **Create command workflows** showing typical usage patterns

### Phase 4: Quality Enhancement (Long-term)
1. **Add automated validation** for command format compliance
2. **Create command discovery system** for better navigation
3. **Implement success metrics** for command effectiveness
4. **Regular audit schedule** for maintaining standards

## Proposed Standard Format

```markdown
---
description: "Single clear sentence under 100 characters"
category: "folder_name"
agent: "primary-agent-name"
tools: ["Tool1", "Tool2"]
complexity: "simple|moderate|complex"
---

# Command: {Action Verb} {Object}

## Purpose
Single sentence describing the command's primary function.

## Usage
```
/{category}:{command-name} [arguments]
```

## Process
1. Step 1: Clear action
2. Step 2: Next action
3. Step 3: Final outcome

## Agent Integration
- **Primary Agent**: agent-name - brief role
- **Secondary Agents**: if any

## Examples
[Real usage examples]

## Output
[Expected results]

## Integration Points
- **Follows**: prerequisite commands
- **Followed by**: typical next commands
- **Related**: similar commands
```

## Impact Assessment

### Benefits of Standardization
- **Improved discoverability**: Users can find relevant commands
- **Better agent integration**: Clear orchestrator assignments
- **Enhanced maintainability**: Consistent format for updates
- **Quality assurance**: Standard validation criteria
- **User experience**: Predictable command behavior

### Implementation Effort
- **High initial effort**: Requires updating all 47 commands
- **Medium ongoing effort**: New commands must follow template
- **Validation automation**: Can be automated once template is established

### Risk Mitigation
- **Backward compatibility**: Maintain existing command functionality
- **Gradual rollout**: Implement in phases to validate approach
- **User feedback**: Gather input during standardization process

## Priority Command List for Standardization

### Highest Priority (Most Used)
1. `/spec-kit:implement` - Core feature implementation
2. `/workflows:run-comprehensive-review` - Quality assurance
3. `/docs:generate` - Documentation creation
4. `/analyze:performance` - Performance optimization
5. `/fix:bug-quickly` - Rapid issue resolution

### High Priority (Inconsistent Format)
6. All `/spec-kit/*` commands - Currently mixed implementation/description
7. All `/docs/*` commands - Missing agent assignments
8. All `/workflows/*` commands - Need orchestrator mapping

### Medium Priority (Good Content, Format Issues)
9. `/refactor/*` commands - Good structure, need agent info
10. `/clean/*` commands - Consistent purpose, format varies
11. `/review/*` commands - Clear purpose, missing integration

### Lower Priority (Already Consistent)
12. `/fix/*` commands - Most consistent category
13. `/git/*` commands - Well structured

## Implementation Roadmap

### Week 1: Foundation
- [ ] Finalize command template
- [ ] Create validation checklist
- [ ] Update 5 highest priority commands
- [ ] Test with user feedback

### Week 2: High Priority
- [ ] Standardize all spec-kit commands
- [ ] Update workflow commands with orchestrator assignments
- [ ] Standardize documentation commands

### Week 3: Remaining Commands
- [ ] Complete refactor and clean commands
- [ ] Update analysis and review commands
- [ ] Finalize all remaining commands

### Week 4: Validation & Testing
- [ ] Validate all commands against template
- [ ] Test agent integration points
- [ ] Update project documentation
- [ ] Create maintenance procedures

This audit provides the foundation for systematic command standardization aligned with the Agent Orchestra framework.