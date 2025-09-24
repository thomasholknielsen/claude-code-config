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

### III. Test-First Implementation (NON-NEGOTIABLE)
Implementation follows strict TDD methodology: Write tests → User approval → Tests fail → Implement to pass. Contract tests must be generated from API specifications. Integration tests must validate user scenarios. All code changes require comprehensive test coverage before completion.

**Rationale**: TDD ensures code correctness, prevents regressions, and serves as living documentation. This non-negotiable principle maintains code quality and reduces debugging time.

### IV. Constitutional Compliance Gates
All features must pass constitution compliance checks at two stages: initial specification review and post-design review. Violations must be documented with justification in the Complexity Tracking section. No complexity can be added without demonstrating that simpler alternatives are insufficient.

**Rationale**: Prevents unnecessary complexity accumulation and ensures architectural consistency. Gates provide natural checkpoints for quality assurance and technical debt prevention.

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

### Multi-Modal Review Process
Three specialized review workflows operate in parallel:
1. **Code Review**: Syntax, bugs, performance, style, completeness via code-reviewer-advanced
2. **Security Review**: OWASP compliance, vulnerability assessment via security-scanner
3. **Design Review**: UI/UX compliance, accessibility validation via ui-compliance-checker

### Automated Quality Gates
- Pre-commit: Quick code review and security scan for sensitive changes
- Pre-merge: Full review workflow with all three review types
- Post-deployment: Performance monitoring and user feedback analysis
- Dependency updates: Automated security scanning for CVE detection

### Continuous Improvement Loop
Track effectiveness metrics: task completion quality, time to completion, error reduction rates, and user satisfaction. Use analytics-engine for comprehensive data analysis and trend identification.

## Governance

### Amendment Process
Constitution changes require:
1. Version bump following semantic versioning (MAJOR for breaking changes, MINOR for additions, PATCH for clarifications)
2. Documentation of impact on templates and dependent files
3. Sync Impact Report documenting all affected artifacts
4. Validation that all template references align with new principles

### Compliance Enforcement
- All PRs must verify constitutional compliance
- Complexity deviations require documented justification
- Regular reviews of agent performance and selection patterns
- Template consistency checks during constitution updates

### Version Control and Tracking
Constitution supersedes all other development practices. The latest version always takes precedence. Track amendments with dates and rationale. Maintain backward compatibility unless explicitly documented as breaking change.

**Version**: 1.0.0 | **Ratified**: 2025-09-24 | **Last Amended**: 2025-09-24