---
description: "Rapid bug fixes without full implementation session complexity"
argument-hint: "[issue] [--scope=<area>] [--strategy=<approach>] [--test-first]"
category: "fix"
tools: ["Read", "Edit", "MultiEdit", "Bash"]
complexity: "moderate"
---

# Command: Bug Quickly

## Purpose

Provides rapid bug fixes without full implementation session complexity, focusing on immediate resolution of specific issues.

## Usage

```bash
/fix:bug-quickly [issue] [--scope=<area>] [--strategy=<approach>] [--test-first]
```

**Arguments**:

- `issue` (optional): Specific bug description or error message
- `--scope` (optional): Limit search scope (file, module, component)
- `--strategy` (optional): Fix approach (minimal, comprehensive, root-cause)
- `--test-first` (optional): Create failing test before implementing fix

**$ARGUMENTS Usage**:
The command processes arguments through the $ARGUMENTS placeholder:

- `$ARGUMENTS` - Contains all user-provided arguments as a single string
- `$1` - First positional argument (issue description)
- `$2` - Second positional argument (if provided)
- Named flags are parsed from $ARGUMENTS for scope, strategy, and test-first options

## Process

1. **Argument Processing & Diagnostic Analysis**: Parse $ARGUMENTS and use Task() to simultaneously investigate multiple aspects:

   ```python
   # Parse arguments from $ARGUMENTS
   issue_description = $1 if $1 else "general debugging"
   scope = parse_flag("--scope", $ARGUMENTS) or "project-wide"
   strategy = parse_flag("--strategy", $ARGUMENTS) or "comprehensive"
   test_first = "--test-first" in $ARGUMENTS

   # Parallel diagnostic tasks
   Task("analyze-symptoms", f"Examine error messages, logs, and failure patterns for: {issue_description}"),
   Task("analyze-recent-changes", "Review recent commits and changes that might be related"),
   Task("analyze-similar-issues", f"Search for similar patterns in {scope} scope")
   ```

2. **Root Cause Investigation**: Quickly identify the source of the problem using parsed arguments:
   - Trace error messages to specific code locations (focused on $1 if provided)
   - Analyze data flow and state changes within specified --scope
   - Identify timing, concurrency, or dependency issues
   - Check for common bug patterns (null references, off-by-one, etc.)
   - Apply investigation strategy based on --strategy argument

3. **Fix Strategy Selection**: Choose appropriate resolution approach based on $ARGUMENTS:
   - **Minimal Fix**: Address immediate symptom with smallest change (--strategy=minimal)
   - **Comprehensive Fix**: Address root cause and prevent similar issues (--strategy=comprehensive)
   - **Root Cause Fix**: Deep investigation and structural changes (--strategy=root-cause)
   - **Test-Driven Fix**: Create test case first when --test-first is specified
   - Default to comprehensive approach if no --strategy specified

4. **Rapid Implementation**: Apply fix with immediate validation:
   - Implement the most targeted fix possible
   - Add logging or debugging aids if needed
   - Include error handling for edge cases
   - Ensure fix doesn't introduce regressions

5. **Quick Validation**: Verify fix effectiveness:
   - Run relevant tests to confirm issue resolution
   - Test edge cases and similar scenarios
   - Verify no new issues are introduced

## Agent Integration

- **Primary Specialist**: bug-fixer - A specialized agent that can be spawned for rapid issue diagnosis and targeted fix implementation with minimal disruption

## Parallelization Patterns

**Multi-Vector Diagnosis**: Simultaneously analyze logs, recent changes, and similar issues to quickly narrow down root cause.

**Parallel Testing**: Run multiple test scenarios concurrently to verify fix effectiveness and catch potential regressions.

## Examples

```bash
# Quick fix for a specific error ($1 = "TypeError: cannot read property of undefined")
/fix:bug-quickly "TypeError: cannot read property of undefined"

# Minimal fix with focused scope (--scope=auth-module, --strategy=minimal)
/fix:bug-quickly --scope=auth-module --strategy=minimal

# Test-driven bug fix ($1 = "login fails with valid credentials", --test-first flag)
/fix:bug-quickly "login fails with valid credentials" --test-first

# Comprehensive fix with scoped investigation
/fix:bug-quickly "API timeout errors" --scope=api-layer --strategy=root-cause

# General debugging without specific issue
/fix:bug-quickly --scope=components --test-first
```

**$ARGUMENTS Processing Examples**:

- `"TypeError: undefined"` → $1="TypeError: undefined", $ARGUMENTS="TypeError: undefined"
- `--scope=auth --strategy=minimal` → $ARGUMENTS="--scope=auth --strategy=minimal"
- `"login error" --test-first` → $1="login error", --test-first flag detected
