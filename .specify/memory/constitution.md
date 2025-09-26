<!--
Sync Impact Report:
Version: 1.0.0 (initial constitution)
Modified principles: N/A (initial creation)
Added sections: All core principles and governance
Removed sections: N/A
Templates requiring updates:
  ✅ plan-template.md - Constitution Check section aligns with principles
  ✅ spec-template.md - Requirements align with agent-driven development
  ✅ tasks-template.md - Task ordering follows TDD and dependency principles
Follow-up TODOs: None
-->

# Claude Code Configuration Constitution

## Core Principles

### I. Agent-First Architecture
Every development task must be delegated to the most appropriate specialized agent based on domain expertise. Manual implementation is only acceptable when no suitable agent exists or when the task requires human creativity and judgment. Agent selection must be proactive and context-aware, leveraging parallel execution when tasks are independent.

**Rationale**: Specialized agents provide domain expertise, reduce errors, and improve code quality through focused competency. This principle ensures optimal resource utilization and maintains consistency across different types of development work.

### II. Specification-Driven Development
All features must begin with a comprehensive specification that defines user requirements, acceptance criteria, and testable outcomes before any implementation begins. Specifications must be business-focused (WHAT and WHY) and explicitly exclude implementation details (HOW). Any ambiguities must be marked as [NEEDS CLARIFICATION] and resolved before proceeding.

**Rationale**: Clear specifications prevent scope creep, ensure stakeholder alignment, and provide a foundation for test-driven development. This approach reduces rework and ensures features meet actual user needs.

### III. Pragmatic Testing Approach
Testing should be appropriate to the context: critical functionality requires comprehensive tests, while prototypes and experiments may use lighter testing. Tests should be written based on risk assessment and user impact. Test coverage should prioritize high-value scenarios over arbitrary metrics.

**Rationale**: Flexible testing approach balances quality with development velocity. This allows teams to adapt testing investment based on actual risk and business value.

### IV. Practical Quality Standards
Code changes should meet reasonable quality standards through automated tooling (linting, type checking) and peer review. Complex changes benefit from additional testing, but simplicity is preferred over rigid compliance. Quality investments should be proportional to the feature's importance and risk profile.

**Rationale**: Maintains code quality while allowing flexibility for different project phases and requirements. Focuses resources where they provide the most value.

### V. Incremental Context Management
Agent context files (CLAUDE.md, AGENTS.md, etc.) must be updated incrementally using the provided scripts. Manual context between markers must be preserved. Files must remain under 150 lines for token efficiency. Only recent changes (last 3) should be maintained to prevent context bloat.

**Rationale**: Effective context management ensures agents have relevant information while maintaining performance. Incremental updates prevent information loss and maintain system efficiency.

## Development Workflow Standards

### Code Quality Requirements
- All code changes must pass linting and type checking before completion
- Follow existing code patterns and conventions discovered through codebase analysis
- Security-sensitive changes require security-scanner agent review
- UI changes require ui-compliance-checker for accessibility and design compliance
- Performance-critical code requires performance-benchmarker validation

### File Management Protocol
- Prefer editing existing files over creating new files
- Never create documentation files unless explicitly requested
- Always use Read tool before editing any file
- Verify parent directory existence before creating new directories
- Quote file paths containing spaces in shell commands

### Git and Version Control
- Only commit changes when explicitly requested by users
- Follow repository's existing commit message patterns
- Include co-author attribution for AI assistance
- Never push to remote repositories without explicit permission
- Use appropriate branch naming conventions (###-feature-name format)

## Quality Assurance Framework

### Balanced Review Process
Apply reviews based on change risk and impact:
1. **Code Review**: Focus on maintainability, security, and functionality
2. **Security Review**: Required for authentication, data handling, and external integrations
3. **Design Review**: Applied to user-facing changes and accessibility-critical features

### Flexible Quality Checkpoints
- **High-risk changes**: Comprehensive review and testing
- **Standard changes**: Automated tooling plus peer review
- **Low-risk changes**: Automated checks with optional review
- **Experimental features**: Lightweight validation focused on learning

### Continuous Improvement Loop
Track effectiveness metrics: task completion quality, time to completion, error reduction rates, and user satisfaction. Use analytics-engine for comprehensive data analysis and trend identification.

## Governance

### Amendment Process
Constitution changes require:
1. Version bump following semantic versioning (MAJOR for breaking changes, MINOR for additions, PATCH for clarifications)
2. Documentation of impact on templates and dependent files
3. Sync Impact Report documenting all affected artifacts
4. Validation that all template references align with new principles

### Practical Governance
- Follow constitution principles as guidelines, not rigid rules
- Document significant architectural decisions and their rationale
- Regular retrospectives on what's working and what needs adjustment
- Evolve practices based on team feedback and project realities

### Version Control and Tracking
Constitution supersedes all other development practices. The latest version always takes precedence. Track amendments with dates and rationale. Maintain backward compatibility unless explicitly documented as breaking change.

**Version**: 1.1.0 | **Ratified**: 2025-09-24 | **Last Amended**: 2025-09-25