# Claude Code Skills Guide

## What Are Skills?

**Skills are model-invoked capabilities** that extend Claude Code's functionality. Unlike slash commands (which you explicitly invoke), **Claude automatically activates Skills based on your requests and the Skill's description**.

Think of Skills as specialized knowledge modules that Claude can access when they're relevant to your task. They're stored as simple Markdown files with YAML metadata and load on-demand to keep Claude responsive.

## Key Differences: Skills vs Slash Commands

| Aspect | Skills | Slash Commands |
|--------|--------|-----------------|
| **Invocation** | Automatic (model-invoked) | Manual (user-invoked) |
| **Discovery** | Based on description match | Explicit: `/command-name` |
| **Use Case** | Specialized expertise, complex workflows | Quick utilities, single-purpose tasks |
| **Overhead** | Minimal until activated (30-50 tokens) | Always active |
| **Sharing** | Git-tracked for team availability | Centralized in `.claude/commands/` |

## Skill Storage Locations

### Personal Skills (~/.claude/skills/)
- Individual use only
- Not shared with others
- Ideal for experimental or personal workflows
- Example: `~/.claude/skills/my-workflow-skill/`

### Project Skills (./.claude/skills/)
- Shared with team automatically via git
- Checked into repository
- Available to all team members on pull
- Example: `./.claude/skills/azure-devops/`

### Plugin Skills
- Bundled capabilities from installed plugins
- Distributed as packages
- Recommended for public distribution

## Anatomy of a Skill

Every Skill requires a `SKILL.md` file with this structure:

```
my-skill/
├── SKILL.md              # Main file (REQUIRED)
├── scripts/              # Optional: executable files
│   ├── helper.py
│   └── validator.js
└── resources/            # Optional: static assets
    ├── templates/
    └── configs/
```

### SKILL.md Structure

```yaml
---
name: skill-name
description: "What it does and when to use it (critical for discovery)"
allowed-tools: Read, Grep, Glob  # Optional: restrict tools
---

# Skill Title

## Instructions
[Step-by-step guidance]

## Examples
[Concrete scenarios and outputs]

## Best Practices
[Domain-specific guidance]
```

## Creating a Skill: Step by Step

### Step 1: Plan Your Skill

Ask yourself:
- **What is the single focused capability?** (Not too broad)
- **When should Claude use this?** (Trigger scenarios)
- **What guidance does Claude need?** (Instructions)
- **What examples help?** (Concrete scenarios)

### Step 2: Create the Directory

**For personal use:**
```bash
mkdir -p ~/.claude/skills/my-skill-name
```

**For project/team use:**
```bash
mkdir -p ./.claude/skills/my-skill-name
```

### Step 3: Write SKILL.md

Use the template at `~/.claude/templates/skills/skill.md`:

```bash
cp ~/.claude/templates/skills/skill.md ./.claude/skills/my-skill/SKILL.md
```

Then customize:
1. Fill in `name` (lowercase, hyphens only, max 64 chars)
2. Write discovery-focused `description` (max 1024 chars)
3. Add clear `Instructions`
4. Include 2-3 concrete `Examples`
5. Document `Best Practices`

### Step 4: Test the Skill

Ask Claude questions that match your Skill's description:

```
"Help me with [topic described in skill]"
"How do I [workflow your skill covers]?"
"I need to [use case from your skill description]"
```

Claude should automatically recognize and use the Skill.

### Step 5: Iterate & Refine

- Does Claude understand when to use it?
- Are instructions clear enough?
- Do examples cover common scenarios?
- Is the description discoverable?

## Best Practices for Skill Creation

### 1. Write for Discovery

Your `description` is critical—Claude uses it to decide if your Skill is relevant.

**❌ Poor description:**
```yaml
description: "A skill for working with data"
```

**✅ Great description:**
```yaml
description: "Formats and validates JSON data. Use when you need to pretty-print JSON, fix formatting issues, or validate JSON syntax."
```

**Why?** The good version:
- Specifies exact functionality
- Lists specific use cases
- Includes keywords Claude recognizes
- Tells you exactly when it applies

### 2. Keep Skills Focused

One skill = one clear capability. Don't create sprawling skills that do everything.

**❌ Too broad:**
```yaml
name: development-helper
description: "Helps with development tasks like testing, debugging, deployment, configuration..."
```

**✅ Appropriately scoped:**
```yaml
name: pytest-testing
description: "Helps write, organize, and debug Python pytest tests..."
```

### 3. Include Progressive Examples

Start simple, build to complex:

```markdown
### Example 1: Basic Usage
[Simple, immediate use case]

### Example 2: Adding Features
[Intermediate workflow]

### Example 3: Advanced Patterns
[Complex or sophisticated usage]
```

### 4. Provide Step-by-Step Instructions

Break down the process into clear, sequential steps:

```markdown
## Instructions

1. Identify the [specific thing]
2. Check [validation or prerequisites]
3. Apply [core technique]
4. Validate [output or results]
```

### 5. Document Assumptions & Prerequisites

What does Claude need to know before using this Skill?

```markdown
## Prerequisites

- Assumes [X technology] is installed
- Requires [permission/access] to [resource]
- Works best with [specific context]
```

### 6. Use Tool Restrictions (When Appropriate)

If your Skill should only use certain tools:

```yaml
allowed-tools: Read, Grep, Glob
```

This prevents Claude from using tools it shouldn't, adding a safety layer for read-only or sensitive operations.

## Advanced Features

### Supporting Scripts

For complex operations, add executable scripts:

```
my-skill/
├── SKILL.md
└── scripts/
    ├── validator.py
    └── transformer.js
```

Reference them in your instructions:

```markdown
## Instructions

The skill uses `scripts/validator.py` to:
1. Parse input data
2. Apply validation rules
3. Generate report
```

### Resource Files

Include templates, configurations, or reference materials:

```
my-skill/
├── SKILL.md
└── resources/
    ├── templates/
    │   ├── report-template.md
    │   └── config-template.yml
    └── reference/
        └── terminology.md
```

Reference in your skill:

```markdown
## Templates

See `resources/templates/report-template.md` for the structure.
```

### Versioning & History

Track changes as you improve your Skill:

```markdown
## Version History

**v1.2** (2025-01-15)
- Added support for async workflows
- Improved error detection
- Added examples for edge cases

**v1.1** (2025-01-10)
- Initial release
```

## Real-World Examples

### Example 1: Document Processing Skill

**Use Case:** Handling DOCX/PDF files with advanced operations

```yaml
name: document-processor
description: "Processes Word, PDF, and PowerPoint documents with format conversion, metadata extraction, and batch operations. Use when working with complex document automation, content extraction, or format conversions."
```

**Value:** Replaces manual document manipulation, enables batch processing.

### Example 2: Web Testing Skill

**Use Case:** Automated browser testing with Playwright

```yaml
name: webapp-testing
description: "Tests web applications using Playwright with screenshot capture, form interaction, and accessibility validation. Use when testing frontend applications, validating user flows, or checking accessibility compliance."
```

**Value:** Automates QA tasks, catches regressions early.

### Example 3: Code Pattern Skill

**Use Case:** React patterns and best practices

```yaml
name: react-patterns
description: "Provides expert guidance on React component patterns, hooks, state management, and performance optimization. Use when building React components, implementing state management, or optimizing performance."
```

**Value:** Ensures consistent, idiomatic React code.

## Sharing Skills

### Project Skills (Recommended)

Store in `./.claude/skills/` and commit to git:

```bash
git add ./.claude/skills/my-skill/
git commit -m "feat: add new skill for X functionality"
```

Team members automatically get the Skill on pull.

### Plugin Distribution (Advanced)

For public consumption, package as a Claude Code Plugin.

## Debugging Skills

### Skill Not Being Triggered?

1. **Check the description:** Does it match your request?
   ```bash
   # Read your Skill's frontmatter
   grep "^description:" ./.claude/skills/my-skill/SKILL.md
   ```

2. **Verify the file structure:**
   ```bash
   ls -la ./.claude/skills/my-skill/
   # Should show: SKILL.md
   ```

3. **Check YAML syntax:**
   ```bash
   # Frontmatter must be valid YAML
   head -5 ./.claude/skills/my-skill/SKILL.md
   ```

4. **Test with explicit keywords:** Ask a question that clearly matches your description.

### Claude Ignoring Instructions?

- Rewrite instructions with more specific, actionable steps
- Add more concrete examples
- Break down complex processes into simpler steps
- Test with simpler questions first

## Integration with Other Claude Code Features

### Skills + Commands

Skills provide expertise; Commands orchestrate workflows.

```
User Request
  ↓
  → Relevant Skill(s) activated automatically
  ↓
  → Command may invoke Skill for specific expertise
```

### Skills + Agents

Use Skills for declarative guidance; delegate complex analysis to Agents via Task tool.

### Skills + MCP Tools

Skills can guide Claude on when/how to use MCP tools (Context7, Playwright, etc.), but don't invoke them directly.

## Performance Considerations

- **Initial overhead:** 30-50 tokens to load a Skill
- **Activation:** Only when description matches request
- **No performance penalty** for unused Skills
- **Context efficiency:** Skills keep Claude responsive by deferring loading

## Security & Safety

### Trust & Permissions

- Only use Skills from trusted sources
- Project Skills are reviewed in code review
- Personal Skills affect only your sessions

### Tool Restrictions

Limit available tools for safety:

```yaml
allowed-tools: Read, Grep, Glob
# Prevents execution of dangerous operations
```

## FAQ

**Q: How many Skills should I create?**
A: Create Skills for specialized expertise areas. Start with 2-3, grow as you identify patterns.

**Q: Can Skills execute code?**
A: Skills can reference executable scripts in `scripts/` directory. Claude decides whether to invoke them.

**Q: How do I know if my Skill is good?**
A: Test it! Ask Claude questions matching your description. If Claude uses it correctly, it's working.

**Q: Can I use Skills with slash commands?**
A: Yes. Commands often leverage Skills for expertise. They work together naturally.

**Q: What if my Skill is too specialized?**
A: That's fine! Specialized Skills for niche use cases are valuable. Keep scope focused.

**Q: How do I share Skills with my team?**
A: Commit to `./.claude/skills/` in your repository. Team gets them on pull.

## Next Steps

1. **Review existing Skills** in `~/.claude/skills/` and `./.claude/skills/`
2. **Plan your Skill:** What focused capability would help you most?
3. **Use the template:** `cp ~/.claude/templates/skills/skill.md ./.claude/skills/my-skill/SKILL.md`
4. **Customize:** Fill in your specific guidance
5. **Test:** Ask Claude a relevant question
6. **Iterate:** Refine based on how Claude responds

## Additional Resources

- **Official Documentation:** [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills.md)
- **Awesome Claude Skills:** [Community Repository](https://github.com/travisvn/awesome-claude-skills)
- **Skills Template:** `~/.claude/templates/skills/skill.md`
- **Real Examples:** Existing project Skills in `./.claude/skills/`
