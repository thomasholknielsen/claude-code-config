# Skills Development Guide

## Overview

This guide covers creating and maintaining Skills within the Claude Code project. Skills extend Claude's capabilities for specialized domains and are automatically activated when relevant.

## Architectural Position

**Skills** fit into the Claude Code ecosystem as:

```
User Request
    ↓
    ├─→ Slash Commands (explicit: /command-name)
    ├─→ Domain Agents (via Task tool for analysis)
    └─→ Skills (automatic: matched by description)
```

- **Slash Commands**: Orchestrate workflows, are user-invoked
- **Skills**: Provide expertise, are model-invoked
- **Agents**: Conduct deep analysis, are spawned by commands or main thread

## When to Create a Skill

Create a Skill when you need to provide:

✅ **Specialized domain expertise** (e.g., "React patterns", "Azure DevOps workflows")
✅ **Detailed guidance for complex processes** (e.g., multi-step procedures)
✅ **Best practices & patterns** for a specific technology or workflow
✅ **Examples & templates** that Claude should reference
✅ **Read-only guidance** (information, patterns, troubleshooting)

❌ **NOT for:**
- Executing code or making changes (use Commands/Agents)
- Single-purpose utilities (use slash Commands)
- Temporary workflows (might be better as Commands)

## File Structure

```
./.claude/skills/skill-name/
├── SKILL.md              # Core Skill (REQUIRED)
├── scripts/              # Optional: Helper executables
│   └── processor.py
└── resources/            # Optional: Templates, configs
    ├── templates/
    │   └── example.md
    └── reference/
        └── terminology.md
```

## Creating a Skill: Checklist

### Phase 1: Planning

- [ ] Define single focused capability
- [ ] List 3-5 trigger scenarios
- [ ] Identify 2-3 concrete examples
- [ ] Plan 4+ best practices
- [ ] Check if existing Skill covers this

### Phase 2: Development

- [ ] Copy template: `cp ~/.claude/templates/skills/skill.md ./.claude/skills/skill-name/SKILL.md`
- [ ] Write discovery-focused description (max 1024 chars)
- [ ] Document step-by-step instructions
- [ ] Add 3+ concrete examples with inputs/outputs
- [ ] Include troubleshooting section
- [ ] List integration points

### Phase 3: Testing

- [ ] Verify YAML syntax in frontmatter
- [ ] Test with matching question: Does Claude activate the Skill?
- [ ] Test with mismatch question: Does Claude ignore it?
- [ ] Verify all examples work as documented
- [ ] Check instruction clarity

### Phase 4: Integration

- [ ] Place in `./.claude/skills/` (project-shared)
- [ ] Update project documentation if relevant
- [ ] Create pull request
- [ ] Include in git commit

### Phase 5: Maintenance

- [ ] Monitor usage and effectiveness
- [ ] Update with new examples
- [ ] Refine instructions based on feedback
- [ ] Keep version history

## Frontmatter Fields

### Required

**`name`** (string, max 64 chars)
- Lowercase letters, numbers, hyphens only
- Examples: `azure-devops`, `react-patterns`, `json-formatter`
- Used for internal reference and filesystem naming

**`description`** (string, max 1024 chars)
- **CRITICAL for skill discovery**
- Explain what it does AND when to use it
- Include keywords Claude will recognize
- Include specific use cases

Example:
```yaml
description: "Formats and validates JSON data. Use when you need to pretty-print JSON, fix formatting issues, or validate JSON syntax."
```

### Optional

**`allowed-tools`** (comma-separated list)
- Restrict which tools the Skill can access
- Useful for read-only or safety-sensitive Skills
- Format: `Tool1, Tool2, Tool3` (no brackets)
- Example: `Read, Grep, Glob`

```yaml
allowed-tools: Read, Grep, Glob
```

## SKILL.md Content Structure

### Required Sections

1. **What This Skill Does**
   - 1-2 sentence value proposition

2. **When to Use This Skill**
   - 3-5 trigger scenarios
   - Keywords Claude matches on

3. **Instructions**
   - Step-by-step process
   - Clear, sequential actions

4. **Examples**
   - 2-3 concrete scenarios
   - Input → Process → Output

### Recommended Sections

5. **Best Practices**
   - 4+ domain-specific practices
   - Explain why each matters

6. **Common Patterns**
   - Reusable workflows
   - Decision trees

7. **Troubleshooting**
   - Common issues
   - Solutions

8. **Integration Points**
   - How this connects to other tools/workflows
   - Dependencies

### Optional Sections

9. **Key Terminology**
   - Domain-specific definitions

10. **Additional Resources**
    - Links to docs, tools, references

## Writing Effective Skill Content

### Discovery-Focused Description

Your description determines when Claude activates your Skill. Make it discoverable:

```yaml
# ❌ Too vague
description: "A skill for working with Azure"

# ✅ Clear and discoverable
description: "Provides expert guidance on Azure DevOps tasks including work item management, pipelines, repositories, pull requests, and CI/CD workflows. Use when working with Azure DevOps projects, configuring pipelines, managing work items, or integrating Azure DevOps with development workflows."
```

**Why the second works:**
- Specifies exact capabilities
- Lists concrete use cases
- Includes decision keywords ("when working with", "configuring", "managing")
- Explains when Claude should use it

### Clear Instructions

Break down complex processes into sequential steps:

```markdown
## Instructions

1. **Identify** the work item type (Epic, Feature, User Story, Task, Bug)
2. **Set** appropriate fields: Title, Description, Acceptance Criteria, State
3. **Link** related items (depends on, related to, blocked by)
4. **Assign** to team member and set sprint/iteration
5. **Apply** area path and tags for organization
```

Each step should be:
- Actionable (start with verb)
- Specific (what exactly to do)
- Sequential (builds on previous steps)
- Verifiable (Claude can check completion)

### Concrete Examples

Examples are where Skills shine. Include 2-3 scenarios:

```markdown
### Example 1: Basic Scenario

**Scenario:** [Describe the situation]

**Process:**
1. [Show specific approach]
2. [Show validation]
3. [Show output]

**Output:**
[Show actual result]

### Example 2: Advanced Pattern

[Similar structure, more complexity]
```

**Make examples:**
- Real-world and relatable
- Progressive (basic → advanced)
- Include actual inputs/outputs
- Show decision points

### Best Practices Section

Provide 4+ practices with explanation:

```markdown
## Best Practices

- **Keep descriptions concise but detailed** - Balance brevity with clarity
- **Break down large features into stories** - Prevents scope creep
- **Use acceptance criteria to define done** - Creates clear completion criteria
- **Link related items to show dependencies** - Improves traceability
```

## Project-Specific Guidelines

### Directory Organization

```
./.claude/skills/
├── azure-devops/           # Cloud platform integration
├── react-patterns/         # Framework expertise
├── json-formatter/         # Utility/data handling
└── database-schema/        # Data management
```

Organize by:
- Technology/platform (Azure, AWS, etc.)
- Framework/language (React, Python, etc.)
- Domain/workflow (Testing, CI/CD, etc.)

### Naming Conventions

- Use hyphens for multi-word names: `azure-devops`, not `AzureDevOps`
- Be specific: `react-hooks-patterns`, not `react-skill`
- Match documentation references: If docs mention "React Patterns", name it `react-patterns`

### Documentation Integration

When creating a Skill, update related docs:

1. **Skills Guide** (`docs/user/skills-guide.md`)
   - Add to "Real-World Examples" if broadly useful

2. **Project CLAUDE.md**
   - Mention in skills section if project-critical

3. **README** or getting-started guides
   - Reference if it's essential for onboarding

### Git Integration

```bash
# Create the Skill
mkdir -p ./.claude/skills/my-skill
cp ~/.claude/templates/skills/skill.md ./.claude/skills/my-skill/SKILL.md

# Customize
# ... edit SKILL.md ...

# Commit
git add ./.claude/skills/my-skill/
git commit -m "feat: add my-skill for [purpose]

Provides expert guidance on [domain].
Includes [number] examples and [feature list]."
```

### Commit Message Format

```
feat: add [skill-name] skill

- Covers [main capability 1]
- Includes [feature 2]
- Documents [best practice area]
- Examples: [list example types]
```

## Advanced Features

### Supporting Scripts

If your Skill references executables:

```
my-skill/
├── SKILL.md
└── scripts/
    ├── validator.py          # Input validation
    └── transformer.js        # Data transformation
```

Reference in instructions:

```markdown
## Instructions

This skill uses `scripts/validator.py` to verify input format:

1. Input data is passed to validator
2. Script checks against rules
3. Report is generated
```

### Resource Files

For templates and reference materials:

```
my-skill/
├── SKILL.md
└── resources/
    ├── templates/
    │   ├── pull-request.md
    │   └── commit-message.md
    └── reference/
        └── terminology.md
```

Reference them:

```markdown
## Templates

Use `resources/templates/pull-request.md` as your PR description template.
```

### Version Control

Track improvements in your Skill:

```markdown
## Version History

**v1.3** (2025-01-20)
- Added multi-stage pipeline examples
- Improved troubleshooting section
- Added integration with GitHub Actions

**v1.2** (2025-01-15)
- Initial project release
```

## Testing & Validation

### YAML Validation

Ensure frontmatter is valid:

```bash
head -10 ./.claude/skills/skill-name/SKILL.md
# Should show valid YAML between ---
```

### Skill Activation Testing

Ask Claude a question matching your description:

```
# Should activate the Skill
"Help me configure [what skill does]"
"How do I [use case from skill description]?"

# Should NOT activate the Skill
"Tell me about unrelated topic"
"How do I [completely different domain]?"
```

### Content Review

- [ ] Instructions are clear and sequential
- [ ] Examples work as documented
- [ ] Troubleshooting covers common issues
- [ ] Links (if any) are correct
- [ ] Terminology is consistent
- [ ] Best practices are actionable

## Common Patterns

### Read-Only Skill (Informational)

```yaml
allowed-tools: Read, Grep, Glob
```

Use when Skill should only provide guidance, not execute actions.

### Comprehensive Domain Skill

Cover related workflows (like Azure DevOps covering projects, pipelines, tests):

```markdown
## When to Use This Skill

- Setting up Azure DevOps projects
- Configuring CI/CD pipelines
- Managing work items and sprints
- Reviewing pull requests
- Setting up branch policies
```

### Step-Heavy Skill

When the process has many sequential steps:

```markdown
## Instructions

1. Preparation Phase
   - Check prerequisites
   - Gather information
   - Plan approach

2. Execution Phase
   - [Specific steps...]

3. Validation Phase
   - [Verification steps...]

4. Completion Phase
   - [Finalization steps...]
```

## Troubleshooting

### Skill Not Being Activated?

1. Check description includes trigger keywords
2. Verify YAML syntax
3. Test with exact phrases from description
4. Review instruction clarity

### Claude Misunderstanding Instructions?

1. Add more concrete examples
2. Simplify step-by-step process
3. Use consistent terminology
4. Add explicit decision trees for complex workflows

### Skill Seems Out of Scope?

Might be better as a slash Command instead. If it:
- Is frequently invoked manually → Command
- Requires exact argument format → Command
- Orchestrates a workflow → Command

But if Claude should use it when relevant → Skill

## Maintenance

### Regular Reviews

- Every quarter: Update examples if outdated
- New releases: Add support for new features
- User feedback: Refine instructions
- Deprecations: Mark old patterns as legacy

### Deprecation Pattern

```markdown
## Legacy Patterns

⚠️ **Deprecated:** The [old pattern] is no longer recommended. Use [new pattern] instead.

### Example: [old pattern]
...
```

## Related Documentation

- **Skills User Guide:** `docs/user/skills-guide.md`
- **Skills Template:** `templates/skills/skill.md`
- **Official Docs:** https://docs.claude.com/en/docs/claude-code/skills.md
- **Community:** https://github.com/travisvn/awesome-claude-skills

## Best Practices Summary

✅ **Focus** - One clear capability per Skill
✅ **Discover** - Write descriptions for auto-activation
✅ **Guide** - Provide step-by-step instructions
✅ **Exemplify** - Include 2-3 concrete examples
✅ **Practice** - Document domain-specific best practices
✅ **Support** - Add troubleshooting section
✅ **Test** - Verify activation and accuracy
✅ **Share** - Commit to git for team availability
