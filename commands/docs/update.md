# Documentation Updater

I'll intelligently update your existing project documentation by analyzing changes and keeping everything current and consistent.

**My focused approach:**
1. **Analyze conversation and code changes** - Understand what actually changed
2. **Read existing documentation** - All current docs to understand structure
3. **Compare reality vs documentation** - Find outdated or missing information
4. **Update systematically** - Maintain existing style and structure
5. **Preserve custom content** - Never overwrite manual additions

**I focus on updating, not creating** - Use `/docs generate` for new documentation or `/docs analyze` for coverage analysis.

## Smart Update Process

I'll automatically detect what needs updating by:

1. **Analyzing changes** - Compare code vs current documentation
2. **Identifying updates needed:**
   - New features to document
   - Changed APIs or interfaces
   - Removed features to clean up
   - New configuration options
   - Updated dependencies
   - Bug fixes and improvements

3. **Update systematically:**
   - README.md with new features/changes
   - CHANGELOG.md with version entries
   - API docs with new endpoints
   - CLAUDE.md statistics via `.specify/scripts/sync-claude-md.py` (if in Claude Code repo)
   - Configuration docs with new options
   - Migration guides if breaking changes

## Context-Aware Updates

I automatically detect what type of changes occurred:
- **New features** → Update README features, add to CHANGELOG
- **Bug fixes** → Document in CHANGELOG, update troubleshooting
- **Refactoring** → Update architecture docs, migration guide
- **Security fixes** → Update security policy, CHANGELOG
- **Performance improvements** → Update benchmarks, CHANGELOG
- **Spec-kit features** → Document completed features from `.specify/`

## Update Rules

**ALWAYS:**
- Read existing docs completely before any update
- Find the exact section that needs updating
- Update in-place, never duplicate
- Preserve custom content and formatting
- Match existing style and structure

**Preserve sections:**
```markdown
<!-- CUSTOM:START -->
User's manual content preserved
<!-- CUSTOM:END -->
```

**Smart CHANGELOG:**
- Groups changes by type (Added, Fixed, Changed, etc.)
- Suggests appropriate version bump
- Links to relevant PRs/issues
- Maintains chronological order

## Integration Points

Works with other commands:
- After `/implement` or `/scaffold` - Document new features
- After `/fix bug-quickly` - Update CHANGELOG and troubleshooting
- After `/refactor` - Update architecture and migration docs
- After `/test` - Update test documentation coverage
- After `/review security` - Update security documentation

## Usage Patterns

**Simple update after changes:**
```bash
/docs update
# Analyzes recent changes and updates all affected documentation
```

**After major development:**
```bash
/explain architecture && /docs update
# Re-analyzes architecture, then updates all architectural documentation
```

**Before releases:**
```bash
/test all && /docs update
# Ensures tests pass, then documents any test coverage changes
```

This command focuses solely on keeping existing documentation current and accurate.