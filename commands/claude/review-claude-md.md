---
description: "Conduct thorough CLAUDE.md quality review with interactive fix selection to reduce verbosity and improve clarity"
argument-hint: "[--scope=project|user] [--output=file] [--no-interactive]"
allowed-tools: Read, Write, Edit, Grep, Glob, Task, Bash(python:*), Bash(cp:*)
---

# Command: Review CLAUDE.md Quality

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Analyze CLAUDE.md for quality issues and provide prioritized recommendations with optional interactive fix application.

**Claude Code MUST execute this workflow:**
1. ✓ Detect analysis scope (project or user CLAUDE.md)
2. ✓ Invoke docs-analyst for comprehensive quality analysis
3. ✓ Categorize findings by priority (Critical/High/Medium/Low)
4. ✓ Create backup before applying any changes
5. ✓ Present interactive A/B/C/D/Skip options
6. ✓ Apply selected fixes with progress reporting
7. ✓ Display before/after metrics and context file location

**Claude Code MUST NOT:**
- ✗ Skip backup creation
- ✗ Modify files without user choice
- ✗ Leave incomplete file operations

---

## Purpose

Analyze CLAUDE.md files for documentation drift, verbosity, consistency, and quality issues, providing prioritized recommendations to improve clarity and reduce bloat.

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| A | Default workflow | [RECOMMENDED] |
| B | Alternative approach | For different use case |
| C | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output | Check generated content |
| 2 | Iterate or refine | Run command again [RECOMMENDED] |
| 3 | Continue workflow | Proceed to next step |
| 4 | Get help | Use /claude:guru for guidance |

What would you like to do next?


## Usage

```
/system:claude-review [--scope=project|user] [--output=file]
```

**Arguments**:

- `--scope=project` (default): Review project CLAUDE.md (`.claude/CLAUDE.md`)
- `--scope=user`: Review user CLAUDE.md (`~/CLAUDE.md`)
- `--output=file`: Save recommendations to specified file path (optional)
- `--no-interactive`: Skip interactive fix selection, only show recommendations

**Examples**:

- `/system:claude-review` - Review project CLAUDE.md with interactive fix selection (default)
- `/system:claude-review --scope=user` - Review user CLAUDE.md with interactive selection
- `/system:claude-review --no-interactive` - Analysis only, no fix application
- `/system:claude-review --output=.agent/claude-review.md` - Save detailed recommendations to file

## Process

1. **Scope Detection**
   - Default to project CLAUDE.md (`.claude/CLAUDE.md`)
   - If `--scope=user`, review `~/CLAUDE.md` instead
   - Verify file exists before proceeding

2. **Documentation Quality Analysis (Anthropic Best Practices)**
   - Invoke docs-analyst for comprehensive CLAUDE.md analysis
   - **Token Budget**: Estimate token usage (word count × 1.3), target <2000 tokens
   - **AI-First Writing**: Check for narrative paragraphs vs declarative bullets
   - **Documentation Drift**: Detect hard-coded counts, percentages, timings, statistics
   - **Structural Clarity**: Verify Markdown heading hierarchy and section organization
   - **Redundancy**: Identify repeated information and obvious explanations
   - **Necessity**: Ensure every line serves Claude's work (no commentary)
   - **Consistency**: Validate template alignment, naming conventions, cross-references
   - **Completeness**: Check for critical commands, constraints, and workflows

3. **Anti-Drift Validation**
   - Hard-coded counts ("43 agents", "15 commands")
   - Percentage statistics ("32% reduction")
   - Performance timings ("3-5min", "75-85% faster")
   - Timeline estimates ("first week", "1-3 months")
   - Token burn percentages ("90%+ tokens")

4. **Recommendation Generation**
   - Organize findings by priority (Critical, High, Medium, Low)
   - Provide specific, actionable fix recommendations
   - Suggest structural improvements
   - Identify redundant sections for removal
   - Propose clarity improvements

5. **Interactive Fix Selection** (unless `--no-interactive`)
   - Present summary of all recommendations grouped by priority
   - Show estimated impact for each priority level
   - Present options using standard A/B/C/D table format:

   | Option | Description | Impact |
   |--------|-------------|--------|
   | A | Critical fixes only | Highest priority issues |
   | B | Critical + High fixes | Recommended for most cases |
   | C | Critical + High + Medium | Comprehensive improvement |
   | D | All fixes (including Low) | Complete optimization |
   | Skip | Exit without changes | No modifications |

   - Validate user input (A/B/C/D/Skip, case-insensitive)
   - Create backup: `{CLAUDE.md}.backup-{timestamp}` before applying

6. **Apply Selected Fixes**
   - Apply fixes in order (Critical → High → Medium → Low)
   - Show progress: "Applying fix 3 of 8..."
   - Handle errors gracefully (restore from backup if needed)
   - Display summary: "Applied 5 fixes, skipped 3, token reduction: 28%"

7. **Output Delivery**
   - Present concise summary to user
   - Show before/after metrics (token count, issue count)
   - If `--output` specified, save detailed findings to file
   - Reference context file: `.agent/Session-{name}/context/docs-analyst.md`

## Interactive Selection Format

Uses standard A/B/C/D table format for clarity and consistency:

**Input Options:**

- `A` - Apply critical priority fixes only
- `B` - Apply critical + high priority fixes (recommended)
- `C` - Apply critical + high + medium priority fixes
- `D` - Apply all fixes (critical + high + medium + low)
- `Skip` - Exit without applying any changes

**Input Validation:**

- Case-insensitive (a, A, b, B, etc. all work)
- Invalid input re-prompts once, then defaults to Skip
- Ctrl+C to exit at any time

**Why A/B/C/D Format:**

- Cleaner, more scannable than numbered lists
- Letter-based options more intuitive than complex syntax
- Consistent with speckit command patterns
- Table format groups related options visually
- Maximum 5 options keeps choices focused

## Agent Integration

- **Primary Agent**: docs-analyst - Conducts comprehensive CLAUDE.md quality analysis
- **Analysis Focus** (Anthropic Best Practices Compliance):
  - **Token Budget**: Rough token estimate, identify bloat (target <2000 tokens)
  - **AI-First Writing**: Detect narrative prose vs declarative bullets
  - **Documentation Drift**: Find hard-coded counts, percentages, timings
  - **Structural Clarity**: Check Markdown hierarchy and section organization
  - **Redundancy Elimination**: Identify repeated or obvious explanations
  - **Necessity Focus**: Flag commentary, nice-to-have, non-essential info
  - **Consistency Validation**: Verify template alignment, naming, cross-references
  - **Completeness**: Check for missing commands, terminology, workflows
- **Coordination**: Docs-analyst persists findings to `.agent/Session-{name}/context/docs-analyst.md`, returns concise summary with recommendation counts by priority (Critical/High/Medium/Low)

**Coordination Pattern**:

- Command has full main thread access (unrestricted)
- Spawns docs-analyst for CLAUDE.md analysis
- Agent provides advisory recommendations (not direct execution)
- User decides which recommendations to implement

## Examples

### Example 1: Interactive Review with Fix Selection (Default)

```
/system:claude-review

# Expected behavior:
→ Reads .claude/CLAUDE.md
→ Invokes docs-analyst for Anthropic best practices analysis
→ Token Budget: 3,200 tokens (target: 2,000)

## Analysis Results

**Critical Issues (3):**
- Line 43: Hard-coded count "43 agents" → "Multiple domain analysts"
- Line 89: Hard-coded count "15 commands" → "Comprehensive command library"
- Line 134: Performance claim "75-85% faster" → "Significantly faster"

**High Priority (7):**
- Lines 45-52: Narrative paragraph → Convert to bullets
- Lines 78-85: Narrative paragraph → Convert to bullets
- Lines 134-140: Duplicate MCP tools section → Consolidate
- Lines 160-165: Narrative paragraph → Convert to bullets
- Lines 201-205: Narrative paragraph → Convert to bullets
- Lines 225-230: Redundant section → Remove
- Lines 245-250: Obvious explanation → Remove

**Medium Priority (4):**
- Line 67: Add missing command "npm run test"
- Line 68: Add missing command "npm run build"
- Lines 112-115: Redundant explanation → Remove
- Lines 189-192: Template duplication → Remove

**Low Priority (2):**
- Line 99: Define project-specific term "speckit"
- Line 156: Define project-specific term "context elision"

**Estimated Impact:**
- Token reduction: ~1,000 tokens (31% reduction)
- Issues: 3 critical, 7 high, 4 medium, 2 low

## How would you like to proceed?

| Option | Description | Impact |
|--------|-------------|--------|
| A | Critical fixes only | 3 fixes, ~200 tokens saved |
| B | Critical + High (recommended) | 10 fixes, ~800 tokens saved |
| C | Critical + High + Medium | 14 fixes, ~950 tokens saved |
| D | All fixes | 16 fixes, ~1,000 tokens saved |
| Skip | Exit without changes | No modifications |

Your choice: _

→ User enters: B
→ Validated: Applying Critical + High priority fixes
→ Creating backup: .claude/CLAUDE.md.backup-20250114-143022
→ Applying 10 fixes (3 critical + 7 high)...
  [1/10] Fixing line 43: Hard-coded count → Qualitative description ✓
  [2/10] Fixing line 89: Hard-coded count → Qualitative description ✓
  [3/10] Fixing line 134: Performance claim → Qualitative description ✓
  [4/10] Converting lines 45-52 to bullets ✓
  [5/10] Converting lines 78-85 to bullets ✓
  [6/10] Consolidating MCP sections ✓
  [7/10] Converting lines 160-165 to bullets ✓
  [8/10] Converting lines 201-205 to bullets ✓
  [9/10] Removing redundant section (lines 225-230) ✓
  [10/10] Removing obvious explanation (lines 245-250) ✓

## Results

✅ Applied 10 fixes successfully
📊 Before: 3,200 tokens, 16 issues
📊 After: 2,380 tokens, 6 issues (4 medium + 2 low)
💾 Backup saved: .claude/CLAUDE.md.backup-20250114-143022
📁 Context: .agent/Session-{name}/context/docs-analyst.md

Remaining issues: 4 medium + 2 low priority (run command again to address)
```

### Example 2: Analysis Only (No Interactive Mode)

```
/system:claude-review --no-interactive

# Expected behavior:
→ Reads .claude/CLAUDE.md
→ Invokes docs-analyst for analysis
→ Presents all recommendations with priorities
→ Saves to .agent/Session-{name}/context/docs-analyst.md
→ Exits without prompting for fixes (user applies manually)

Use case: When you want to review findings before deciding
```

### Example 3: User CLAUDE.md Review with Output File

```
/system:claude-review --scope=user --output=.agent/user-claude-review.md

# Expected behavior:
→ Reads ~/CLAUDE.md
→ Invokes docs-analyst for global patterns analysis
→ Presents A/B/C/D selection table
→ User enters: C (critical + high + medium)
→ Applies 14 selected fixes to ~/CLAUDE.md
→ Saves detailed recommendations to .agent/user-claude-review.md
```

## Official CLAUDE.md Best Practices

### Core Principles (Anthropic Guidelines)

**1. Token Budget Awareness**

- CLAUDE.md contents are prepended to EVERY prompt
- Bloated files increase costs and introduce noise
- Keep it lean: only include what Claude needs to work
- Target: Scannable in <30 seconds

**2. Write for AI, Not Humans**

- Use short, declarative bullet points
- Avoid narrative paragraphs and lengthy explanations
- Example: ❌ "This folder contains all the React components we use" → ✅ "Components: React UI elements"

**3. Living Document Approach**

- Treat as iterative, not final
- Add instruction → Test → Observe → Refine
- Update frequently based on what works
- Use emphasis ("IMPORTANT", "YOU MUST") for critical rules

**4. Structure with Clarity**

- Use standard Markdown headings (#, ##)
- Logical sections: Tech Stack, Commands, Code Style, Testing
- Trim redundancy (don't explain obvious folder names)
- Focus on necessity over comprehensiveness

**5. Hierarchical Organization**

- Root: Project-wide conventions
- Child directories: Context-specific rules
- Home (~/.claude/CLAUDE.md): Universal patterns
- Claude prioritizes most specific (nested) when relevant

### Recommended Content

**Include**:

- Common bash commands with descriptions
- Core files and utility functions
- Code style guidelines (specific, enforceable)
- Testing requirements and commands
- Repository etiquette and workflows
- Unexpected project behaviors or gotchas
- Project-specific terminology and jargon
- Environment setup commands

**Exclude**:

- Commentary or nice-to-have information
- Verbose explanations of obvious things
- Hard-coded counts, percentages, timings
- Timeline estimates or performance claims
- Redundant information covered by templates

### Structure Template

```markdown
# Project Name

## Bash Commands
- command: Description

## Tech Stack
- Technology: Purpose

## Code Style
- Rule (specific, testable)

## Testing
- When to test
- How to run tests

## Workflow
- Step-by-step for common tasks

## Do Not Touch
- Files/directories to avoid
```

## Safety Features

**Automatic Backups:**

- Before applying ANY changes, creates backup: `{CLAUDE.md}.backup-{timestamp}`
- Example: `.claude/CLAUDE.md.backup-20250114-143022`
- User can restore manually if needed: `cp .claude/CLAUDE.md.backup-* .claude/CLAUDE.md`

**Error Handling:**

- If any fix fails, automatically restores from backup
- Shows clear error message with which fix failed
- User can retry individual fix or skip problematic ones

**Progressive Application:**

- Fixes applied one at a time with progress indicator
- User can Ctrl+C to stop at any point (partial changes are kept)
- Before/after metrics shown after all fixes applied

**Validation:**

- After fixes, shows token count reduction
- Displays remaining issues for future review
- Suggests re-running command if more optimization possible

## Quality Standards

- **Anti-Drift Compliance**: No hard-coded counts, percentages, timings, or statistics
- **Token Budget Respect**: Concise, scannable, only necessary information
- **Clarity Over Completeness**: Prefer brief bullet points over narrative explanations
- **Structural Consistency**: Follow standard Markdown heading hierarchy
- **Actionable Output**: Every recommendation must be specific and implementable
- **Priority Validation**: Critical issues must pose actual maintenance or clarity risks
- **AI-First Writing**: Short declarative statements, no human-centric prose

## Review Dimensions

**1. Token Budget Efficiency**

- **Check**: Estimate token usage (rough word count × 1.3)
- **Anti-Pattern**: Files >3000 tokens consuming excessive budget
- **Best Practice**: Target <2000 tokens for most projects
- **Recommendation**: Identify sections to trim, consolidate, or remove

**2. AI-First Writing Style**

- **Check**: Paragraph length, narrative vs bullet points
- **Anti-Pattern**: Long paragraphs explaining concepts vs declarative statements
- **Example**: ❌ "In this project, we use TypeScript because..." → ✅ "TypeScript: Type-safe JavaScript"
- **Recommendation**: Convert prose to bullets, remove human-centric explanations

**3. Documentation Drift Detection**

- **Check**: Hard-coded counts, percentages, timings, statistics
- **Anti-Pattern**: "43 agents", "75-85% faster", "3-5min", "first week"
- **Best Practice**: Use qualitative descriptions ("multiple", "significantly faster")
- **Recommendation**: Replace specific metrics with relative descriptions

**4. Structural Clarity**

- **Check**: Markdown heading hierarchy (#, ##), section organization
- **Anti-Pattern**: No headings, flat structure, unclear sections
- **Best Practice**: Logical sections (Tech Stack, Commands, Code Style, Testing, Workflow)
- **Recommendation**: Reorganize with standard Markdown structure

**5. Redundancy Elimination**

- **Check**: Repeated information, obvious explanations
- **Anti-Pattern**: "components folder contains components", template duplication
- **Best Practice**: If folder name is self-explanatory, omit explanation
- **Recommendation**: Remove redundant sections, consolidate duplicates

**6. Necessity Focus**

- **Check**: Every line serves Claude's work
- **Anti-Pattern**: Commentary, nice-to-have info, philosophical explanations
- **Best Practice**: Only include what Claude needs to execute tasks
- **Recommendation**: Remove non-essential information

**7. Consistency Validation**

- **Check**: Template alignment, naming conventions, cross-references
- **Anti-Pattern**: Outdated agent names, incorrect command references
- **Best Practice**: Accurate references to current system state
- **Recommendation**: Update stale references, fix naming inconsistencies

**8. Completeness Assessment**

- **Check**: Critical commands, key constraints, essential workflows
- **Anti-Pattern**: Missing bash commands, undefined terminology, unclear testing requirements
- **Best Practice**: Include common commands, project jargon, gotchas
- **Recommendation**: Add missing essential information

## Integration Points

- **Follows**: `/claude:create-agent`, `/claude:create-command` (after creating new artifacts)
- **Followed by**: Manual CLAUDE.md editing based on recommendations
- **Related**:
  - `/docs:changelog` - Documentation consistency
  - `/system:guru` - Context-aware guidance system
  - `/docs:sync` - Comprehensive documentation workflow

## Output

- **User Summary**: Concise findings with recommendation counts by priority
- **Context File**: `.agent/Session-{name}/context/docs-analyst.md` with detailed analysis
- **Optional File**: Detailed recommendations saved to specified path if `--output` provided
- **Actionable Format**: Each recommendation includes:
  - Priority level (Critical/High/Medium/Low)
  - Specific issue location (section, line reference)
  - Concrete fix suggestion
  - Rationale for change
