# CHANGELOG Manager

I'll intelligently manage your project's CHANGELOG.md by analyzing changes, organizing them by type, and maintaining professional version history.

**My CHANGELOG approach:**
1. **Analyze changes** - Review commits, PRs, and conversation history
2. **Categorize updates** - Group by Added, Fixed, Changed, Security, etc.
3. **Suggest versioning** - Recommend semantic version bumps
4. **Format professionally** - Follow Keep a Changelog standards
5. **Maintain chronology** - Preserve version history and dates

**I focus on CHANGELOG maintenance** - Use `/docs update` for general documentation or `/git commit` for commit message generation.

## Change Analysis & Categorization

### Automatic Change Detection
I'll analyze and categorize changes from:
- **Git commits** - Commit messages and diffs
- **Pull requests** - PR titles, descriptions, and changes
- **Conversation history** - What was implemented in the session
- **Code analysis** - New features, bug fixes, refactoring
- **Dependency updates** - Package.json, requirements.txt changes

### Standard Categories
Following Keep a Changelog format:
- **Added** - New features, components, endpoints
- **Changed** - Changes to existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Deleted features or functionality
- **Fixed** - Bug fixes and issue resolutions
- **Security** - Vulnerability fixes and security improvements

### Semantic Versioning Suggestions
Based on changes, I'll recommend:
- **MAJOR** (x.0.0) - Breaking changes, removed features
- **MINOR** (0.x.0) - New features, non-breaking additions
- **PATCH** (0.0.x) - Bug fixes, security patches
- **Pre-release** - Alpha, beta, release candidate versions

## CHANGELOG Generation & Maintenance

### Professional Format
Generate industry-standard CHANGELOG:
```markdown
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.2.0] - 2024-01-15

### Added
- User authentication system with JWT tokens
- Password reset functionality via email
- API rate limiting middleware

### Changed
- Improved error handling in authentication module
- Updated database connection pooling configuration

### Fixed
- Fixed memory leak in file upload handler
- Resolved issue with timezone handling in date queries

### Security
- Updated dependencies to address security vulnerabilities
- Enhanced input validation for user registration

## [1.1.0] - 2023-12-20
...
```

### Smart Content Generation
I'll create meaningful entries by:
- **Extracting key changes** - Focus on user-facing improvements
- **Writing clear descriptions** - Non-technical language for users
- **Linking to issues/PRs** - Reference GitHub issues and pull requests
- **Grouping related changes** - Combine similar improvements
- **Highlighting breaking changes** - Clearly mark compatibility issues

## Advanced CHANGELOG Features

### Breaking Changes Documentation
For major version bumps:
- **Migration guides** - How to upgrade from previous versions
- **Compatibility notes** - What changed and why
- **Deprecation timeline** - When features will be removed
- **Alternative approaches** - Replacements for removed features

### Release Note Generation
Transform CHANGELOG entries into:
- **GitHub release notes** - Formatted for GitHub releases
- **Blog post content** - User-friendly announcements
- **Email newsletters** - Customer communication
- **Documentation updates** - Version-specific guides

### Integration Links
Automatically link to:
- **GitHub issues** - `Fixed issue #123`
- **Pull requests** - `Merged PR #456`
- **Commit hashes** - `(abc123f)`
- **Contributors** - `Thanks @username`
- **External links** - Security advisories, RFC references

## Project-Specific Intelligence

### Framework-Aware Changes
Detect and categorize framework-specific changes:
- **API changes** - New endpoints, parameter changes
- **Database migrations** - Schema changes, new tables
- **Configuration changes** - New environment variables
- **Dependencies** - Package updates, new libraries
- **Performance improvements** - Optimization and benchmarks

### Technology-Specific Categories
Adapt categories for project type:
- **Web apps** - UI changes, performance, accessibility
- **APIs** - Endpoints, authentication, rate limiting
- **Libraries** - Public API changes, breaking changes
- **CLI tools** - New commands, option changes
- **Mobile apps** - Platform updates, native features

## Workflow Integration

### Automated CHANGELOG Updates
```bash
# After development session
/docs changelog
# Analyze session changes and update CHANGELOG

# Before release
/docs changelog --version 1.2.0
# Prepare release entry with version number

# After feature completion
/spec-kit implement && /docs changelog
# Complete feature, then document in CHANGELOG
```

### Release Preparation
```bash
# Complete release workflow
/test all && /docs changelog --release && /git commit
# Run tests, prepare CHANGELOG, commit changes
```

## Version Management

### Unreleased Section Management
- **Accumulate changes** - Collect changes in [Unreleased] section
- **Release preparation** - Move unreleased to version section
- **Clean organization** - Maintain proper change categorization
- **Date formatting** - ISO date format for releases

### Version History Maintenance
- **Preserve history** - Never delete or modify existing entries
- **Consistent formatting** - Maintain uniform structure
- **Link management** - Keep GitHub compare links updated
- **Archive old versions** - Separate file for extensive history

## Quality Standards

### Change Description Quality
Ensure entries are:
- **User-focused** - Written from user perspective
- **Action-oriented** - Clear about what changed
- **Specific** - Detailed enough to understand impact
- **Consistent** - Uniform tone and structure
- **Scannable** - Easy to skim for relevant changes

### Technical Accuracy
- **Verify changes** - Ensure accuracy against actual code
- **Check links** - Validate issue and PR references
- **Date accuracy** - Correct release dates
- **Version compliance** - Follow semantic versioning rules

## Output Formats

### Standard CHANGELOG.md
- **Keep a Changelog format** - Industry standard
- **Markdown formatting** - Proper headers and lists
- **GitHub integration** - Linkable sections and references
- **Semantic versioning** - Proper version numbering

### Alternative Formats
- **JSON changelog** - Machine-readable format
- **Release notes** - GitHub/GitLab release format
- **RSS/Atom feeds** - Syndicated change notifications
- **API changelog** - OpenAPI change documentation

## Usage Patterns

### Continuous Updates
```bash
/docs changelog
# Add changes from current session to unreleased section
```

### Release Preparation
```bash
/docs changelog --version 2.1.0 --date 2024-01-15
# Move unreleased changes to version 2.1.0 release
```

### Focused Updates
```bash
/docs changelog --category security
# Focus only on security-related changes

/docs changelog --since v1.0.0
# Include changes since specific version
```

This command maintains professional, comprehensive version history that keeps users informed about project evolution and helps with upgrade planning.