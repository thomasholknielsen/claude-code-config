---
description: Context-aware test execution with intelligent failure resolution
category: testing
tools: Bash, Read, Grep, TodoWrite
---

# Smart Test Runner

I'll intelligently run tests based on context and actively help fix failures.

## Context-Aware Testing

**Test strategies based on context:**
- **Cold start**: Full suite with coverage report
- **Active development**: Test only modified files
- **Post-command**: Context-specific testing (scaffold→new component tests)
- **Debug mode**: Failed tests with verbose output
- **Pre-commit**: Full suite + lint + typecheck

## Test Execution Process

**Project analysis:**
- Detect test frameworks and runners
- Find test file patterns and configurations
- Understand coverage requirements and CI/CD setup

**Execution strategy:**
- Build verification before testing
- Intelligent test selection based on changes
- Real-time monitoring with failure capture
- Coverage analysis and quality reporting

**Failure resolution:**
- Parse failure output for root causes
- Apply common fixes (async, imports, types, mocks)
- Run isolated tests for complex failures
- Track fixes systematically

## Advanced Features

**Smart diagnostics:**
- Console pattern detection (memory leaks, port conflicts)
- Log analysis for hidden errors
- Environment-specific issue identification
- Flaky test pattern analysis

**Integration support:**
- Session-aware testing based on goals
- Integration with other commands for workflow
- Automatic todo creation for complex failures

Perfect test validation while maximizing development speed.