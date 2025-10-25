---
description: "Analyze and synchronize documentation to match codebase changes"
argument-hint: "[--scope=changes|project]"
allowed-tools: Task, Bash, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch
---

# Command: Sync Documentation

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Analyze documentation state, detect needed updates, and synchronize docs with codebase

**Claude Code MUST execute this workflow:**
1. ✓ Detect scope (--scope=changes for uncommitted changes, --scope=project for all docs)
2. ✓ Launch 6 domain analysts in parallel to review documentation
3. ✓ Analyze findings: FUNDAMENTAL (reality mismatches), STRUCTURAL (architecture issues), SURFACE (polish)
4. ✓ Present user options (full workflow, critical fixes only, show plan, or skip)
5. ✓ Execute chosen CRUD operations (create missing docs, update outdated, delete obsolete)
6. ✓ Validate: all required docs exist, links work, examples are current

**Claude Code MUST NOT:**
- ✗ Modify files without user confirmation
- ✗ Skip validation step
- ✗ Silently fail

---

## VALIDATION & PREREQUISITES

**Before executing, Claude Code MUST validate:**

- [ ] Git repository exists (check `.git/` directory)
- [ ] `docs/` directory exists and is readable
- [ ] Can read uncommitted changes (git status works)
- [ ] Can write to documentation files

---

## IMPLEMENTATION FLOW

### Step 1: Scope Detection
Determine analysis scope: `--scope=changes` (default, 30-60s) or `--scope=project` (comprehensive, 4-6 min)

### Step 2: Parallel Analysis (6 concurrent analysts)
- docs-analyst x4 (information architecture, content quality, user journey, semantic coherence)
- architecture-analyst (technical accuracy)
- code-quality-analyst (code examples)

### Step 3: Categorize Findings
Group findings as FUNDAMENTAL (reality mismatches), STRUCTURAL (architecture), or SURFACE (polish)

### Step 4: Present Condensed Summary
Present user with interactive choice table (A/B/C/Other/Skip options) with recommendation

### Step 5: Execute CRUD Operations
Based on user choice, create missing docs, update outdated content, delete obsolete sections

### Step 6: Validate & Report
Verify README links, CHANGELOG format, API docs accuracy, code examples current

---

## USAGE

```bash
# Default: Analyze changes related to uncommitted git modifications (fast)
/docs:sync

# Analyze entire project documentation (comprehensive)
/docs:sync --scope=project

# Explicit: Analyze only uncommitted changes
/docs:sync --scope=changes
```

**Arguments:**

| Argument | Default | Description |
|----------|---------|-------------|
| `--scope` | changes | Analyze scope: `changes` (git modifications) or `project` (all docs) |

**Examples:**

- `/docs:sync` - Quick check on changes
- `/docs:sync --scope=project` - Full documentation audit

---

## Sync Options

| Option | Action | Recommendation |
|--------|--------|-----------------|
| **A** | Analyze recent changes only | **← Recommended** for iterative updates |
| **B** | Auto-fix identified issues immediately | For straightforward formatting and structure fixes |
| **C** | Run full project audit | When performing comprehensive documentation review |

Your choice (A/B/C)?

## Next Steps

| Step | Action | Details |
|------|--------|---------|
| 1 | Review identified documentation gaps | Check what changes are needed and why |
| 2 | Commit documentation updates | Stage and commit synchronized changes |
| 3 | Push to repository or docs branch | Sync with main repository or docs deployment |
| 4 | Deploy updated documentation | Trigger docs rebuild and publish changes |

What would you like to do next?
| Skip | Exit | Don't modify documentation | No changes |

**User Flow:**
1. Analysis completes and displays findings (FUNDAMENTAL/STRUCTURAL/SURFACE)
2. Table above is presented
3. Prompt: `Your choice (A/B/C/Other/Skip): _`
4. Upon selection (e.g., B): `Proceeding with Option B (Critical Issues Only)...`
5. Execute chosen CRUD operations
6. Display results and **Next Steps** table

---

## EXAMPLES

**Example 1: Quick Documentation Check**

```bash
/docs:sync

# Expected output:
✅ Documentation Sync Complete

**Scope**: Analyzing changes (12 files affected)

**Analysis Results**:
- FUNDAMENTAL: 0 issues
- STRUCTURAL: 2 issues (1 broken link, 1 outdated API reference)
- SURFACE: 3 issues (formatting, code examples)

**Recommended Action**: Option B (structural fixes)

Your choice: B

**Changes Applied**:
- Updated: docs/api/users.md (endpoint signature)
- Fixed: README.md (broken link)
- Updated: 2 code examples

✅ Documentation synchronized
```

**Example 2: Full Project Audit**

```bash
/docs:sync --scope=project

# Expected output:
✅ Documentation Audit Complete

**Scope**: Analyzing entire project (145 files)

**Analysis Results**:
- FUNDAMENTAL: CONTRIBUTING.md missing, 3 entity references
- STRUCTURAL: Navigation inconsistent in 5 files
- SURFACE: 12 formatting issues

**Recommended Action**: Option A (comprehensive fix)

Your choice: A

**Changes Applied**:
- Created: CONTRIBUTING.md
- Updated: 8 documentation files
- Fixed: 15 broken links
- Reformatted: 5 files for consistency

✅ Documentation now current and complete
```

---

## ERROR HANDLING

| Error | Cause | Solution |
|-------|-------|----------|
| Git not available | git command missing | Install git first |
| `docs/` directory not found | Documentation missing | Initialize documentation structure |
| Permission denied | Can't write to files | Check file permissions |
| No changes detected | Nothing to analyze | Make code changes or use `--scope=project` |

---

## OUTPUT FORMAT

✅ **Status**: Documentation Sync Complete
✅ **Scope**: What was analyzed
✅ **Results**: Issues found by category
✅ **Action**: Recommendation and user choice
✅ **Changes**: Files created/updated/deleted
✅ **Next Steps**: Commit docs or run again later

---

## ROBUSTNESS & CONSTRAINTS

**IN SCOPE:**
- Analyze README, CHANGELOG, CONTRIBUTING, SECURITY, API docs, architecture docs
- Keep a Changelog v1.1.0 compliance
- Code example validation
- Cross-reference checking
- GitHub rendering optimization

**OUT OF SCOPE:**
- Code implementation (developer responsibility)
- Git operations beyond status/diff (use /git:* commands)
- External documentation hosting setup
- Translation/internationalization

**Atomic Operations:**
- If validation fails: No modifications
- Either fully succeeds or fails cleanly
- No partial documentation updates

**Cross-Platform:**
- Works on: Windows (PowerShell/WSL), macOS, Linux
- Uses: `python` (cross-platform)
- Paths: Forward slashes `/` work everywhere

---

## INTEGRATION POINTS

- **Follows**: Code implementation or feature development
- **Precedes**: Git commit, release workflow
- **Related**: `/docs:changelog` (manual changelog management)

**Workflow Example:**
```
/development → /docs:sync → /git:commit → /git:push
```

---

## QUALITY STANDARDS

**Command succeeds when:**
- ✓ Analysis completes without errors
- ✓ User sees clear categorized findings
- ✓ User confirms before modifications
- ✓ Chosen CRUD operations execute
- ✓ Validation passes for all changes
- ✓ Clear summary of what changed

**Checklist:**
- [X] Scope detection works (changes vs project)
- [X] Analysts can be launched in parallel
- [X] Findings are categorized appropriately
- [X] User can choose action level
- [X] CRUD operations execute cleanly
- [X] Validation comprehensive
- [X] User Feedback Table shows exactly ONE "Recommended" option
- [X] Next Steps table always provided (2-4 actionable options)
- [X] Ends with "What would you like to do next?" closing

---

## Next Steps

After documentation sync completes, suggested next actions:

| Option | Action | Description | Command |
|--------|--------|-------------|---------|
| **A** | Review changes | Examine what was modified in docs | `git diff docs/` |
| **B** | Commit changes | **Recommended: Save documentation updates** | `/git:commit "docs: synchronize documentation with codebase"` |
| **C** | Continue development | Proceed with code changes | Continue coding |
| **Other** | Custom | What you need next | Describe your next step |

What would you like to do next? Choose from the table above or describe your next step.
