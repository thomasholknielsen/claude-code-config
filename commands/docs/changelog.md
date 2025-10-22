---
description: "Maintain CHANGELOG.md following Keep a Changelog v1.1.0 standard"
argument-hint: "[version] [--add-entry] [--release]"
allowed-tools: Bash, Read, Edit, Grep, mcp__sequential-thinking__sequentialthinking
---

# Command: Changelog

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Maintain CHANGELOG.md following Keep a Changelog v1.1.0 standard with semantic versioning compliance.

**Claude Code MUST execute this workflow:**
1. ✓ Validate CHANGELOG.md format (Keep a Changelog v1.1.0)
2. ✓ Support two modes: add-entry (new bullet to Unreleased) and release (migrate Unreleased to version)
3. ✓ Enforce semantic versioning format (MAJOR.MINOR.PATCH)
4. ✓ Validate category order (Added/Changed/Deprecated/Removed/Fixed/Security)
5. ✓ Update comparison links for version diffs
6. ✓ Preserve ISO 8601 date format (YYYY-MM-DD)
7. ✓ Display confirmation with format validation

**Claude Code MUST NOT:**
- ✗ Allow non-semver versions
- ✗ Disrupt category ordering
- ✗ Skip format validation

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Maintain CHANGELOG.md via Keep a Changelog v1.1.0 + Semantic Versioning standards, interactive entry addition (category selection: Added/Changed/Deprecated/Removed/Fixed/Security, description + issue/PR reference, append to Unreleased), version release (validate Unreleased content, create version header with ISO date, move entries to version section, reset Unreleased, update comparison links), format validation (semver, ISO 8601 dates, no 'v' prefix)

**P**urpose: Maintain user-focused changelog following industry standards (Keep a Changelog v1.1.0), enable systematic change tracking across releases, support semantic versioning compliance (MAJOR.MINOR.PATCH), provide clear communication to users about changes, integrate with development/release workflows, maintain comparison links for version diffs

**E**xpectation: Add-entry mode → new bullet in Unreleased section (category/description/reference), updated file. Release mode → version header [X.Y.Z] - YYYY-MM-DD, Unreleased entries moved to version, Unreleased reset, comparison links updated, semver validated. All modes preserve Keep a Changelog format (categories in order: Added/Changed/Deprecated/Removed/Fixed/Security)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% format compliance, Accuracy >90% version/date correctness, Relevance >85% user-focused descriptions, Efficiency <10s typical update)

## Explicit Constraints

**IN SCOPE**: CHANGELOG.md maintenance (Keep a Changelog v1.1.0), entry addition (interactive category/description/reference), version release (header creation, entry migration, Unreleased reset, link updates), format validation (semver, ISO 8601, no 'v' prefix), user-focused writing (impact not implementation), issue/PR referencing
**OUT OF SCOPE**: Automated git log parsing (manual entry required), implementation details in entries, non-semver versioning, custom changelog formats, multi-file changelogs, automated release creation (changelog only)

## Purpose

Maintains project CHANGELOG.md following the [Keep a Changelog v1.1.0](https://keepachangelog.com/en/1.1.0/) standard with semantic versioning.

## Usage

```bash
/docs:changelog $ARGUMENTS
```

**Arguments**:

- `$1` (version): Version number for release (e.g., 1.2.0, 2.0.0-beta.1) (optional)
- `$2` (--add-entry): Add new change entry to Unreleased section (optional)
- `$3` (--release): Mark Unreleased changes as released under version (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "1.2.0 --release"` - Release version 1.2.0 with current Unreleased changes
- `$ARGUMENTS = "--add-entry"` - Add new entry to Unreleased section
- `$ARGUMENTS = "2.0.0-beta.1 --release"` - Release pre-release version

## Keep a Changelog Standard

### Required Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Vulnerability fixes

## [1.2.0] - 2025-10-06

### Added
- Feature description

[Unreleased]: https://github.com/org/repo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/org/repo/compare/v1.1.0...v1.2.0
```

### Change Categories (in order)

1. **Added** - New features
2. **Changed** - Changes in existing functionality
3. **Deprecated** - Soon-to-be removed features
4. **Removed** - Removed features
5. **Fixed** - Bug fixes
6. **Security** - Vulnerability fixes

### Version Format

- **Major.Minor.Patch**: `1.2.0` (semantic versioning)
- **Pre-release**: `2.0.0-alpha.1`, `2.0.0-beta.1`, `2.0.0-rc.1`
- **Date**: `YYYY-MM-DD` format (ISO 8601)

## Process

### Adding New Entry (`--add-entry`)

1. **Interactive Prompt**:

   ```text
   Select change type:
   1. Added (new features)
   2. Changed (existing functionality changes)
   3. Deprecated (soon-to-be removed)
   4. Removed (removed features)
   5. Fixed (bug fixes)
   6. Security (vulnerability fixes)

   Choice: 5

   Enter change description:
   > Fix authentication token expiration bug

   Issue/PR reference (optional):
   > #123
   ```

2. **Add to Unreleased Section**: Append entry to appropriate category

3. **Validate Format**: Ensure Keep a Changelog compliance

### Releasing Version (`--release`)

1. **Validate Unreleased Section**: Check for changes to release

2. **Create Version Header**:

   ```markdown
   ## [1.2.0] - 2025-10-06
   ```

3. **Move Unreleased Changes**: Transfer all Unreleased entries to version section

4. **Reset Unreleased Section**: Clear all categories for new changes

5. **Update Comparison Links**:

   ```markdown
   [Unreleased]: https://github.com/org/repo/compare/v1.2.0...HEAD
   [1.2.0]: https://github.com/org/repo/compare/v1.1.0...v1.2.0
   ```

6. **Validate Semantic Versioning**: Check version number follows semver

## Examples

### Add New Feature Entry

```bash
/docs:changelog --add-entry

# Interactive prompt:
# Type: 1 (Added)
# Description: "Implement JWT authentication with refresh tokens"
# Reference: "#123"

# Result in CHANGELOG.md:
## [Unreleased]

### Added
- Implement JWT authentication with refresh tokens (#123)
```

### Add Bug Fix Entry

```bash
/docs:changelog --add-entry

# Interactive prompt:
# Type: 5 (Fixed)
# Description: "Resolve authentication token expiration bug"
# Reference: "#125"

# Result in CHANGELOG.md:
## [Unreleased]

### Fixed
- Resolve authentication token expiration bug (#125)
```

### Release Version

```bash
/docs:changelog 1.2.0 --release

# Transforms:
## [Unreleased]

### Added
- Implement JWT authentication (#123)

### Fixed
- Resolve token expiration bug (#125)

# Into:
## [Unreleased]

## [1.2.0] - 2025-10-06

### Added
- Implement JWT authentication (#123)

### Fixed
- Resolve token expiration bug (#125)

# Updates comparison links:
[Unreleased]: https://github.com/org/repo/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/org/repo/compare/v1.1.0...v1.2.0
```

### Release Pre-release Version

```bash
/docs:changelog 2.0.0-beta.1 --release

# Creates:
## [2.0.0-beta.1] - 2025-10-06

### Added
- New breaking API endpoints

[Unreleased]: https://github.com/org/repo/compare/v2.0.0-beta.1...HEAD
[2.0.0-beta.1]: https://github.com/org/repo/compare/v1.2.0...v2.0.0-beta.1
```

## Integration Points

### Development Workflow

```bash
# After implementing feature
/development:small "implement user auth"
/docs:changelog --add-entry  # Add feature to Unreleased

# After fixing bug
/quality:bug-quickly "fix token expiration"
/docs:changelog --add-entry  # Add fix to Unreleased
```

### Release Workflow

```bash
# Prepare release
/docs:changelog 1.2.0 --release
/git:commit "chore: release v1.2.0"
/git:pr "Release v1.2.0"
```

### CI/CD Integration

```yaml
# .github/workflows/release.yml
- name: Update Changelog
  run: claude-cli /docs:changelog $VERSION --release

- name: Commit Changelog
  run: |
    git add CHANGELOG.md
    git commit -m "chore: release v$VERSION"
```

## Validation Rules

### Entry Format Validation

- **Required**: Category, description
- **Optional**: Issue/PR reference, author attribution
- **Format**: `- Description text (#123)` or `- Description text by @username (#123)`

### Version Number Validation

- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Pre-release**: MAJOR.MINOR.PATCH-alpha|beta|rc.N
- **No 'v' prefix**: Use `1.2.0`, not `v1.2.0` in headers

### Date Format Validation

- **ISO 8601**: `YYYY-MM-DD`
- **Example**: `2025-10-06`

## Quality Standards

### Writing Guidelines

**User-Focused**:

- Write from user perspective
- Describe impact, not implementation
- Use active voice

**Examples**:

- ✅ "Add password reset via email"
- ❌ "Implemented password reset functionality"
- ✅ "Fix login redirect after authentication"
- ❌ "Fixed bug in auth redirect logic"

**Specific and Actionable**:

- Include enough context to understand impact
- Reference issues/PRs for detailed information
- Group related changes logically

**Consistent Structure**:

- Start with verb in present tense (Add, Change, Fix, Remove)
- Keep entries concise (one line preferred)
- Use bullet points for sub-items if needed

### Technical Accuracy

- **Verify changes**: Ensure accuracy against git log
- **Check references**: Validate issue and PR links
- **Date accuracy**: Use actual release date
- **Version compliance**: Follow semantic versioning strictly

## Error Handling

### No Unreleased Changes

```text
⚠ No unreleased changes found to release

Add changes with:
  /docs:changelog --add-entry

Then release with:
  /docs:changelog 1.2.0 --release
```

### Invalid Version Format

```text
✗ Invalid version format: v1.2.0

Use semantic versioning without 'v' prefix:
  1.2.0 (release)
  2.0.0-beta.1 (pre-release)
```

### Missing CHANGELOG.md

```text
⚠ CHANGELOG.md not found

Creating CHANGELOG.md with Keep a Changelog format...
✓ Created CHANGELOG.md
```

## Best Practices

1. **Add entries immediately** - Don't batch changelog updates
2. **Reference issues/PRs** - Always link to context (#123)
3. **User-focused descriptions** - Write for users, not developers
4. **Semantic versioning** - Follow semver strictly
5. **Keep Unreleased current** - Maintain up-to-date Unreleased section
6. **Release notes from changelog** - Use changelog for release descriptions
7. **Review before release** - Proofread Unreleased section before releasing

## Related Standards

- **Keep a Changelog**: <https://keepachangelog.com/en/1.1.0/>
- **Semantic Versioning**: <https://semver.org/spec/v2.0.0.html>
- **ISO 8601 Dates**: <https://www.iso.org/iso-8601-date-and-time-format.html>

## Success Criteria

✅ CHANGELOG.md follows Keep a Changelog v1.1.0 format
✅ All changes categorized correctly (Added, Changed, Fixed, etc.)
✅ Version numbers follow semantic versioning
✅ Dates use ISO 8601 format (YYYY-MM-DD)
✅ Comparison links updated correctly
✅ Entries are user-focused and actionable
✅ Issue/PR references included where applicable
