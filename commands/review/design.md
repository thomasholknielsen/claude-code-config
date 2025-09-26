# Design Review Command

Perform comprehensive UI/UX compliance review on $ARGUMENTS to ensure design system adherence, accessibility standards, and visual consistency.

## Design Review Process

Execute a thorough frontend design review following these steps:

### 1. Scope Analysis
- Identify components, pages, or features to review
- Detect the design system or UI framework in use
- Locate style guides, design tokens, and component libraries
- Understand responsive breakpoints and device targets

### 2. Launch UI Compliance Checker
- Deploy the **ui-compliance-checker** subagent for comprehensive design analysis
- The checker will validate:
  - Design system component usage
  - Visual consistency (colors, typography, spacing)
  - Accessibility compliance (WCAG 2.1 Level AA)
  - Responsive design implementation
  - User experience patterns
  - Performance impact of UI choices

### 3. Visual Inspection with Playwright
If the application is running locally:
- Use Playwright MCP to navigate to the UI
- Capture screenshots at multiple breakpoints (mobile, tablet, desktop)
- Document interaction states (hover, focus, active, disabled)
- Check animations and transitions
- Validate loading and error states

### 4. Accessibility Audit
Perform comprehensive accessibility checks:
- **WCAG Level A**: Basic accessibility requirements
- **WCAG Level AA**: Standard compliance level
- Screen reader compatibility
- Keyboard navigation testing
- Focus management validation
- Color contrast analysis
- ARIA implementation review

### 5. Design System Compliance
Verify adherence to design standards:
- **Components**: Proper use of design system components
- **Tokens**: Design token usage (colors, spacing, typography)
- **Patterns**: Consistent UI patterns across the application
- **Custom Code**: Identify unauthorized custom implementations
- **Consistency**: Cross-page/component consistency

### 6. Performance Impact Assessment
Analyze frontend performance implications:
- Bundle size impact
- Core Web Vitals (LCP, FID, CLS)
- Image optimization
- Font loading strategies
- CSS complexity
- Render-blocking resources

### 7. Generate Design Report
Create a comprehensive design review report:
- **Summary**: Overall design compliance score
- **Visual Issues**: Design system violations with screenshots
- **Accessibility Findings**: WCAG violations with severity
- **Responsive Problems**: Device-specific issues
- **Performance Concerns**: UI-related performance impacts
- **Positive Observations**: Well-implemented patterns

### 8. Create Remediation Tasks
Generate a TodoWrite list with:
- Critical accessibility fixes (legal compliance)
- Design system violations to correct
- Responsive design issues to address
- Performance optimizations needed
- UX improvements to implement

## Review Coverage

### Visual Design
- Typography hierarchy and readability
- Color usage and brand consistency
- Spacing and layout grid compliance
- Icon usage and sizing
- Shadow and elevation standards
- Border and corner radius consistency

### Interaction Design
- Button states and feedback
- Form validation and error handling
- Loading and progress indicators
- Transitions and animations
- Micro-interactions
- Touch targets and gesture support

### Accessibility
- Alternative text for images
- Form labels and instructions
- Error identification
- Keyboard accessibility
- Screen reader compatibility
- Focus indicators
- Skip navigation

### Responsive Design
- Mobile-first implementation
- Breakpoint consistency
- Content reflow
- Touch-friendly interfaces
- Performance on mobile networks
- Viewport configuration

## Output Format

The review will provide:

```markdown
## UI/UX Compliance Report

### 📊 Overall Score
- Design Compliance: X%
- Accessibility: X/100
- Responsive: Pass/Fail
- Performance Impact: Low/Medium/High

### 🎨 Design System Violations
[Detailed list with locations and fixes]

### ♿ Accessibility Issues
[WCAG violations with remediation]

### 📱 Responsive Design Problems
[Device-specific issues with screenshots]

### ⚡ Performance Concerns
[UI-related performance impacts]

### ✅ Well-Implemented Patterns
[Positive findings to maintain]

### 📋 Action Items
[Prioritized list of fixes]
```

## Example Usage

```
/design-review src/components
/design-review "checkout flow" --screenshot
/design-review HomePage.tsx --accessibility
/design-review . --design-tokens
```

## Integration

This command can work with:
- **frontend-developer** for implementing fixes
- **ui-designer** for design decisions
- **performance-benchmarker** for optimization
- **code-reviewer-advanced** for code quality

## Best Practices

- Focus on user impact over technical perfection
- Prioritize accessibility compliance (legal requirement)
- Consider the design system as the source of truth
- Provide visual evidence with screenshots when possible
- Suggest specific, implementable fixes
- Balance consistency with practical constraints

Remember: Good design review ensures both beautiful and usable interfaces. Prioritize accessibility and user experience while maintaining visual consistency and brand standards.