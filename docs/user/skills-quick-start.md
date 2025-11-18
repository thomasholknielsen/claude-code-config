# Skills Quick Start Guide

Get up and running with Claude Code Skills in 5 minutes.

## What Are Skills?

Skills are **expert modules** that Claude automatically activates when relevant to your request.

```
You: "Help me set up an Azure pipeline"
    ↓
Claude detects: "This matches the azure-devops Skill description"
    ↓
Claude activates Skill automatically
    ↓
You get expert guidance on pipeline setup
```

**Key difference from Slash Commands:**
- Commands: You invoke explicitly with `/command-name`
- Skills: Claude detects and activates automatically

## Existing Skills

### azure-devops
Expert guidance on Azure DevOps workflows, pipelines, work items, CI/CD.

**Try it:** Ask Claude: "Help me set up a CI/CD pipeline"

### json-formatter
Formats and validates JSON data.

**Try it:** Ask Claude: "Format this JSON for me"

## Create Your First Skill

### Option 1: Quick Create (Recommended)

```bash
/skills:create my-skill
```

This command:
- ✅ Creates directory
- ✅ Copies template
- ✅ Shows customization checklist
- ✅ Guides next steps

### Option 2: Manual

```bash
mkdir -p ./.claude/skills/my-skill
cp ~/.claude/templates/skills/skill.md ./.claude/skills/my-skill/SKILL.md
# Then edit the file
```

## Customize Your Skill

Edit `./.claude/skills/my-skill/SKILL.md` and fill in:

### 1. Frontmatter (Top of file)
```yaml
---
name: my-skill              # Change this
description: "What this does and when to use it"  # Critical!
---
```

**The description is crucial** - Claude uses it to decide when to activate your Skill. Make it specific:

❌ "A skill for working with data"
✅ "Formats and validates JSON data. Use when you need to pretty-print JSON, fix formatting issues, or validate JSON syntax."

### 2. Main Sections (Edit the content)

```markdown
## When to Use This Skill
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

## Instructions
1. Step 1
2. Step 2
3. Step 3

## Examples
### Example 1
[Show input, process, output]

## Best Practices
- Practice 1
- Practice 2
- Practice 3

## Troubleshooting
[Common issues + solutions]
```

## Test Your Skill

Ask Claude a question matching your skill's description:

```
"Help me [what your skill does]"
"How do I [use case from your description]?"
```

If Claude activates your Skill, you're good!

If not, refine the **description** - it needs better keywords.

## Share With Team

If you created it in `./.claude/skills/` (project scope):

```bash
git add ./.claude/skills/my-skill/
git commit -m "feat: add my-skill for [purpose]"
git push
```

Team members get it automatically on pull.

## Common Skill Ideas

### By Domain

**Web Development:**
- React patterns
- API testing
- Frontend accessibility
- Web performance optimization

**Backend:**
- Database optimization
- API design
- Authentication patterns
- Caching strategies

**DevOps:**
- Pipeline configuration
- Infrastructure as code
- Monitoring setup
- Deployment strategies

**Project Management:**
- Agile ceremonies
- Documentation standards
- Code review guidelines
- Release procedures

## Naming Your Skill

**Rules:**
- Lowercase letters, numbers, hyphens only
- Maximum 64 characters
- No spaces or special characters

**Good names:**
- azure-devops
- react-patterns
- json-formatter
- api-testing-guide

**Bad names:**
- My Awesome Skill (spaces)
- react_patterns (underscore)
- APITesting (capitals)

## File Structure

After creating, your Skill looks like:

```
./.claude/skills/my-skill/
├── SKILL.md              # Main file (required)
├── scripts/              # Optional: code files
│   └── helper.py
└── resources/            # Optional: templates, configs
    └── templates/
```

For most Skills, just `SKILL.md` is enough.

## Next Steps

| What | How |
|------|-----|
| **Create Skill** | `/skills:create [name]` |
| **Learn More** | Read `docs/user/skills-guide.md` |
| **See Examples** | Check `./.claude/skills/` |
| **Understand Details** | Read `docs/developer/skills-development-guide.md` |
| **Quick Reference** | See `docs/reference/skills-cheat-sheet.md` |

## Checklist: Before Sharing

- [ ] Name is valid (lowercase, hyphens, max 64 chars)
- [ ] Description is clear and discoverable (includes keywords + use cases)
- [ ] Instructions are step-by-step
- [ ] Examples are concrete (input → output)
- [ ] Best practices documented (4+)
- [ ] Troubleshooting included
- [ ] Tested with Claude (ask a matching question)
- [ ] Ready to commit: `git add ./.claude/skills/[name]/`

## Troubleshooting

**Skill not activating?**
→ Refine the description to include more keywords

**Claude not following instructions?**
→ Simplify steps, add more examples

**Still confused?**
→ Check the full guide: `docs/user/skills-guide.md`

## Key Takeaways

1. **Create**: `/skills:create my-skill`
2. **Customize**: Edit SKILL.md (description + sections)
3. **Test**: Ask Claude a matching question
4. **Share**: `git commit` from `./.claude/skills/`
5. **Iterate**: Improve based on feedback

---

**Now create your first Skill!**

```bash
/skills:create my-first-skill
```

Or dive deeper: `docs/user/skills-guide.md`
