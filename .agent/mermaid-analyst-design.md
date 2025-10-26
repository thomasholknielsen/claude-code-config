# Agent Design Analysis: Mermaid Chart Analyst

**Objective**: Design specialized agent to help users create great, user-friendly Mermaid diagrams

**Status**: Ready for Template Generation

---

## Domain Validation Summary

**Uniqueness Check (vs 43 existing agents)**:
- docs-analyst: RECOMMENDS Mermaid but doesn't specialize in creation
- architecture-analyst: May need diagrams but focuses on SOLID/patterns
- ui-ux-analyst: Visual design focus, not Mermaid-specific  
- frontend-analyst: No overlap - different domain

**Validation**: UNIQUE domain, fills capability gap for diagram-specific guidance

---

## Design Recommendations

**Agent Name**: mermaid-analyst
**Agent Type**: Domain Analyst
**Color**: cyan
**Model**: inherit

### Rationale

- **Naming**: Follows kebab-case convention consistent with docs-analyst, ui-ux-analyst
- **Type**: Analysis-only (recommends, does not implement) - matches framework pattern
- **Color**: Cyan for visualization/design domain, distinct from other analysts
- **Model**: Inherit sufficient for systematic analysis, doesn't require opus

---

## Core Expertise Areas (5)

1. **Diagram Type Selection & Matching**
   - Flowchart (TD, LR), Sequence, State, Journey, Gantt, Class diagrams
   - Matching type to use case

2. **Layout & Structure Optimization**
   - Subgraph grouping, directional flow, node/edge labeling (5-7 words)
   - Visual complexity management, flow clarity

3. **Accessibility & Visual Design**
   - High-contrast, colorblind-safe palettes
   - Shape + color combinations, legends, WCAG compliance

4. **Process Modeling Best Practices**
   - Decision points, error paths, input/output documentation
   - SLAs, actor/system separation, feedback loops

5. **Diagram Patterns & Examples**
   - Well-structured examples, common patterns/anti-patterns
   - Maintainability, scalability considerations

---

## MCP Tool Selection

**Selected Tools**:
- Read, Grep, Glob, WebSearch, Bash, Edit
- mcp__playwright__browser_navigate
- mcp__playwright__browser_take_screenshot
- mcp__playwright__browser_snapshot
- mcp__sequential-thinking__sequentialthinking

**Rationale**:
- Playwright: Visual validation of diagram rendering, contrast, layout
- WebSearch: Research Mermaid best practices, accessibility standards
- Sequential-Thinking: Complex diagram analysis (type selection, layout decisions)

---

## Usage Examples (3 scenarios)

### Example 1: Process Flow Optimization
User: "My order processing diagram is confusing with crossing lines"
Agent: Recommends subgraph reorganization, layout optimization, label clarity

### Example 2: Diagram Type Selection
User: "Should OAuth2 use sequenceDiagram or flowchart?"
Agent: Recommends sequenceDiagram - shows interactions, timing, parallel paths

### Example 3: Accessibility Audit
User: "I created a CI/CD pipeline stateDiagram - ensure it's accessible"
Agent: Audits accessibility (contrast, shape distinction), structure, maintainability

---

## Expertise Boundaries

**In Scope**:
- Diagram type selection, layout optimization, accessibility
- Process modeling best practices, Mermaid syntax, patterns

**Out of Scope**:
- Documentation quality (docs-analyst)
- UI/UX design (ui-ux-analyst)
- Architecture patterns (architecture-analyst)
- Diagram generation (analysis-only role)

---

## Actionable Tasks

### Ready for Implementation
- [x] Domain name validated - mermaid-analyst
- [x] Core expertise defined - 5 areas
- [x] MCP tools selected - Playwright, WebSearch, Sequential-Thinking
- [x] Usage examples crafted - 3 realistic scenarios
- [x] Color assigned - cyan
- [x] Template compatibility confirmed

### Validations Complete
- [x] Uniqueness vs 43 agents - NO overlaps
- [x] Gap analysis - Fills Mermaid-specific guidance gap
- [x] Naming conventions - Follows kebab-case + -analyst suffix
- [x] Domain boundaries - Clear scope with delegations

---

## Summary

- **Agent**: mermaid-analyst
- **Type**: Domain Analyst
- **Color**: cyan
- **Model**: inherit
- **Expertise**: Diagram type selection, layout, accessibility, process modeling, patterns
- **Status**: FINALIZED ✓

---

## Main Thread Log

### 2025-10-24
**Completed**: Agent finalized and integrated
**Actions**:
- Generated agent file: `agents/mermaid-analyst.md` (744 lines, S-tier template)
- Updated CLAUDE.md: Added new "Visualization" category to Domain Analyst Framework
- Updated agent count: 43 → 44 agents (41 domain analysts + 3 meta)
- CLAUDE.md changes: Committed to project configuration

**Integration Status**: Ready for Claude Code restart to load new agent
