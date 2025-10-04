---
description: "Execute comprehensive security audit to identify vulnerabilities and ensure secure coding practices"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/review:security), SlashCommand(/analyze:dependencies)
---

# Command: Run Security Audit

## Purpose

Executes comprehensive security audit by orchestrating atomic security commands to identify vulnerabilities, ensure secure coding practices, and
validate compliance standards.

## Usage

```bash
/workflows:run-security-audit
```

## Process

1. **Security Vulnerability Review**: Execute `/review:security` command for comprehensive OWASP Top 10 vulnerability assessment
2. **Dependency Security Analysis**: Execute `/analyze:dependencies` command for third-party dependency vulnerability scanning
3. **Results Coordination**: Compile findings from both security commands for prioritized remediation planning

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates execution of atomic security commands and consolidates audit results

## Implementation Steps

**Step 1: Security Code Review**
Execute comprehensive security vulnerability assessment:

```bash
SlashCommand("/review:security")
```

This command performs:

- OWASP Top 10 vulnerability assessment
- Authentication and authorization review
- Input validation and output encoding analysis
- Cryptographic implementation review
- Security configuration assessment

**Step 2: Dependency Security Analysis**
Execute dependency vulnerability scanning:

```bash
SlashCommand("/analyze:dependencies")
```

This command performs:

- Known vulnerability detection in dependencies
- Outdated package identification
- License compliance analysis
- Security advisory review

**Step 3: Results Integration**
The orchestrator consolidates findings from both commands to provide:

- Prioritized vulnerability list by CVSS score
- Remediation recommendations
- Security compliance status

## Examples

**Basic Security Audit:**

```bash
/workflows:run-security-audit
```

**Example Execution Flow:**

1. Orchestrator executes `/review:security` for comprehensive code security analysis
2. Orchestrator executes `/analyze:dependencies` for dependency vulnerability scanning
3. Results are consolidated into prioritized security report

## Integration Points

**Prerequisites:**

- Codebase available for security analysis
- Package manager files present (package.json, requirements.txt, etc.)
- Project dependencies installed

**Follows Well With:**

- `/clean:development-artifacts` - Clean up before security audit
- `/docs:update` - Update security documentation after audit
- `/git:commit` - Commit security fixes after remediation

**Works With:**

- `/review:code` - Comprehensive code quality review
- `/analyze:potential-issues` - General issue identification
- `/workflows:run-comprehensive-review` - Full project review including security

## Output

Provides consolidated security audit report including:

- Security vulnerability assessment results
- Dependency security analysis findings
- Prioritized remediation recommendations
- Compliance status summary
