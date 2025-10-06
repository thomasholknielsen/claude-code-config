<!--
Sync Impact Report:
Version: 2.1.0 (Updated to reflect Domain Analyst Framework with 15 agents)
Modified principles: Updated Agent Specialist Framework to Domain Analyst Framework with 15 domain analysts (1 research + 14 specialists)
Added sections: Research analyst role, expanded domain specialist coverage (React, TypeScript, Python, API, security, performance, testing, accessibility, documentation, database, frontend, quality, architecture, refactoring)
Removed sections: Strategic/Technical specialist division (replaced with research + domain analyst pattern)
Templates requiring updates:
  ✅ plan-template.md - Constitution Check section updated to reflect Domain Analyst Framework
  ✅ spec-template.md - Updated to reference domain analyst patterns
  ✅ tasks-template.md - Task ordering follows atomic command principles
Follow-up TODOs: Update existing specs to reference v2.1.0
-->

# Claude Code Command System Constitution

## Core Principles

### I. Domain Analyst Framework Architecture

The repository is built on the **Domain Analyst Framework** with 15 specialized domain analysts providing comprehensive advisory expertise:

**Research Analyst (1):**
- `research-analyst` - Conducts comprehensive sequential research across multiple domains and provides synthesized findings. Uses Context7 for framework documentation.

**Domain Analysts (14):**

**Framework/Technology Analysts:**
- `react-analyst` - React patterns, hooks, state management, component design analysis
- `typescript-analyst` - Type safety, generics, interface design, TypeScript best practices
- `python-analyst` - Pythonic patterns, PEP 8 compliance, library best practices, type hints analysis
- `api-analyst` - REST/GraphQL patterns, endpoint design, versioning strategies, contract validation

**Code Quality & Architecture Analysts:**
- `quality-analyst` - Complexity analysis, code smells detection, maintainability metrics, SOLID principles validation
- `architecture-analyst` - SOLID principles, design patterns, system design recommendations (uses opus + ultrathink)
- `refactoring-analyst` - Code smell detection, refactoring opportunities, design pattern recommendations, technical debt assessment

**Security & Performance Analysts:**
- `security-analyst` - OWASP Top 10 analysis, threat modeling, vulnerability detection, auth/authz review, mitigation strategies
- `performance-analyst` - Bottleneck detection, optimization strategies, profiling recommendations, caching patterns, query optimization

**Testing & Accessibility Analysts:**
- `testing-analyst` - Test coverage assessment, test quality evaluation, edge case identification, testing strategy recommendations
- `accessibility-analyst` - WCAG compliance assessment, ARIA pattern evaluation, keyboard navigation analysis, screen reader compatibility

**Documentation & Data Analysts:**
- `documentation-analyst` - Documentation completeness assessment, API documentation quality, comment effectiveness, knowledge gap identification
- `database-analyst` - Schema design evaluation, query optimization, indexing strategies, migration assessment, database performance
- `frontend-analyst` - Component architecture evaluation, state management patterns, bundle optimization, UI framework best practices

**Usage Patterns:**
- Research analyst for multi-domain sequential research and synthesized findings
- Domain analysts for deep domain-specific analysis with context elision (conduct extensive research, return 2-3 sentence summaries)
- All domain analysts persist findings to `.artifacts/context/{domain}-analysis-*.md` for main thread access
- Domain analysts are **advisory** - they provide recommendations and guidance, not direct execution

**Rationale**: Domain analysts provide deep domain expertise while maintaining context elision pattern (detailed research → concise summaries). This enables parallel research workflows and keeps main thread context clean for implementation.

### II. Atomic Command Design

All commands (except workflows) must be atomic, single-purpose operations:

**Command Characteristics:**
- Single, clear responsibility with predictable outcomes
- Can be used directly by users or recommended by strategic specialists
- Include integration points showing relationships to other commands
- Follow standardized template structure with required sections

**Workflow Commands Exception:**
- Workflows orchestrate other atomic commands using SlashCommand tool
- Use `task-orchestrator` agent instead of specialized agents
- Document sequential execution strategy

**Rationale**: Atomic design enables composability, maintainability, and clear understanding of system capabilities. Workflows provide sophisticated automation by combining atomic operations.

### III. Specification-Driven Feature Development

Features follow the spec-kit workflow when `.specify/` folder exists:

**Required Artifacts:**
- `spec.md` - User requirements and acceptance criteria (WHAT/WHY, not HOW)
- `plan.md` - Technical design and implementation strategy
- `tasks.md` - Ordered, dependency-aware task breakdown
- `contracts/` - API and validation contracts

**Clarification Protocol:**
- Mark ambiguities as [NEEDS CLARIFICATION]
- Run `/spec-kit:clarify` to resolve uncertainties before planning
- Ensure requirements are testable and unambiguous

**Rationale**: Structured specification process prevents scope creep, ensures alignment, and provides clear acceptance criteria. This reduces rework and validates features meet actual needs.

### IV. Cross-Platform Compatibility

All automation must work on macOS, Windows, and Linux:

**Implementation Requirements:**
- Use Python with `pathlib.Path` for all file operations
- Use `Path.home()` for user directory references
- No shell-specific scripts or commands
- User-agnostic paths: `~/.claude/` instead of `/Users/specific-user/.claude/`

**Rationale**: Cross-platform compatibility ensures the command system works consistently across all development environments without platform-specific modifications.

### V. MCP Integration Patterns

Leverage Model Context Protocol servers for enhanced capabilities:

**Context7 MCP** - External documentation access:
- Use for current library/framework documentation
- Tools: `mcp__context7__resolve-library-id`, `mcp__context7__get-library-docs`
- Commands: `/docs:extract-external`, `/review:security`, `/analyze:dependencies`

**Playwright MCP** - Browser automation:
- Use for UI testing, visual regression, user interaction simulation
- Full navigation, interaction, and analysis capabilities
- Integration: Design review, testing workflows

**Rationale**: MCP integration provides access to current external information and advanced testing capabilities that enhance command functionality.

## Development Workflow Standards

### Command Development Protocol

**Template Compliance:**
- Follow `docs/command-template.md` for atomic commands
- Use workflow template for orchestration commands
- Required frontmatter: description, argument-hint, category, tools, complexity
- Document $ARGUMENTS parsing patterns
- Include agent integration and examples

**Agent Assignment:**
- Assign to existing Agent Specialist Framework agent
- Single responsibility per command
- No duplicate functionality across commands

### Git Operations Constraint

**CRITICAL SECURITY RULE**: Only `/git/*` commands can perform Git operations

**Enforcement:**
- All other agents/commands must use SlashCommand tool for Git delegation
- Explicit user consent required for Git operations outside `/git/*`
- Agents cannot call Git commands directly

**Rationale**: Centralized Git control prevents accidental or unauthorized repository modifications.

### File Management Standards

- Prefer editing existing files over creating new files
- Always use Read tool before editing
- Verify parent directory existence before creating directories
- Quote file paths with spaces in shell commands
- Use appropriate branch naming: `###-feature-name` format

## Quality Standards

### Command Quality Requirements

- **Atomic Design**: Single, clear purpose with predictable outcomes
- **Complete Documentation**: Follow template structure with all required sections
- **Integration Clarity**: Document relationships to other commands
- **Functional Verification**: Ensure command works as documented

### Agent Quality Requirements

- **Single Responsibility**: One clear, focused capability per agent
- **Specialization Compliance**: Follow analysis/execution specialist pattern
- **Tool Appropriateness**: Select tools matching agent domain expertise
- **Documentation Clarity**: Clear purpose, usage patterns, and examples

### System Quality Requirements

- **Cross-Platform**: Works on Windows, macOS, Linux without modification
- **User-Agnostic**: No hardcoded user-specific paths
- **Security Enforcement**: Git constraints respected, no unauthorized operations
- **Performance**: Efficient execution with minimal resource usage

### TODO Management Constraint

**CRITICAL**: All TODO operations use standardized location only:
- **Required**: `{project_root}/.claude/.todos/TODO.md`
- **Prohibited**: TODO files in any other location
- **Enforcement**: All `/to-do:*` commands validate this constraint

**Rationale**: Centralized task tracking prevents scattered TODO files and ensures consistent file management.

## Success Metrics

Track system effectiveness through:

- **Command Usage**: Most/least used commands, adoption patterns
- **Agent Collaboration**: Analysis specialist → execution specialist advisory workflows
- **Documentation Quality**: User feedback, template compliance rates
- **System Performance**: Command execution speed and reliability
- **Error Rates**: Failed commands, common issues, resolution patterns

## Governance

### Amendment Process

Constitution updates require:

1. **Version Bump** - Semantic versioning (MAJOR: breaking, MINOR: additions, PATCH: clarifications)
2. **Impact Analysis** - Document affected templates, specs, and commands
3. **Sync Report** - List all artifacts requiring updates
4. **Validation** - Ensure template references align with new principles
5. **Communication** - Update CLAUDE.md and related documentation

### Critical Constraints

**What NOT to do:**
- Don't bypass Git constraints (only `/git/*` commands perform Git operations)
- Don't hardcode user-specific paths (use `~/.claude/` patterns)
- Don't duplicate agent responsibilities (each agent has unique purpose)
- Don't ignore MCP integration opportunities (Context7, Playwright)
- Don't break atomic design (keep commands single-purpose)

**Required Practices:**
- Use Agent Specialist Framework for all development work
- Follow provided templates for consistency
- Test cross-platform compatibility (Windows, macOS, Linux)
- Document thoroughly with examples and integration points
- Validate security constraints are respected
- Maintain CLAUDE.md synchronization after changes

### Version Control

Constitution supersedes other development practices. Latest version always takes precedence. Track amendments with dates and rationale. Maintain backward compatibility unless explicitly documented as breaking change.

**Version**: 2.1.0 | **Ratified**: 2025-10-03 | **Last Amended**: 2025-10-05 | **Based On**: Project CLAUDE.md actual practices with Domain Analyst Framework
