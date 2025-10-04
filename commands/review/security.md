---
description: "Comprehensive security analysis with vulnerability remediation"
argument-hint: "[scope] [--severity=level] [--fix] [--report]"
category: "review"
tools: ["Read", "Write", "Grep", "Glob", "MultiEdit"]
complexity: "complex"
allowed-tools: Read, Write, Grep, Glob, MultiEdit
---

# Command: Review Security

## Purpose

Performs comprehensive security vulnerability assessment with parallel analysis of authentication,
authorization, data protection, and infrastructure security vectors.

## Usage

```bash
/review:security $ARGUMENTS
```

**Arguments**:

- `$1` (scope): Security focus area (auth|data|infrastructure|dependencies|all) (optional)
- `$2` (--severity): Minimum severity to report (critical|high|medium|low) (optional)
- `$3` (--fix): Automatically remediate low-risk vulnerabilities (optional)
- `$4` (--report): Generate detailed security assessment report (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "auth --severity=high"` - Focus on authentication with high severity issues
- `$ARGUMENTS = "all --report"` - Comprehensive security assessment with report
- `$ARGUMENTS = "dependencies --fix"` - Dependency security scan with auto-fix

## Process

1. **Parse Security Scope**: Extract scope and options from $ARGUMENTS
2. **Threat Modeling**: Identify attack surfaces and security boundaries
3. **Parallel Vulnerability Assessment**: Launch concurrent security scans across multiple vectors
4. **Risk Analysis**: Evaluate and prioritize findings by business impact and exploitability
5. **Remediation Planning**: Generate fix strategies and security improvements
6. **Compliance Validation**: Verify adherence to security standards and best practices

## Parallelization Patterns

**Multi-Vector Security Analysis**: Comprehensive parallel security assessment:

```python
# Core security vectors
Task("Analyze authentication mechanisms, session management, and access controls")
Task("Review authorization patterns, role-based access, and privilege escalation risks")
Task("Assess input validation, SQL injection, and XSS vulnerability patterns")
Task("Evaluate cryptographic implementations, key management, and data protection")
Task("Analyze network security, HTTPS implementation, and communication channels")
Task("Review API gateway security including CORS configuration, rate limiting, timeout policies, and upstream service protection")
```

**Dependency and Infrastructure Security**: Parallel external threat analysis:

```python
# External security assessment
Task("Scan dependencies for known vulnerabilities using CVE databases")
Task("Analyze container and infrastructure security configurations")
Task("Review API security, rate limiting, and endpoint protection mechanisms")
Task("Evaluate secrets management, environment variables, and credential storage")
Task("Assess logging, monitoring, and incident response capabilities")
```

**Application-Specific Security**: Technology-aware parallel analysis:

```python
# Frontend security
Task("Review client-side security, CSP headers, and browser security features")
Task("Analyze frontend authentication flows and token management")
Task("Evaluate third-party script security and supply chain risks")

# Backend security
Task("Review server-side security controls and request processing")
Task("Analyze database security, query patterns, and data access controls")
Task("Evaluate microservices security and inter-service communication")
```

**Compliance and Standards**: Parallel regulatory assessment:

```python
# Security compliance
Task("Evaluate OWASP Top 10 compliance and mitigation strategies")
Task("Assess GDPR/privacy compliance and data handling practices")
Task("Review industry-specific security requirements and standards")
Task("Analyze audit logging and compliance reporting capabilities")
```

## Agent Integration

- **Specialist Options**: reviewer specialist can be spawned to orchestrate parallel security analysis and vulnerability prioritization
- **Coordination**: Integrates with Context7 MCP for latest OWASP guidelines and CVE data
- **Integration**: Works with `bug-fixer` for vulnerability remediation, `documenter` for security documentation

## Examples

```bash
# Full security assessment
/review:security $ARGUMENTS
# where $ARGUMENTS = "all --report"

# Focus on authentication security
/review:security $ARGUMENTS
# where $ARGUMENTS = "auth --severity=high"

# Quick fix for low-risk issues
/review:security $ARGUMENTS
# where $ARGUMENTS = "--severity=low --fix"

# Infrastructure security review
/review:security $ARGUMENTS
# where $ARGUMENTS = "infrastructure"
