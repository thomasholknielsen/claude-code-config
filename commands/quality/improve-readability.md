---
description: "Manual code beautification - readability improvements, naming, structure optimization"
argument-hint: "[path] [--focus=<area>] [--preserve-functionality] [--interactive]"
allowed-tools: Read, Edit, MultiEdit, Bash
---

# Command: Improve Readability

## Purpose

Performs manual code beautification focusing on readability improvements, meaningful naming, and structure optimization beyond automated formatting.

## Usage

```bash
/clean:improve-readability $ARGUMENTS
```

**Arguments**:

- `$1` (path): Specific file or directory to improve (optional)
- `$2` (--focus): Focus area (naming, structure, comments, expressions) (optional)
- `$3` (--preserve-functionality): Ensure no behavioral changes (optional)
- `$4` (--interactive): Prompt for approval on significant changes (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/"` - Improve readability in src directory
- `$ARGUMENTS = "components/ --focus=naming"` - Focus on variable naming in components
- `$ARGUMENTS = "utils.js --preserve-functionality --interactive"` - Interactive improvements with safety

## Process

1. **Parallel Readability Analysis**: Use Task() to assess different readability aspects:

   ```python
   Task("analyze-naming", "Evaluate variable, function, and class names for clarity")
   Task("analyze-structure", "Assess code organization, nesting, and logical flow")
   Task("analyze-complexity", "Identify overly complex expressions and statements")
   ```

## Agent Integration

**Critical Constraint**: **Subagents provide analysis ONLY - no implementation allowed**

- **Phase 1**: Domain analysts conduct analysis and return recommendations to main thread
- **Phase 2**: **Main thread synthesizes analyst findings and implements all changes**
- **Phase 3**: Main thread applies all readability improvements based on analysis

**Domain Specialists** (analysis only):
- quality-analyst - Code quality assessment and improvement recommendations
- refactoring-analyst - Readability enhancement techniques and strategies
- architecture-analyst - Structure organization and pattern recommendations

**Implementation Responsibility**: Main thread executes all recommendations using Edit/MultiEdit tools

2. **Improvement Identification**: Find readability enhancement opportunities:
   - Unclear or abbreviated variable names
   - Overly complex expressions that could be simplified
   - Poor code organization and logical flow
   - Missing or misleading comments
   - Inconsistent patterns within the codebase

3. **Manual Beautification**: Apply human-guided improvements based on $ARGUMENTS scope:
   - Rename variables and functions for clarity
   - Break complex expressions into understandable parts
   - Reorganize code for better logical flow
   - Add strategic comments for complex logic
   - Improve error messages and user-facing text

4. **Structure Optimization**: Enhance code organization:
   - Group related functionality together
   - Extract inline code into well-named functions
   - Improve class and module organization
   - Optimize import statements and dependencies

5. **Validation**: Ensure improvements maintain functionality:
   - Run tests to verify behavior preservation
   - Check that readability improvements don't affect performance
   - Validate naming consistency across the codebase

## Agent Integration

- **Primary Agent**: quality-analyst - Can be spawned to apply human-guided readability improvements with careful functionality preservation

## Parallelization Patterns

**Multi-Aspect Analysis**: Simultaneously analyze naming, structure, and complexity to build comprehensive improvement plan.

**Impact Assessment**: Run parallel analysis of potential changes to ensure safe improvements that maintain functionality.

## Examples

```bash
# Improve readability across current directory
/clean:improve-readability

# Focus on variable naming
/clean:improve-readability $ARGUMENTS
# where $ARGUMENTS = "src/ --focus=naming"

# Interactive mode for complex changes
/clean:improve-readability $ARGUMENTS
# where $ARGUMENTS = "components/ --interactive"
```
