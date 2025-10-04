---
description: "Perform comprehensive UI/UX compliance review to ensure design system adherence and accessibility"
argument-hint: "[component] [--aspect=focus] [--device=type] [--fix]"
category: "review"
tools: ["mcp__playwright__browser_snapshot", "mcp__playwright__browser_navigate", "Read", "Grep"]
complexity: "complex"
allowed-tools: mcp__playwright__browser_snapshot, mcp__playwright__browser_navigate, Read, Grep
---

# Command: Review Design

## Purpose

Performs comprehensive UI/UX compliance review with parallel analysis of design system adherence,
accessibility standards, visual consistency, and user experience patterns.

## Usage

```bash
/review:design $ARGUMENTS
```

**Arguments**:

- `$1` (component): Specific component or page to review (optional, default: entire application)
- `$2` (--aspect): Design focus area (accessibility|consistency|usability|performance) (optional)
- `$3` (--device): Device context (desktop|mobile|tablet|all) (optional)
- `$4` (--fix): Automatically apply design system corrections where possible (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "components/header --aspect=accessibility"` - Accessibility review of header
- `$ARGUMENTS = "--device=mobile --fix"` - Mobile design review with auto-fixes
- `$ARGUMENTS = "checkout-flow --aspect=usability --device=all"` - Cross-device usability review

## Process

1. **Parse Design Scope**: Extract component and review options from $ARGUMENTS
2. **Design System Analysis**: Evaluate adherence to established design patterns and guidelines
3. **Parallel Compliance Assessment**: Launch concurrent reviews across accessibility, visual, and UX dimensions
4. **Cross-Device Validation**: Test responsive behavior and device-specific optimizations
5. **User Experience Evaluation**: Assess usability patterns and interaction flows
6. **Remediation Strategy**: Generate design improvements and accessibility fixes

## Parallelization Patterns

**Multi-Dimensional Design Analysis**: Comprehensive parallel design assessment:

```python
# Core design dimensions
Task("Evaluate accessibility compliance including WCAG 2.1 AA standards and screen reader support")
Task("Analyze visual consistency, color usage, typography, and design system adherence")
Task("Assess responsive design patterns, breakpoints, and cross-device compatibility")
Task("Review user interaction patterns, navigation flow, and information architecture")
Task("Evaluate performance impact of design choices, image optimization, and loading patterns")
```

**Accessibility-Focused Parallel Review**: Comprehensive a11y assessment:

```python
# Accessibility analysis
Task("Analyze semantic HTML structure, heading hierarchy, and landmark usage")
Task("Evaluate keyboard navigation, focus management, and interaction accessibility")
Task("Review color contrast ratios, text readability, and visual accessibility")
Task("Assess screen reader compatibility and assistive technology support")
Task("Validate ARIA attributes, labels, and accessibility metadata")
```

**Visual Design Parallel Assessment**: Design system and visual consistency:

```python
# Visual design evaluation
Task("Review design token usage, color palette consistency, and brand compliance")
Task("Analyze typography scales, font usage, and text hierarchy patterns")
Task("Evaluate spacing systems, layout grids, and component alignment")
Task("Assess iconography, imagery, and visual element consistency")
Task("Review animation patterns, micro-interactions, and transition behaviors")
```

**Device-Specific Parallel Testing**: Cross-platform design validation:

```python
# Multi-device assessment using Playwright MCP
Task("Capture and analyze desktop layout patterns and full-width behaviors")
Task("Evaluate tablet responsive design and medium-screen adaptations")
Task("Review mobile design patterns, touch targets, and small-screen usability")
Task("Assess cross-browser compatibility and vendor-specific design implementations")
```

**User Experience Parallel Evaluation**: Usability and flow analysis:

```python
# UX pattern analysis
Task("Evaluate user onboarding flows, form usability, and input validation patterns")
Task("Analyze navigation patterns, menu structures, and wayfinding systems")
Task("Review error states, loading patterns, and user feedback mechanisms")
Task("Assess content organization, readability, and information hierarchy")
```

## Agent Integration

- **Specialist Options**: reviewer specialist can be spawned to orchestrate parallel design analysis using Playwright MCP for visual testing
- **MCP Integration**: Uses Playwright tools for screenshot capture, visual regression testing, and responsive analysis
- **Coordination**: Works with `code-writer` for design system implementations, `documenter` for design guidelines

## Examples

```bash
# Complete design system review
/review:design $ARGUMENTS
# where $ARGUMENTS = "--aspect=consistency"

# Accessibility-focused review
/review:design $ARGUMENTS
# where $ARGUMENTS = "--aspect=accessibility --fix"

# Mobile-specific design review
/review:design $ARGUMENTS
# where $ARGUMENTS = "components/checkout --device=mobile"

# Full cross-device design validation
/review:design $ARGUMENTS
# where $ARGUMENTS = "--device=all"
