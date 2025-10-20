---
description: "Idempotent documentation workflow: analyzes needs and performs CRUD operations on all documentation types"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Docs

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Idempotent documentation workflow - analyze needs and execute CRUD operations on all documentation types.

**YOU MUST:**
1. ✓ Analyze documentation scope (changes vs project)
2. ✓ Launch 6 domain analysts in parallel (4x docs-analyst perspectives + architecture + code-quality)
3. ✓ Detect CRUD operations needed (Create/Read/Update/Delete)
4. ✓ Present user choice: A=full workflow, B=fundamental fixes, C=show plan, Skip
5. ✓ Execute chosen operations (create missing docs, update outdated, delete obsolete)
6. ✓ Validate completeness (README, CHANGELOG, CONTRIBUTING, SECURITY, API docs)

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Make changes without user confirmation
- ✗ Skip validation step

---

## IMPLEMENTATION FLOW

### Step 1: Scope Detection
Detect scope (--scope=changes or --scope=project) and launch parallel analysis

### Step 2: Parallel Analysis (6 concurrent analysts)
- docs-analyst x4 (IA, content quality, user journey, semantic coherence)
- architecture-analyst (technical accuracy)
- code-quality-analyst (code examples)

### Step 3: Present Findings
Show categorized findings: FUNDAMENTAL (reality mismatches) | STRUCTURAL (architecture) | SURFACE (polish)

### Step 4: User Confirmation
Present A/B/C/Skip choices and get user input

### Step 5: Execute Operations
Create missing docs, update outdated content, delete obsolete sections

### Step 6: Validate
Check README links, CHANGELOG format, API docs accuracy, cross-references

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Idempotent documentation workflow for maintaining all documentation types (README, CHANGELOG following Keep a Changelog v1.1.0, CONTRIBUTING, SECURITY, API docs, architecture docs, user guides) with intelligent CRUD operation detection based on codebase changes

**O**bjective: Analyze current documentation state through parallel domain analysis (docs-analyst, architecture-analyst, code-quality-analyst), determine necessary CRUD operations (Create missing docs, Update outdated content, Delete obsolete sections), execute changes, validate completeness and accuracy

**S**tyle: Idempotent documentation automation with smart detection (code change timestamps, completeness validation, quality checks), Keep a Changelog v1.1.0 compliance, GitHub-friendly rendering (mobile-responsive, 2-level depth), and incremental updates

**T**one: Professional, comprehensive, standards-compliant with emphasis on maintainability - clear documentation structure, accurate code examples, proper cross-references

**A**udience: Developers, API consumers, documentation maintainers requiring always-current documentation that automatically synchronizes with codebase changes

**R**esults: Complete, current documentation suite with all required files (README, CHANGELOG, CONTRIBUTING, SECURITY), accurate API/architecture docs, validated code examples, working cross-references, and GitHub-optimized rendering

## Analysis Methodology

### 1. Scope Detection & Multi-Perspective Analysis (Parallel): Detect scope (changes vs project), launch 6 analysts concurrently - 4 docs-analyst invocations with different objectives (information architecture, content quality & reality alignment, user journey validation, semantic coherence) + architecture-analyst (technical accuracy) + code-quality-analyst (code examples)

### 2. User Confirmation: Display condensed summary (<10 lines) with progressive disclosure categorized as FUNDAMENTAL (reality mismatches), STRUCTURAL (architecture), SURFACE (polish). Provide smart recommendation. Offer execution levels: A=Full workflow, B=Fundamental fixes only (⭐ recommended for reality alignment), C=Show detailed plan. Skip=Cancel. NO file modifications until A or B selected

### 3. CRUD Operation Planning: Based on findings, determine Create (missing docs), Read (validation), Update (outdated content), Delete (obsolete sections) operations needed

### 4. Implementation: Main thread executes CRUD operations based on user choice (A=all fixes, B=fundamental only) - create missing files, update outdated sections, remove obsolete content, maintain Keep a Changelog format

### 5. Validation: Verify README links work, CHANGELOG follows Keep a Changelog v1.1.0, API docs match code, examples are accurate, cross-references valid, GitHub rendering correct

## Explicit Constraints

**IN SCOPE**: Documentation CRUD operations (README, CHANGELOG, CONTRIBUTING, SECURITY, API docs, architecture docs, user guides), Keep a Changelog v1.1.0 compliance, code example validation, cross-reference checking, GitHub rendering optimization
**OUT OF SCOPE**: Code implementation (developer responsibility), git operations (use /git:* commands), external documentation hosting (ReadTheDocs, GitBook setup), translation/i18n (internationalization)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% required docs, Accuracy >90% code examples, Relevance >85% synchronized with codebase, Efficiency <45s parallel analysis)

## Purpose

Intelligent, idempotent documentation workflow that analyzes current documentation state, determines what needs to be done (Create, Read, Update, Delete), and executes the appropriate operations across all documentation types.

## Usage

```bash
# Default: Analyze docs related to uncommitted changes (fast, iterative)
/workflows:docs

# Analyze entire project documentation (comprehensive)
/workflows:docs --scope=project

# Explicit: Analyze only uncommitted changes
/workflows:docs --scope=changes
```

**Arguments**:

- `--scope=changes` (default) - Analyze documentation related to uncommitted git changes (fast, 30-60s)
- `--scope=project` - Analyze all documentation in the project (comprehensive, 4-6min)

## Core Principle: Idempotency

**Idempotent Operation**: Running this command multiple times produces the same result - it only performs necessary changes, not redundant updates.

**Smart Detection**:

- Creates missing documentation (README, CONTRIBUTING, API docs, etc.)
- Updates outdated content based on code changes
- Validates existing documentation for accuracy
- Skips already-current documentation
- Removes obsolete or contradictory content

## UX Principles

**Condensed Summary (<10 lines)**:

- Lead with Impact (files, time, quality score)
- Group findings by priority: Critical → Important → Polish
- Use progressive disclosure for detailed breakdowns
- No scrolling required to see options

**Smart Recommendations**:

- Option A: Full workflow (comprehensive fixes, longer time)
- Option B: Critical fixes only (⭐ quick wins, minimal time)
- Option C: Show detailed plan (exploration, no changes)
- Recommend based on severity: Critical issues → suggest B, comprehensive needs → suggest A, no issues → suggest Skip

**Scannability**:

- Time estimates for each option
- Risk levels clearly labeled
- Recommended option marked with rationale
- Table format for easy comparison

**Progressive Disclosure**:

- Summary visible immediately
- Detailed analysis hidden in `<details>` tags
- Full context available but not overwhelming
- "View detailed breakdown" for power users

## Process

### Phase 1: Documentation State Analysis (Parallel)

**Step 1: Scope Detection**

```python
# Determine analysis scope based on --scope parameter (default: changes)
if scope == "changes":
    # Get uncommitted changes
    git_changes = run("git status --porcelain && git diff --name-only HEAD")

    # Smart expansion: Determine related documentation
    affected_docs = categorize_changes(git_changes):
        # Agent changes (agents/*.md) → Analyze docs mentioning those agents
        # Command changes (commands/**/*.md) → Analyze docs about command categories
        # CLAUDE.md changes → Analyze all concept/architecture docs
        # README.md changes → Analyze getting-started/onboarding docs
        # Code changes (*.py, *.sh) → Analyze docs about hooks/scripts

    # Result: Focused list of docs to analyze (e.g., 5-15 files)
    # Performance: ~30-60s analysis time

elif scope == "project":
    # Comprehensive analysis
    affected_docs = "all documentation in docs/, root docs (README, CONTRIBUTING, etc.)"
    # Performance: ~4-6min analysis time
```

**Step 2: Launch 6 Parallel Analysts (Scoped)**

```python
# All 6 analysts analyze ONLY the determined scope
# Each docs-analyst invocation has a different objective for multi-perspective analysis

Task(f"docs-analyst: Analyze information architecture of {affected_docs} - evaluate structure, navigation, taxonomy, findability, and organization")
Task(f"docs-analyst: Analyze content quality of {affected_docs} - cross-reference with codebase (check agents/ directory), validate entity references, find reality mismatches")
Task(f"docs-analyst: Analyze user journey in {affected_docs} - test onboarding paths, validate tutorials, check Day 1-30 progression, identify broken instructions")
Task(f"docs-analyst: Analyze semantic coherence in {affected_docs} - check terminology consistency, find conceptual conflicts, validate mental model clarity")
Task(f"architecture-analyst: Review technical documentation accuracy in {affected_docs}, validate diagrams, check architectural consistency")
Task(f"code-quality-analyst: Verify code examples in {affected_docs}, formatting standards, GitHub rendering compatibility")

# Each analyst persists findings to separate context files:
# - .agent/context/{session-id}/docs-analyst-info-arch.md
# - .agent/context/{session-id}/docs-analyst-content-quality.md
# - .agent/context/{session-id}/docs-analyst-user-journey.md
# - .agent/context/{session-id}/docs-analyst-semantic.md
# - .agent/context/{session-id}/architecture-analyst.md
# - .agent/context/{session-id}/code-quality-analyst.md

# Returns concise summary categorized as FUNDAMENTAL/STRUCTURAL/SURFACE issues
```

**Scope Examples**:

```bash
# Example 1: User modifies agents/security-analyst.md
affected_docs = [
    "README.md",  # Lists security-analyst
    "CLAUDE.md",  # References security patterns
    "docs/concepts/agent-specialist-framework.md",  # Describes agents
    "docs/user/user-guide.md"  # References security workflows
]
# Analysis time: ~45s (4 files)

# Example 2: User runs --scope=project
affected_docs = "all 145+ .md files in docs/, agents/, commands/, and root"
# Analysis time: ~6min (comprehensive)
```

### Phase 2: User Confirmation (Required)

**Display condensed summary (<10 lines) with progressive disclosure and new categorization**:

```markdown
## Documentation Workflow Summary

**Scope**: {changes: 12 files | project: 145 files}
**Impact**: X files · Y-Z min · Quality: [current]→[projected]/100 [✅ or ⚠️]

**FUNDAMENTAL (reality mismatches)**: [Non-existent entity refs, conceptual conflicts, broken onboarding]
**STRUCTURAL (architecture)**: [Navigation issues, IA problems, taxonomy gaps]
**SURFACE (polish)**: [Broken links, language tags, formatting]

<details><summary>📊 View detailed breakdown by analysis type</summary>

**Information Architecture Analysis**:
- Navigation: [findings]
- Taxonomy: [findings]
- Organization: [findings]

**Content Quality & Reality Alignment**:
- Entity validation: [findings - non-existent references]
- Reality mismatches: [findings - docs vs codebase conflicts]
- Outdated concepts: [findings]

**User Journey Validation**:
- Onboarding issues: [findings - broken paths]
- Tutorial problems: [findings - non-existent commands]
- Instruction gaps: [findings]

**Semantic Coherence Analysis**:
- Terminology conflicts: [findings - "8 agents" vs "43 analysts"]
- Conceptual inconsistencies: [findings]
- Mental model issues: [findings]

**Technical Accuracy** (architecture-analyst): [findings]
**Code Quality** (code-quality-analyst): [findings]

**CREATE Operations** (X files):
[Detailed list with explanations]

**UPDATE Operations** (X files):
[Detailed list with reasons - categorized by FUNDAMENTAL/STRUCTURAL/SURFACE]

**DELETE Operations**:
[List of obsolete content to remove]

</details>

## How would you like to proceed?

| Option | What Happens | Time | Focus |
|--------|--------------|------|-------|
| **A** | Full documentation refactoring | X hrs | All issues |
| **B** | Fundamental fixes (reality alignment) | X min | Conceptual + References ⭐ |
| **C** | Structural + Fundamental | X min | Architecture + Reality |
| **D** | Surface polish | X min | Links + Formatting |
| Skip | Exit without changes | 0s | None |

💡 **Recommended**: [Based on severity: FUNDAMENTAL → B, STRUCTURAL → C, SURFACE → D, None → Skip]

Your choice: _
```

**Actions based on user choice**:

- **A**: Proceed to Phase 3 with all CRUD operations (full workflow - all categories)
- **B**: Execute only FUNDAMENTAL fixes (reality mismatches, non-existent references, conceptual conflicts, broken onboarding), then exit
- **C**: Execute FUNDAMENTAL + STRUCTURAL fixes (add IA improvements, navigation, taxonomy), then exit
- **D**: Execute only SURFACE fixes (broken links, language tags, formatting), then exit
- **Skip**: Exit cleanly without any file modifications

**Critical Constraints**:

- NO file operations occur until user explicitly selects option A, B, C, or D
- Summary must be <10 lines before the expandable details section
- Lead with scope and time estimate for quick assessment
- Always provide recommended option based on severity of FUNDAMENTAL vs STRUCTURAL vs SURFACE findings
- Option B (fundamental) is typically recommended when reality mismatches are found

### Phase 3: Intelligent CRUD Operations (Main Thread)

Based on analyst findings, main thread determines and executes operations:

**CREATE Operations**:

- Generate missing README.md sections
- Create absent documentation files (CONTRIBUTING.md, API docs, architecture docs)
- Initialize CHANGELOG.md with Keep a Changelog format if missing
- Generate code examples and usage guides where needed
- Create external library documentation references

**READ Operations**:

- Validate existing documentation structure
- Check cross-references and links
- Verify documentation organization follows standards
- Review documentation completeness against codebase

**UPDATE Operations**:

- Refresh outdated sections based on code changes
- Update API documentation for modified endpoints
- Add CHANGELOG entries for unreleased changes
- Synchronize README with actual project state
- Update external library documentation references
- Refresh code examples with current syntax

**DELETE Operations**:

- Remove obsolete documentation for deleted features
- Clean up broken links and references
- Eliminate contradictory or redundant content
- Archive deprecated documentation appropriately

### Phase 4: Validation & Quality Assurance

```python
# Verify all operations completed successfully:
# - README links to docs/ work correctly
# - CHANGELOG follows Keep a Changelog v1.1.0 format
# - API documentation matches actual code
# - All code examples are accurate and runnable
# - Documentation renders properly on GitHub
# - Cross-references are valid
```

## Documentation Types Handled

### Essential Documentation

- **README.md** - Project overview, quick start, links to comprehensive docs
- **CHANGELOG.md** - Version history following Keep a Changelog v1.1.0
- **CONTRIBUTING.md** - Contribution guidelines
- **LICENSE** - License information (reference only, no modification)
- **SECURITY.md** - Security vulnerability reporting

### Technical Documentation

- **API Documentation** - Endpoint documentation, schemas, examples
- **Architecture Documentation** - System design, component relationships, diagrams
- **Developer Guides** - Setup, development workflows, testing
- **User Guides** - Installation, usage, tutorials

### External Documentation

- **Library Documentation** - External framework/library references (via Context7)
- **Best Practices** - Industry standards and patterns

## Idempotency Examples

### First Run (Missing Documentation)

```bash
/workflows:docs

# Phase 1 - Analysis:
✓ Documentation analyst: Missing CONTRIBUTING.md, API docs incomplete, CHANGELOG needs entries
✓ Architecture analyst: No architecture diagrams, component relationships undocumented
✓ Quality analyst: Several code examples outdated, formatting inconsistencies

# Phase 2 - Confirmation (Condensed UX):
## Documentation Workflow Summary

**Impact**: 8 files · 15-20 min · Quality: 65→85/100 ✅

**Critical (must fix)**: CONTRIBUTING.md missing, 2 broken README links
**Important**: API docs structure, architecture diagrams, CHANGELOG entries
**Polish**: 5 code examples, formatting consistency

<details><summary>📊 View detailed breakdown</summary>
[Full CREATE/UPDATE/DELETE lists with explanations...]
</details>

## How would you like to proceed?

| Option | What Happens | Time | Risk |
|--------|--------------|------|------|
| **A** | Full workflow (all fixes) | 20 min | Low |
| **B** | Critical fixes only | 5 min | Very Low ⭐ |
| **C** | Show detailed plan | 1 min | None |
| Skip | Exit without changes | 0s | None |

💡 **Recommended**: Option A (comprehensive documentation setup)

Your choice: A

# Phase 3 - CRUD Operations (after user approval):
CREATE: CONTRIBUTING.md with project guidelines
CREATE: docs/architecture.md with Mermaid diagrams
CREATE: docs/api/ with endpoint documentation
UPDATE: CHANGELOG.md with 3 unreleased entries
UPDATE: 5 code examples with current syntax
UPDATE: README.md links to new documentation structure
DELETE: 2 broken links from README
DELETE: Obsolete feature documentation

# Result: Documentation now complete and current (85/100) ✅
```

### Second Run (Already Current)

```bash
/workflows:docs

# Phase 1 - Analysis:
✓ Documentation analyst: All documentation current and complete
✓ Architecture analyst: Technical docs match current codebase
✓ Quality analyst: All examples valid, formatting consistent

# Phase 2 - Confirmation (Condensed UX):
## Documentation Workflow Summary

**Impact**: 0 files · 0 min · Quality: 88/100 ✅ (already meets target)

**Critical**: None - all documentation current
**Important**: None - no updates needed
**Polish**: None - formatting consistent

## How would you like to proceed?

| Option | What Happens | Time | Risk |
|--------|--------------|------|------|
| **A** | Full workflow (no changes) | 0 min | None |
| **B** | Critical fixes only (none needed) | 0 min | None |
| **C** | Show validation report | 1 min | None |
| Skip | Exit | 0s | None ⭐ |

💡 **Recommended**: Skip (documentation already current)

Your choice: Skip

# Result: No changes required - documentation healthy ✅
```

### Third Run (After Code Changes)

```bash
/workflows:docs

# Phase 1 - Analysis:
✓ Documentation analyst: 2 API endpoints changed, 1 new feature undocumented
✓ Architecture analyst: Component diagram needs update for new service
✓ Quality analyst: 3 code examples need updating

# Phase 2 - Confirmation (Condensed UX):
## Documentation Workflow Summary

**Impact**: 6 files · 10-12 min · Quality: 85→88/100 ✅

**Critical (must fix)**: New notifications feature undocumented
**Important**: 2 API endpoint docs outdated, architecture diagram stale
**Polish**: 3 code examples need refresh

<details><summary>📊 View detailed breakdown</summary>
**CREATE**: docs/features/notifications.md (new feature)
**UPDATE**: docs/api/authentication.md, docs/api/users.md, docs/architecture.md, CHANGELOG.md, 3 code examples
</details>

## How would you like to proceed?

| Option | What Happens | Time | Risk |
|--------|--------------|------|------|
| **A** | Full workflow (all fixes) | 12 min | Low |
| **B** | Critical fixes only | 3 min | Very Low ⭐ |
| **C** | Show detailed plan | 1 min | None |
| Skip | Exit without changes | 0s | None |

💡 **Recommended**: Option B (document new feature quickly, update rest later)

Your choice: B

# Phase 3 - CRUD Operations (critical fixes only):
CREATE: docs/features/notifications.md (new feature documentation)
UPDATE: CHANGELOG.md (add notifications feature entry)

# Result: Critical documentation synchronized (new feature documented) ✅
# Note: Run workflow again later to update API docs and code examples
```

## Agent Integration

**Critical Constraint**: Subagents provide analysis ONLY - no implementation allowed

- **Phase 1**: Scope detection + 6 parallel analyst invocations (multi-perspective analysis)
- **Phase 2**: Main thread displays condensed summary (<10 lines) categorized as FUNDAMENTAL/STRUCTURAL/SURFACE, recommends execution level (A/B/C/D)
- **Phase 3**: **Main thread executes CRUD operations** based on user choice (A=all, B=fundamental, C=fundamental+structural, D=surface) after explicit approval
- **Phase 4**: Main thread validates all changes and ensures quality

**Multi-Perspective Analysis Pattern**: Single enhanced docs-analyst invoked 4 times in parallel with different objectives

**Analyst Invocations** (all analysis only, no implementation):

1. **docs-analyst (information architecture)** - Structure, navigation, taxonomy, findability
2. **docs-analyst (content quality)** - Cross-reference with codebase, validate entity references, reality alignment
3. **docs-analyst (user journey)** - Test onboarding paths, validate tutorials, check learning progression
4. **docs-analyst (semantic coherence)** - Terminology consistency, conceptual model accuracy, mental model clarity
5. **architecture-analyst** - Technical accuracy, diagram validation, structural issues
6. **code-quality-analyst** - Example accuracy, formatting standards, quick wins

**Implementation Responsibility**: Main thread executes documentation operations (full/fundamental/structural/surface) after user confirms

**Categorization**: Analysts must tag findings as FUNDAMENTAL (reality mismatches), STRUCTURAL (architecture/IA), or SURFACE (polish) to enable granular option filtering

## Integration Points

### Development Workflow

```bash
# After feature implementation
/development:small "implement notifications"
/workflows:docs  # Automatically documents new feature

# After bug fix
/quality:bug-quickly "fix auth token expiration"
/workflows:docs  # Updates CHANGELOG and troubleshooting docs

# After architectural change
# (refactor services)
/workflows:docs  # Updates architecture diagrams and docs
```

### Release Workflow

```bash
# Prepare release documentation
/workflows:docs  # Ensures all docs current
/docs:changelog 1.2.0 --release  # Release CHANGELOG entry
/git:commit "chore: release v1.2.0 with documentation"
```

### CI/CD Integration

```yaml
# .github/workflows/docs.yml
- name: Validate Documentation
  run: claude-cli /workflows:docs

- name: Check for changes
  run: |
    if git diff --quiet; then
      echo "Documentation is current"
    else
      echo "Documentation updated"
      git add .
      git commit -m "docs: automated documentation update"
    fi
```

## Keep a Changelog Integration

**Automatic CHANGELOG.md Management**:

- Creates CHANGELOG.md with Keep a Changelog v1.1.0 format if missing
- Adds Unreleased entries for undocumented changes
- Maintains proper category structure (Added, Changed, Fixed, etc.)
- Updates comparison links
- Validates semantic versioning compliance

**Use `/docs:changelog` for manual CHANGELOG operations**

## Smart Detection Logic

### Code Change Detection

- Compares documentation timestamps with code modification dates
- Identifies new/modified/deleted files requiring documentation updates
- Detects API signature changes needing documentation updates
- Tracks architectural changes requiring diagram updates

### Completeness Validation

- Verifies all public APIs are documented
- Checks README completeness (required sections present)
- Ensures CONTRIBUTING.md exists
- Validates CHANGELOG entries for recent changes
- Confirms code examples match current codebase

### Quality Checks

- Validates all internal links work
- Verifies code examples execute without errors
- Checks formatting consistency (markdownlint compliance)
- Ensures GitHub rendering compatibility
- Validates Mermaid diagram syntax

## Performance Characteristics

**Multi-Perspective Parallel Analysis**: 6 concurrent analyses (4 docs-analyst objectives + architecture-analyst + code-quality-analyst) - substantially faster than sequential

**Scope-Based Performance**:

- **`--scope=changes`** (default): 30-60s analysis (targeted, iterative)
- **`--scope=project`**: 4-6min analysis (comprehensive, audit)

**Typical Execution**:

- **First run** (missing docs + --scope=project): Comprehensive generation
- **Subsequent runs** (current docs + --scope=changes): Quick validation, targeted updates
- **After code changes** (--scope=changes): Focused analysis of affected docs only

**Idempotency Benefit**: No redundant work, only necessary operations. Scope awareness eliminates analyzing unrelated docs.

## Success Criteria

✅ All required documentation files exist (README, CHANGELOG, CONTRIBUTING, SECURITY)
✅ Documentation is current with codebase (no outdated content)
✅ CHANGELOG follows Keep a Changelog v1.1.0 format
✅ All code examples are accurate and executable
✅ README links to docs/ sections work correctly
✅ API documentation matches actual endpoints
✅ Architecture diagrams reflect current system design
✅ No broken links or references
✅ Consistent formatting across all documentation
✅ GitHub rendering is mobile-friendly

## Related Commands

- `/docs:changelog` - Manual CHANGELOG management with Keep a Changelog standard
- `/git:commit` - Commit documentation changes
- `/development:small` - After implementation, run /workflows:docs
- `/quality:bug-quickly` - After bug fix, run /workflows:docs

## Best Practices

1. **Run after every significant change** - Keep documentation synchronized
2. **Trust idempotency** - Safe to run anytime, no redundant updates
3. **Review generated content** - Verify accuracy before committing
4. **Use /docs:changelog for manual entries** - Add context-rich changelog entries
5. **Let workflow detect needs** - Don't specify what to update, let it analyze
6. **Run before releases** - Ensure all documentation current
7. **Include in CI/CD** - Automated documentation validation

## Notes

- **Fully Automated**: No configuration required
- **Idempotent**: Safe to run repeatedly
- **Intelligent**: Only performs necessary operations
- **Comprehensive**: Handles all documentation types
- **Integrated**: Works with Keep a Changelog v1.1.0 standard
- **Fast**: Parallel analysis for quick assessment
