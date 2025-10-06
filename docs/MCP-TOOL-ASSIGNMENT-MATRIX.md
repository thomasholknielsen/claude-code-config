# MCP Tool Assignment Matrix

**Purpose**: Defines which domain analysts have access to MCP (Model Context Protocol) tools and the rationale for each assignment.

## MCP Tools Overview

- **Context7** (`mcp__context7`): Provides access to up-to-date framework and library documentation
- **Playwright** (`mcp__playwright`): Enables browser automation for UI/UX testing and security analysis

## Agent MCP Tool Assignments

| Agent | Context7 | Playwright | Rationale |
|-------|----------|------------|-----------|
| **react-analyst** | ✅ | ✅ | React documentation lookup + visual component testing |
| **typescript-analyst** | ✅ | ❌ | TypeScript documentation only |
| **python-analyst** | ✅ | ❌ | Python library documentation only |
| **api-analyst** | ✅ | ❌ | REST/GraphQL framework documentation only |
| **frontend-analyst** | ✅ | ✅ | Build tool documentation + UI/UX testing |
| **testing-analyst** | ✅ | ✅ | Testing framework documentation + e2e testing |
| **accessibility-analyst** | ✅ | ✅ | WCAG/ARIA documentation + browser accessibility testing |
| **database-analyst** | ✅ | ❌ | Database and ORM documentation only |
| **security-analyst** | ❌ | ✅ | Browser-based security testing (XSS, CSRF) only |
| **performance-analyst** | ❌ | ❌ | Analyzes code patterns, no external docs needed |
| **architecture-analyst** | ❌ | ❌ | Analyzes design patterns, no external docs needed |
| **quality-analyst** | ❌ | ❌ | Analyzes code quality, no external docs needed |
| **documentation-analyst** | ❌ | ❌ | Analyzes documentation, doesn't need external docs |
| **refactoring-analyst** | ❌ | ❌ | Analyzes code smells, no external docs needed |
| **research-analyst** | ✅ | ❌ | General research needs framework documentation |

## Usage Guidelines

### Context7 MCP (9 agents)

**When to use**: Analyst needs current framework or library documentation

**Agents with access**:

- Framework/Technology analysts: react, typescript, python, api
- Specialized analysts: frontend, testing, accessibility, database
- General research: research-analyst

**Usage pattern**:

```markdown
# Analyst analyzes code patterns
# Uses Context7 to fetch current best practices
# Returns findings with framework-aligned recommendations
```

### Playwright MCP (5 agents)

**When to use**: Analyst needs to test UI/UX or perform browser-based analysis

**Agents with access**:

- UI testing: react, frontend, accessibility
- Testing coverage: testing-analyst
- Security testing: security-analyst

**Usage pattern**:

```markdown
# Analyst analyzes UI components
# Uses Playwright to test in browser
# Returns findings with visual validation results
```

## Design Principles

1. **Minimal Assignment**: Only assign MCP tools to agents that genuinely benefit from them
2. **Clear Purpose**: Each MCP tool has specific, well-defined use cases
3. **No Redundancy**: Agents that analyze code patterns don't need external documentation
4. **Domain Alignment**: MCP tools match the analyst's domain expertise

## Adding New MCP Tools

When adding new MCP tools to the system:

1. **Identify Benefit**: Which analysts would genuinely benefit?
2. **Document Usage**: When and how should the tool be used?
3. **Update Matrix**: Add new tool column to this matrix
4. **Update Agents**: Add tool to relevant agent frontmatter with usage description
5. **Update Template**: Include guidance in agent template

## Condensed Syntax

All agents use condensed MCP syntax in frontmatter:

```yaml
# ✅ Correct - Condensed syntax
tools:
  - mcp__context7
  - mcp__playwright

# ❌ Incorrect - Explicit tool names (deprecated)
tools:
  - mcp__context7__resolve-library-id
  - mcp__context7__get-library-docs
  - mcp__playwright__browser_snapshot
```

The condensed syntax provides access to all tools within that MCP server.
