---
description: "Create a new Claude Code Skill with interactive setup and guidance"
argument-hint: "SKILL-NAME [--scope=personal|project] [--edit]"
allowed-tools: Bash, Read, Write, AskUserQuestion, SlashCommand
---

# Command: Create Skill

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create a new Skill with directory structure, copy template, validate naming, and guide customization.

**Claude Code MUST execute this workflow:**
1. ✓ Validate skill name format (lowercase, hyphens/numbers, max 64 chars)
2. ✓ Determine scope: personal (`~/.claude/skills/`) or project (`./.claude/skills/`)
3. ✓ Create skill directory structure
4. ✓ Copy SKILL.md template from `~/.claude/templates/skills/skill.md`
5. ✓ Display the template content to user
6. ✓ Provide customization guidance with checklist
7. ✓ Suggest next steps for filling in content

**Claude Code MUST NOT:**
- ✗ Automatically fill in frontmatter (user must customize)
- ✗ Edit the skill file without explicit user request
- ✗ Commit to git (that's a user decision)
- ✗ Proceed if skill name is invalid or skill already exists

---

## VALIDATION & PREREQUISITES

**Before executing, Claude Code MUST validate:**

- [ ] Skill name provided and non-empty
- [ ] Skill name matches format: lowercase letters/numbers/hyphens only, max 64 chars
- [ ] Target directory doesn't already exist
- [ ] Template file exists at `~/.claude/templates/skills/skill.md`
- [ ] Write permissions for target location

**If any validation fails:** Stop immediately and report clearly what's wrong.

---

## IMPLEMENTATION FLOW

### Step 1: Validate Skill Name

Parse the argument and validate:
- Must be provided (non-empty)
- Lowercase letters, numbers, hyphens only
- Max 64 characters
- No spaces or special characters

**If invalid**, explain the format rules with examples:
```
Valid names:
  - azure-devops
  - react-patterns
  - json-formatter
  - api-testing-v2

Invalid names:
  - Azure DevOps (spaces, capitals)
  - my_skill (underscore)
  - verylongskillnamethatexceedssixtyfourcharacterslimitwhichisnotallowed (too long)
```

### Step 2: Determine Scope

Ask user where to create the skill:

| Option | Location | Use Case | Default |
|--------|----------|----------|---------|
| **A** | `~/.claude/skills/` | Personal use only | |
| **B** | `./.claude/skills/` | Team-shared via git | ← Recommended if in project |
| **C** | Skip | Cancel operation | |

If already in a project, recommend project scope. Otherwise default to personal.

### Step 3: Create Directory Structure

```bash
mkdir -p [TARGET]/{skill-name}
```

Verify creation succeeded.

### Step 4: Copy Template

```bash
cp ~/.claude/templates/skills/skill.md [TARGET]/{skill-name}/SKILL.md
```

Display success message with path.

### Step 5: Show Customization Checklist

Display the template content with clear guidance on what to customize:

```markdown
✨ Skill Created: [skill-name]

Location: [path]/[skill-name]/SKILL.md

**Next: Customize the template**

Your Skill is ready! Here's what to customize:

1. **Frontmatter** (Lines 2-4)
   - [ ] name: Change to your skill name (already set: [skill-name])
   - [ ] description: Write what this skill does + when to use it
   - [ ] allowed-tools: (Optional) Restrict available tools

2. **Title** (Line 6)
   - [ ] Update to meaningful title (e.g., "Azure DevOps Workflows")

3. **Content Sections** (Keep all sections, customize content)
   - [ ] "When to Use This Skill" - 3-5 trigger scenarios
   - [ ] "Instructions" - Step-by-step process
   - [ ] "Examples" - 2-3 concrete scenarios with input/output
   - [ ] "Best Practices" - 4+ domain-specific practices
   - [ ] "Troubleshooting" - Common issues + solutions

4. **Optional Sections** (Add if relevant)
   - [ ] "Integration Points" - How this connects to other tools
   - [ ] "Key Terminology" - Domain-specific definitions
   - [ ] "Additional Resources" - Links to docs

5. **Test Your Skill**
   - [ ] Ask Claude a question matching your description
   - [ ] Verify Claude activates and uses your skill correctly
```

### Step 6: Show Current Template

Read and display the template with line numbers so user can see structure:

```
File: [path]/[skill-name]/SKILL.md

[Display template content with visual structure]
```

### Step 7: Provide Next Steps

Present actionable next steps in table format:

| Option | Action | Details |
|--------|--------|---------|
| **A** | Open for editing | Use `/claude:guru skills` for guidance on each section |
| **B** | View template guide | Read `docs/user/skills-guide.md` for detailed examples |
| **C** | Start with description | Most important: write discovery-focused description |
| **D** | Review examples | Check `docs/developer/skills-development-guide.md` for patterns |
| **E** | Test skill | Ask Claude a question matching your planned description |
| **F** | Commit to git | `git add ./.claude/skills/[skill-name]/` (if project scope) |

---

## INTERACTIVE PATTERN

### User Feedback Table

When prompting for scope, use decision table:

```markdown
## Where should this Skill live?

| Location | Scope | Best For |
|----------|-------|----------|
| **A** — ~/.claude/skills/ | Personal | Individual workflows, experiments |
| **B** — ./.claude/skills/ | Project | Team-shared expertise, git-tracked |
| **C** — Skip | Cancel | I'll create manually |

**← B Recommended** if you're in a project (auto-shared with team on pull)
```

### Customization Checklist

Display as interactive progress, not just text.

### Next Steps Table

Always include with specific actions and exact command examples.

---

## EXAMPLES

### Example 1: Create Personal Skill

```bash
/skills:create my-workflow

✨ Skill Created: my-workflow

Location: ~/.claude/skills/my-workflow/SKILL.md

The template has been copied with:
  ✓ Frontmatter ready for customization
  ✓ Content sections ready to fill in
  ✓ Examples showing expected format

Next: Edit the file and customize the sections...
```

### Example 2: Create Project Skill

```bash
/skills:create azure-patterns --scope=project

✨ Skill Created: azure-patterns

Location: ./.claude/skills/azure-patterns/SKILL.md

Project scope selected - this skill will be:
  ✓ Shared with team via git
  ✓ Auto-available to teammates on pull
  ✓ Committed to repository

Next: Customize template, test, then commit to git...
```

### Example 3: Invalid Name Handling

```bash
/skills:create My-Awesome Skill

❌ Invalid skill name: "My-Awesome Skill"

Skill names must be:
  ✓ Lowercase letters, numbers, hyphens only
  ✓ No spaces, underscores, or special characters
  ✓ Maximum 64 characters
  ✓ Examples: azure-devops, react-patterns, json-formatter

Try again with a valid name:
  /skills:create my-awesome-skill
```

---

## VALIDATION & ERROR HANDLING

**Invalid Skill Name:**
```
The name must use:
- Lowercase letters (a-z)
- Numbers (0-9)
- Hyphens (-) as separators

Max 64 characters. Examples:
  ✓ azure-devops
  ✓ react-hooks-guide
  ✓ api-testing-v2
  ✗ My Skill (spaces)
  ✗ my_skill (underscore)
```

**Skill Already Exists:**
```
Skill already exists: ./.claude/skills/[name]/SKILL.md

Options:
  - Use a different name: /skills:create [new-name]
  - View existing skill: cat ./.claude/skills/[name]/SKILL.md
  - Modify existing skill: Edit the file manually
```

**Template Not Found:**
```
Template not found: ~/.claude/templates/skills/skill.md

Please ensure the template file exists. It should be at:
  ~/.claude/templates/skills/skill.md

If missing, recreate it from the guide:
  docs/developer/skills-development-guide.md
```

---

## COMMAND BEHAVIOR

### Scope Selection

**Default Logic:**
1. If inside a git project (`.git` exists) → recommend `./.claude/skills/`
2. Otherwise → recommend `~/.claude/skills/`
3. User can override with `--scope=personal|project`

### Template Structure

Copy includes:
- `SKILL.md` with complete structure
- Frontmatter template ready for customization
- All recommended sections with guidance
- No other files (user adds scripts/resources as needed)

### Post-Creation

After creation:
- Display the template
- Show customization checklist
- Provide next steps
- Suggest documentation references

---

## NEXT STEPS TABLE

| Option | Action | Command | Recommended |
|--------|--------|---------|-------------|
| **A** | Customize the Skill | Edit `./.claude/skills/[name]/SKILL.md` manually | ← Start here |
| **B** | View detailed guide | Read `docs/user/skills-guide.md` | For understanding |
| **C** | Review examples | Check `docs/developer/skills-development-guide.md` | For patterns |
| **D** | Test the Skill | Ask Claude a question matching your description | Validate it works |
| **E** | Commit to git | `git add ./.claude/skills/[name]/` (project scope) | To share with team |
| **F** | Create another Skill | `/skills:create [name]` | If ready for more |

**What would you like to do next?**

---

## DOCUMENTATION REFERENCES

- **Quick Reference**: `docs/reference/skills-cheat-sheet.md`
- **User Guide**: `docs/user/skills-guide.md`
- **Developer Guide**: `docs/developer/skills-development-guide.md`
- **Template**: `templates/skills/skill.md`
- **Skills Directory**: `~/.claude/skills/` (personal) or `./.claude/skills/` (project)

---

## RELATED COMMANDS

- **View existing skills**: List `./.claude/skills/` and `~/.claude/skills/`
- **Create slash command**: `/claude:create-command` (different from skills)
- **Test skill**: Ask Claude naturally - no explicit command needed
- **Share skill**: `git commit` from `./.claude/skills/` location
