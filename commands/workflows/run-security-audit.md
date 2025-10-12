---
description: "Execute comprehensive security audit using parallel domain analysis to identify vulnerabilities and ensure secure coding practices"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch
---

# Command: Run Security Audit

## Purpose

Executes comprehensive security audit using parallel domain analysis to identify vulnerabilities, ensure secure coding practices,
and validate compliance standards across application, API, and database layers.

## Core Parallelization Principle

**MAXIMIZE PARALLEL EXECUTION**: Both analysis (via concurrent Task calls) AND implementation (via concurrent security fixes) are heavily parallelized for optimal performance.

## Usage

```bash
/workflows:run-security-audit
```

## Process

1. **Parallel Analysis Phase**: Launch 3 domain analysts concurrently for comprehensive security assessment
2. **Parallel Implementation Phase**: Main thread executes multiple security fixes concurrently based on analyst findings
3. **Parallel Validation Phase**: Verify security improvements and compliance standards concurrently

## Agent Integration

- **Primary Agent**: security-analyst - Orchestrates parallel security analysis and synthesizes findings
- **Parallel Domain Analysts** (3 concurrent):
  - security-analyst - OWASP Top 10 assessment, threat modeling, vulnerability detection, cryptographic review
  - api-analyst - API security, authentication/authorization, input validation, rate limiting assessment
  - database-analyst - SQL injection prevention, database security, access control, encryption at rest

## Implementation Steps

### Phase 1: Parallel Security Analysis

```python
# Launch 3 analysts concurrently for comprehensive security assessment
Task("security-analyst: Perform OWASP Top 10 vulnerability assessment, threat modeling, authentication/authorization review, and cryptographic implementation analysis")
Task("api-analyst: Analyze API security including endpoint authentication, input validation, output encoding, CSRF protection, and rate limiting")
Task("database-analyst: Review database security including SQL injection prevention, parameterized queries, access control, and encryption strategies")

# Each analyst:
# - Burns tokens on comprehensive security domain analysis
# - Persists lean findings to .agent/context/{session-id}/{agent-name}.md
# - Returns 2-3 sentence summary with critical findings to main thread
```

### Phase 2: Main Thread Synthesis & Prioritization

```python
# Read all analyst artifacts
Read(.agent/context/${session_id}/security-analyst.md)
Read(.agent/context/${session_id}/api-analyst.md)
Read(.agent/context/${session_id}/database-analyst.md)

# Consolidate findings and prioritize:
# 1. Aggregate all vulnerabilities by CVSS score
# 2. Deduplicate overlapping security issues
# 3. Categorize by severity (Critical/High/Medium/Low)
# 4. Generate remediation recommendations
# 5. Assess dependency vulnerabilities
# 6. Create compliance status report
# 7. Save comprehensive security audit report

# Save to .artifacts/security/audit-{timestamp}.md
```

### Phase 3: Validation

```python
# Verify security audit completeness:
# - All critical/high severity issues documented
# - Remediation steps provided for each vulnerability
# - Compliance standards mapped (OWASP, CWE, etc.)
# - Dependency vulnerabilities identified with CVE references
```

## Examples

**Basic Security Audit:**

```bash
/workflows:run-security-audit
```

**Expected workflow execution:**

```text
Phase 1: Parallel Security Analysis (quick parallel analysis)
→ Task("security-analyst: OWASP Top 10 and threat modeling assessment")
→ Task("api-analyst: API security and authentication review")
→ Task("database-analyst: SQL injection and database security analysis")

Analysts complete concurrently (significantly faster than sequential execution)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ Aggregate vulnerabilities by CVSS score
→ Prioritize by severity (Critical, High, Medium, Low)
→ Generate remediation recommendations

Phase 3: Validation
→ Critical findings: SQL injection in user search, XSS in comments, weak password hashing
→ High findings: Missing rate limiting, insufficient input validation, weak CORS policy
→ All vulnerabilities mapped to OWASP/CWE standards
→ Comprehensive report saved to .artifacts/security/audit-{timestamp}.md
```

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

## Performance Characteristics

**Traditional Sequential Approach:**

- Security code review executed sequentially
- API security analysis follows
- Database security review completes last
- Total execution time scales linearly

**Parallel Analysis Approach:**

- 3 analysts run concurrently (quick parallel analysis)
- Main thread synthesis completes analysis
- Execution time approaches slowest analyst (Amdahl's Law)
- **Performance Gain: Substantially faster through concurrent execution**

## Domain Analyst Outputs

**security-analyst** persists to `.agent/context/security-assessment-{timestamp}.md`:

- OWASP Top 10 vulnerability findings with CVSS scores
- Authentication and authorization weaknesses
- Cryptographic implementation issues
- Security configuration problems
- Threat model analysis

**api-analyst** persists to `.agent/context/api-analysis-{timestamp}.md`:

- API endpoint authentication gaps
- Input validation vulnerabilities
- CSRF and XSS protection assessment
- Rate limiting and throttling issues
- API security best practices violations

**database-analyst** persists to `.agent/context/database-analysis-{timestamp}.md`:

- SQL injection vulnerability locations
- Parameterized query usage analysis
- Database access control weaknesses
- Encryption at rest assessment
- Database security configuration issues

## Output

Provides consolidated security audit report including:

- Security vulnerability assessment results with CVSS scores
- API and database security findings
- Dependency security analysis with CVE references
- Prioritized remediation recommendations by severity
- OWASP/CWE compliance mapping
- Comprehensive audit saved to `.artifacts/security/audit-{timestamp}.md`
