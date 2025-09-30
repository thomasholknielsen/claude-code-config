# Agent Specialist Framework Documentation

## Overview

The Agent Specialist Framework is a multi-agent system implementation for Claude Code that provides specialized expertise through advisory
specialist agents. Each agent serves as an advisory consultant that the main thread can consult for domain-specific knowledge and strategic
guidance, enabling parallel tool execution while maintaining centralized coordination.

**📚 For detailed parallel execution patterns and examples**, see [Parallel Execution Patterns](parallel-execution-patterns.md).

## Architecture

```mermaid
graph TD
    User[User Request] --> MT[Main Thread]

    MT --> |Advisory Consult| TO[task-analysis-specialist]
    MT --> |Advisory Consult| RO[research-analysis-specialist]
    MT --> |Advisory Consult| IO[implementation-strategy-specialist]
    MT --> |Advisory Consult| CW[code-writer]
    MT --> |Advisory Consult| TW[test-writer]
    MT --> |Advisory Consult| BF[bug-fixer]
    MT --> |Advisory Consult| REV[reviewer]
    MT --> |Advisory Consult| DOC[documenter]

    MT --> |Executes| SC[Slash Commands]
    SC --> |/refactor| Refactor
    SC --> |/fix| Fix
    SC --> |/review| Review
    SC --> |/docs| Docs
    SC --> |/test| Test

    MT --> |Parallel Tools| Tools[Tool Execution]
    Tools --> |Read| FileOps
    Tools --> |Write| FileOps
    Tools --> |Bash| ShellOps
    Tools --> |Grep| SearchOps
```yaml

## Core Components

### 1. Strategic Specialists (3 advisory agents)

#### task-analysis-specialist

- **Role**: Task analysis and planning specialist
- **Expertise**: Task complexity assessment (simple/moderate/complex)
- **Advises**: Optimal workflow patterns and coordination strategies
- **Recommends**: Parallel vs sequential execution approaches
- **Provides**: TodoWrite planning and SlashCommand delegation strategies

#### research-analysis-specialist

- **Role**: Information gathering and research specialist
- **Expertise**: Multi-source research coordination and synthesis
- **Advises**: Research strategies and information prioritization
- **Recommends**: Breadth-first investigation patterns for comprehensive coverage

#### implementation-strategy-specialist

- **Role**: Code architecture and dependency specialist
- **Expertise**: Sequential code changes with validation strategies
- **Advises**: File dependency management and change ordering
- **Recommends**: Hybrid approaches balancing dependencies with parallel validation
- **Provides**: Quality assurance patterns for code, security, design, and performance

### 2. Technical Specialists (5 advisory agents)

#### code-writer

- **Role**: Code generation and architecture specialist
- **Expertise**: Implementation patterns, refactoring strategies, code structure
- **Advises**: `/refactor:large-scale`, `/implement` command usage
- **Specializes**: Clean code practices, architectural patterns, performance optimization

#### test-writer

- **Role**: Testing strategy and implementation specialist
- **Expertise**: Test framework selection, coverage strategies, test architecture
- **Advises**: `/test`, `/spec-kit:tasks` command usage
- **Specializes**: Automated framework detection, test pattern recommendations

#### bug-fixer

- **Role**: Debugging and issue resolution specialist
- **Expertise**: Root cause analysis, systematic debugging approaches
- **Advises**: `/fix:bug-quickly`, `/analyze:potential-issues` command usage
- **Specializes**: Issue reproduction, isolation techniques, verification strategies

#### reviewer

- **Role**: Code quality and security analysis specialist
- **Expertise**: Multi-dimensional review strategies, security best practices
- **Advises**: `/review:code`, `/review:security` command usage
- **Specializes**: Parallel review coordination, comprehensive quality assessment

#### documenter

- **Role**: Technical documentation and API specialist
- **Expertise**: Documentation strategies, multiple format generation
- **Advises**: `/docs:generate`, `/docs:api` command usage
- **Specializes**: README optimization, API documentation, inline comment strategies

## Execution Patterns

### Main Thread Parallel Tool Execution

```yaml
Main Thread executes tools in parallel:
  Bash: Search codebase patterns
  Grep: Analyze documentation
  Read: Review configuration files
  Glob: Find dependency patterns
  WebFetch: Check external resources
```

### Sequential Advisory Pattern

```yaml
Main Thread consults specialists sequentially:
  1. task-analysis-specialist → Assess complexity and strategy
  2. research-analysis-specialist → Recommend information gathering approach
  3. implementation-strategy-specialist → Plan dependency management
  4. code-writer → Provide implementation guidance
  5. reviewer → Validate approach
```

### Hybrid Advisory Pattern

```text
Phase 1 (Parallel consultation):
  Consult research-analysis-specialist for investigation strategy
  Consult implementation-strategy-specialist for architecture guidance
  Consult code-writer for pattern recommendations
Phase 2 (Main thread execution):
  Execute tools based on specialist recommendations
  Apply suggested patterns and approaches
  Validate results with reviewer specialist
```

## Specialist Consultation

Main thread coordinates with specialists through:

- **Advisory Consultation**: Seeking domain-specific expertise and strategic recommendations
- **Strategy Planning**: Consulting on optimal approaches and execution patterns
- **Knowledge Synthesis**: Integrating specialist insights into unified execution plans
- **Quality Guidance**: Leveraging specialist expertise for validation and improvement recommendations

### Consultation Tracking Example

```json
{
  "task_id": "auth-feature-2025",
  "main_thread_status": "executing",
  "specialists_consulted": [
    "task-analysis-specialist",
    "implementation-strategy-specialist",
    "code-writer"
  ],
  "complexity_assessment": "moderate",
  "current_phase": "implementation",
  "tools_executing": ["Read", "Edit", "Bash"],
  "slash_commands_planned": ["/implement", "/refactor:large-scale"]
}
```

## Slash Command Integration

Main thread executes slash commands informed by specialist advisory recommendations:

| Specialist | Recommends Commands | Expertise Domain |
|------------|-------------------|------------------|
| code-writer | `/refactor`, `/implement` | Code generation patterns |
| test-writer | `/test`, `/spec-kit:tasks` | Testing strategies |
| bug-fixer | `/fix:bug-quickly`, `/analyze` | Debugging approaches |
| reviewer | `/review:code`, `/review:security` | Quality assessment |
| documenter | `/docs:generate`, `/docs:api` | Documentation formats |

## Workflow Examples

### Bug Fix Workflow

```mermaid
sequenceDiagram
    participant U as User
    participant MT as Main Thread
    participant TO as task-analysis-specialist
    participant BF as bug-fixer
    participant TW as test-writer

    U->>MT: Fix login timeout bug
    MT->>TO: Advisory Consult: How to approach this?
    TO-->>MT: Advisory Recommendation: Assess → Fix → Test
    MT->>BF: Advisory Consult: Best debugging strategy?
    BF-->>MT: Advisory Recommendation: /fix:bug-quickly approach
    MT->>MT: Execute /fix:bug-quickly
    MT->>TW: Advisory Consult: How to verify fix?
    TW-->>MT: Advisory Recommendation: Integration test pattern
    MT-->>U: Bug fixed and verified
```text

### Feature Implementation

```mermaid
sequenceDiagram
    participant U as User
    participant MT as Main Thread
    participant IO as implementation-strategy-specialist
    participant CW as code-writer
    participant TW as test-writer
    participant D as documenter
    participant R as reviewer

    U->>MT: Implement user auth
    MT->>IO: Advisory Consult: Implementation strategy?
    IO-->>MT: Advisory Recommendation: Structure → Logic → Test → Document
    MT->>CW: Advisory Consult: Best structure patterns?
    CW-->>MT: Advisory Recommendation: Modular auth components
    MT->>MT: Execute implementation commands
    MT->>TW: Advisory Consult: Test coverage strategy?
    TW-->>MT: Advisory Recommendation: Unit + integration tests
    MT->>D: Advisory Consult: Documentation approach?
    D-->>MT: Advisory Recommendation: API docs + examples
    MT->>R: Advisory Consult: Review checklist?
    R-->>MT: Advisory Recommendation: Security + performance review
    MT-->>U: Feature complete
```

## Benefits

1. **Expert Consultation**: Domain-specific specialist knowledge for optimal approaches
2. **Parallel Tool Execution**: Main thread can execute multiple tools simultaneously
3. **Focused Expertise**: Each specialist provides deep knowledge in their domain
4. **Command Integration**: Specialists recommend optimal slash command usage
5. **Unified Coordination**: Main thread maintains context and execution control

## Migration from MECE Agents

| Old MECE Agent | New Specialist Approach |
|----------------|------------------------|
| backend-engineering | Advisory consult: task-analysis-specialist + code-writer specialists |
| frontend-engineering | Advisory consult: task-analysis-specialist + code-writer specialists |
| quality-engineering | Advisory consult: reviewer + test-writer specialists |
| devops-engineering | Keep as specialist (rare use) |
| product-strategy | Advisory consult: research-analysis-specialist |
| security-compliance | Advisory consult: reviewer specialist with security focus |
| developer-experience | Advisory consult: documenter specialist |
| maintenance-support | Advisory consult: bug-fixer specialist |

## Best Practices

1. **Consult Early**: Engage appropriate specialists for advisory guidance at the start of complex tasks
2. **Leverage Expertise**: Use specialist advisory knowledge to inform main thread decisions
3. **Execute Efficiently**: Apply parallel tool execution based on specialist advisory recommendations
4. **Maintain Context**: Keep execution control in main thread for consistency
5. **Balance Consultation**: Don't over-consult for simple tasks that don't require specialist advisory input

## Important Constraints

- **NO automatic git operations**: All git commands require explicit user consent
- **Advisory only**: Specialists provide advisory recommendations, main thread executes all actions
- **No spawning**: Specialists cannot create or spawn other agents or execute tools
- **Single expertise**: Each specialist focuses on their advisory domain knowledge only
- **Main thread control**: All tool execution and coordination happens in main thread

## Future Enhancements

- Add more domain advisory specialists as needed
- Expand specialist advisory knowledge bases with current best practices
- Enhance main thread efficiency with better parallel tool coordination
- Add specialist advisory consultation metrics and optimization
- Develop more sophisticated specialist advisory recommendation patterns
