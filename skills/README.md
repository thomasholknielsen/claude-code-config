# Claude Code Skills

This directory contains **Skills** - model-invoked expertise modules that Claude automatically activates when relevant to your requests.

## About Skills

**Skills differ from Slash Commands:**

| Aspect | Skills | Slash Commands |
|--------|--------|-----------------|
| **How triggered** | Automatic (Claude decides) | Manual: `/command-name` |
| **When to use** | Specialized expertise | Quick utilities & workflows |
| **Discovery** | Description matching | Explicit invocation |
| **Overhead** | Minimal (loaded on-demand) | Always active |

## Available Skills

### azure-devops
Provides expert guidance on Azure DevOps workflows including:
- Work item management (Epics, Features, User Stories)
- Repository and branch management
- Pull request workflows
- CI/CD pipelines and automation
- Test management

**When to use:** Setting up Azure DevOps projects, configuring pipelines, managing work items, integrating CI/CD workflows.

**Location:** `./azure-devops/`

### json-formatter
Formats and validates JSON data:
- Pretty-printing minified JSON
- JSON syntax validation
- Error identification and fixing
- Consistent 2-space indentation

**When to use:** Need to format JSON, fix formatting issues, or validate JSON syntax.

**Location:** `./json-formatter/`

## Using a Skill

Simply ask Claude a question matching the Skill's description. Claude will automatically activate the relevant Skill:

```
# These activate the azure-devops Skill:
"Help me set up a CI/CD pipeline in Azure DevOps"
"How do I configure branch policies?"
"Create a work item for this feature"

# These activate the json-formatter Skill:
"Can you format this JSON?"
"Is this valid JSON?"
"Clean up this minified JSON response"
```

No explicit invocation needed—Claude detects relevance automatically.

## Creating a New Skill

### Quick Start

1. **Use the template:**
   ```bash
   cp ~/.claude/templates/skills/skill.md ./.claude/skills/my-skill/SKILL.md
   ```

2. **Customize frontmatter:**
   ```yaml
   ---
   name: my-skill
   description: "Clear explanation of what this does and when to use it"
   ---
   ```

3. **Add content:**
   - Instructions (step-by-step)
   - Examples (2-3 scenarios)
   - Best practices
   - Troubleshooting

4. **Test:**
   Ask Claude a question matching your description. If Claude uses the Skill correctly, you're done!

### Key Tips

- **Description matters**: Include keywords Claude will recognize and scenarios for triggering
- **Keep it focused**: One clear capability per Skill
- **Show examples**: Include concrete scenarios with inputs and outputs
- **Step by step**: Break processes into sequential, actionable steps
- **Provide practices**: Document domain-specific best practices

### Directory Structure

```
my-skill/
├── SKILL.md              # Main file (REQUIRED)
├── scripts/              # Optional: helper code
│   └── validator.py
└── resources/            # Optional: templates, configs
    ├── templates/
    └── reference/
```

## Documentation

- **User Guide**: Read `docs/user/skills-guide.md` to understand how Skills work and how to use them effectively
- **Developer Guide**: See `docs/developer/skills-development-guide.md` for detailed skill creation guidelines
- **Template**: Check `templates/skills/skill.md` for the standard skill structure

## Best Practices

### Writing Skills
✅ Focus on one capability
✅ Write discoverable descriptions
✅ Include progressive examples
✅ Provide clear instructions
✅ Document best practices
✅ Add troubleshooting section

### Using Skills
✅ Use natural language requests
✅ Include context about what you're doing
✅ Test with varied phrasing
✅ Provide feedback if activation seems off

## Skill Activation Troubleshooting

**Skill not activating?**

1. Check the description includes relevant keywords
2. Ask with different phrasing that matches the description
3. Verify YAML syntax in frontmatter (test with simple questions first)
4. Review instruction clarity

**Claude misunderstanding the Skill?**

1. Add more concrete examples
2. Simplify step-by-step instructions
3. Use consistent terminology
4. Add explicit decision trees

## Tool Restrictions

Some Skills may use `allowed-tools` to restrict available capabilities:

```yaml
allowed-tools: Read, Grep, Glob
```

This prevents certain operations, adding safety for read-only or sensitive workflows.

## Sharing Skills

### Team Distribution

**Project Skills** are automatically shared:

1. Create Skill in `./.claude/skills/` (NOT `~/.claude/skills/`)
2. Commit to git:
   ```bash
   git add ./.claude/skills/my-skill/
   git commit -m "feat: add my-skill for [purpose]"
   ```
3. Team members get it on pull—no additional setup needed

### Personal Skills

Keep experimental or personal Skills in `~/.claude/skills/`. They're for your use only.

## Real-World Examples

### Example 1: Configure Azure Pipeline

```
You: "Help me set up a YAML pipeline for our .NET project"

→ azure-devops Skill activates
→ Claude provides step-by-step YAML configuration
→ Includes examples for build, test, deploy stages
→ Suggests best practices for CI/CD
```

### Example 2: Fix JSON Format

```
You: "Format this JSON response from the API"

→ json-formatter Skill activates
→ Claude pretty-prints the data
→ Validates syntax
→ Shows any errors found
```

## Next Steps

1. **Explore existing Skills** - Try asking Claude about Azure DevOps or JSON formatting
2. **Create your first Skill** - Use the template to build domain expertise
3. **Read the guides** - Check `docs/user/skills-guide.md` and `docs/developer/skills-development-guide.md`
4. **Share with your team** - Commit to `./.claude/skills/` for automatic distribution

## References

- **Official Docs**: https://docs.claude.com/en/docs/claude-code/skills.md
- **Awesome Claude Skills**: https://github.com/travisvn/awesome-claude-skills
- **CLAUDE.md**: Project configuration and system architecture
