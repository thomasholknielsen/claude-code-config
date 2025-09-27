# Typical Workflows Documentation

## Overview

This document illustrates common development workflows using the Claude Code Command System, showing how users interact with
commands, agents coordinate tasks, and the system delivers results. Each workflow demonstrates the integration between user requests,
Agent Orchestra coordination, and command execution.

## Core Workflow Pattern

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant TO as task-orchestrator
    participant Worker as Worker Agent
    participant Command as Slash Command
    participant System as File System

    User->>Claude: Submit Request
    Claude->>TO: Delegate to Orchestrator
    TO->>TO: Analyze Task Complexity
    alt Simple Task
        TO->>Worker: Direct Assignment
        Worker->>Command: Execute Slash Command
        Command->>System: Perform Operations
        System-->>Command: Results
        Command-->>Worker: Command Complete
        Worker-->>TO: Task Complete
    else Complex Task
        TO->>TO: Break Down Task
        TO->>Worker: Sequential Assignment
        loop For Each Subtask
            Worker->>Command: Execute Command
            Command->>System: Operations
            System-->>Worker: Results
        end
        Worker-->>TO: All Subtasks Complete
    end
    TO-->>Claude: Task Complete
    Claude-->>User: Present Results
```text

## Workflow Categories

### 1. Feature Development Workflows

#### Quick Feature Implementation

```mermaid
flowchart TD
    Start([User: "Add login button"]) --> Analyze{Complexity Assessment}

    Analyze -->|Simple| Direct[task-orchestrator → code-writer]
    Direct --> Implement[/implement small]
    Implement --> CodeGen[Generate Code]
    CodeGen --> Review[Auto Review]
    Review --> Done1([Login Button Added])

    Analyze -->|Complex| Research[task-orchestrator → research-orchestrator]
    Research --> Parallel{Parallel Research}
    Parallel --> R1[UI Patterns Research]
    Parallel --> R2[Authentication Flow Analysis]
    Parallel --> R3[Security Requirements]

    R1 --> Synthesize[Synthesize Requirements]
    R2 --> Synthesize
    R3 --> Synthesize

    Synthesize --> Plan[implementation-orchestrator]
    Plan --> Sequence{Sequential Implementation}

    Sequence --> S1[code-writer: UI Component]
    S1 --> S2[code-writer: Event Handlers]
    S2 --> S3[test-writer: Component Tests]
    S3 --> S4[reviewer: Security Review]
    S4 --> S5[documenter: Update Docs]
    S5 --> Done2([Complex Feature Complete])
```text

#### Full Spec-Kit Workflow

```mermaid
graph TB
    UserStory["User Story: E-commerce Checkout"] --> Constitution[/spec-kit:constitution]

    Constitution --> Principles{Project Principles}
    Principles --> P1[Security First]
    Principles --> P2[Performance Standards]
    Principles --> P3[Accessibility Requirements]

    P1 --> Specify[/spec-kit:specify]
    P2 --> Specify
    P3 --> Specify

    Specify --> Requirements{Requirements Analysis}
    Requirements --> Functional[Functional Requirements]
    Requirements --> NonFunc[Non-Functional Requirements]
    Requirements --> UserStories[User Stories]

    Functional --> Clarify1[/spec-kit:clarify Round 1]
    NonFunc --> Clarify1
    UserStories --> Clarify1

    Clarify1 --> Questions1[Questions about Edge Cases]
    Questions1 --> Answers1[User Provides Answers]
    Answers1 --> Clarify2[/spec-kit:clarify Round 2]

    Clarify2 --> Questions2[Questions about Integration]
    Questions2 --> Answers2[User Provides Answers]
    Answers2 --> Plan[/spec-kit:plan]

    Plan --> Architecture{Architecture Design}
    Architecture --> Frontend[Frontend Strategy]
    Architecture --> Backend[Backend Strategy]
    Architecture --> Database[Database Design]

    Frontend --> Tasks[/spec-kit:tasks]
    Backend --> Tasks
    Database --> Tasks

    Tasks --> TaskList{Task Breakdown}
    TaskList --> Setup[Setup Tasks]
    TaskList --> Core[Core Implementation]
    TaskList --> Integration[Integration Tasks]
    TaskList --> Testing[Testing Tasks]

    Setup --> Analyze[/spec-kit:analyze]
    Core --> Analyze
    Integration --> Analyze
    Testing --> Analyze

    Analyze --> Quality{Quality Assessment}
    Quality -->|Pass| Implement[/spec-kit:implement]
    Quality -->|Fail| FixIssues[Address Issues]
    FixIssues --> Analyze

    Implement --> Done([Checkout Feature Complete])
```text

### 2. Code Quality Workflows

#### Comprehensive Code Review

```mermaid
sequenceDiagram
    participant User
    participant TO as task-orchestrator
    participant RO as research-orchestrator
    participant Rev as reviewer
    participant CW as code-writer

    User->>TO: /workflows:run-comprehensive-review
    TO->>RO: Coordinate parallel reviews

    par Security Review
        RO->>Rev: /review:security
        Rev->>Rev: OWASP Analysis
        Rev->>Rev: Vulnerability Scan
        Rev->>Rev: Generate Security Report
    and Code Quality Review
        RO->>Rev: /review:code
        Rev->>Rev: Style Compliance
        Rev->>Rev: Complexity Analysis
        Rev->>Rev: Generate Quality Report
    and Design Review
        RO->>Rev: /review:design
        Rev->>Rev: Architecture Assessment
        Rev->>Rev: Pattern Validation
        Rev->>Rev: Generate Design Report
    end

    Rev-->>RO: All Reviews Complete
    RO->>RO: Consolidate Findings
    RO->>CW: Generate Fix Recommendations
    CW->>CW: Prioritize Issues
    CW-->>TO: Comprehensive Review Complete
    TO-->>User: Present Consolidated Results
```text

#### Automated Cleanup Workflow

```mermaid
flowchart LR
    subgraph "Cleanup Initiation"
        Start([/workflows:run-cleanup-workflow]) --> Assess[task-orchestrator]
    end

    subgraph "Parallel Cleanup Operations"
        Assess --> P1[/clean:apply-style-rules]
        Assess --> P2[/clean:improve-readability]
        Assess --> P3[/clean:development-artifacts]
    end

    subgraph "Style Rules"
        P1 --> S1[Prettier Formatting]
        S1 --> S2[ESLint Fixes]
        S2 --> S3[Style Compliance]
    end

    subgraph "Readability Improvements"
        P2 --> R1[Variable Naming]
        R1 --> R2[Function Structure]
        R2 --> R3[Comment Cleanup]
    end

    subgraph "Artifact Cleanup"
        P3 --> A1[Remove Debug Code]
        A1 --> A2[Clean Temp Files]
        A2 --> A3[Update .gitignore]
    end

    subgraph "Validation"
        S3 --> Validate[reviewer]
        R3 --> Validate
        A3 --> Validate
        Validate --> Report[Generate Cleanup Report]
    end

    Report --> Done([Cleanup Complete])
```text

### 3. Bug Fix Workflows

#### Quick Bug Fix

```mermaid
stateDiagram-v2
    [*] --> Reported
    Reported --> QuickFix : /fix:bug-quickly "Login broken"

    state QuickFix {
        [*] --> Analyze
        Analyze --> Reproduce : bug-fixer reproduces issue
        Reproduce --> Isolate : Identify root cause
        Isolate --> Fix : Apply fix
        Fix --> Verify : Test fix works
        Verify --> [*]
    }

    QuickFix --> TestFix : Automated tests run
    TestFix --> CodeReview : reviewer validates
    CodeReview --> Documentation : documenter updates
    Documentation --> [*]

    note right of QuickFix : Single agent handles\nentire fix process
```text

#### Complex Bug Investigation

```mermaid
flowchart TD
    BugReport[Complex Performance Issue] --> TO[task-orchestrator]
    TO --> RO[research-orchestrator]

    subgraph "Parallel Investigation"
        RO --> I1[Agent 1: Profile Performance]
        RO --> I2[Agent 2: Analyze Database Queries]
        RO --> I3[Agent 3: Check Network Calls]
        RO --> I4[Agent 4: Review Error Logs]
        RO --> I5[Agent 5: Test User Scenarios]
    end

    I1 --> Findings[Consolidate Findings]
    I2 --> Findings
    I3 --> Findings
    I4 --> Findings
    I5 --> Findings

    Findings --> RootCause{Root Cause Identified?}
    RootCause -->|Yes| Plan[implementation-orchestrator]
    RootCause -->|No| DeepDive[/analyze:potential-issues]

    DeepDive --> MoreInvestigation[Extended Research]
    MoreInvestigation --> RootCause

    Plan --> FixStrategy[Design Fix Strategy]
    FixStrategy --> Implementation[Sequential Fix Implementation]

    subgraph "Fix Implementation"
        Implementation --> F1[code-writer: Core Fix]
        F1 --> F2[test-writer: Performance Tests]
        F2 --> F3[reviewer: Impact Analysis]
        F3 --> F4[documenter: Post-Mortem]
    end

    F4 --> Verified[Bug Fixed & Documented]
```text

### 4. Documentation Workflows

#### API Documentation Generation

```mermaid
sequenceDiagram
    participant User
    participant TO as task-orchestrator
    participant RO as research-orchestrator
    participant Doc as documenter
    participant CW as code-writer

    User->>TO: /docs:api
    TO->>RO: Research existing API structure

    par Code Analysis
        RO->>RO: Scan API endpoints
        RO->>RO: Extract schemas
        RO->>RO: Identify patterns
    and Example Generation
        RO->>CW: Generate code examples
        CW->>CW: Create request/response samples
        CW->>CW: Write integration examples
    end

    RO-->>TO: API Analysis Complete
    CW-->>TO: Examples Ready

    TO->>Doc: Generate documentation
    Doc->>Doc: Create OpenAPI spec
    Doc->>Doc: Generate markdown docs
    Doc->>Doc: Create interactive examples
    Doc-->>TO: Documentation Complete
    TO-->>User: API docs generated
```text

#### Comprehensive Documentation Update

```mermaid
graph LR
    subgraph "Documentation Audit"
        Start([/workflows:run-docs-workflow]) --> Audit[/docs:analyze]
        Audit --> Gaps[Identify Documentation Gaps]
    end

    subgraph "Content Generation"
        Gaps --> Generate[/docs:generate]
        Generate --> G1[API Documentation]
        Generate --> G2[User Guides]
        Generate --> G3[Developer Guides]
    end

    subgraph "Content Updates"
        G1 --> Update[/docs:update]
        G2 --> Update
        G3 --> Update
        Update --> U1[Version Updates]
        Update --> U2[Link Validation]
        Update --> U3[Example Updates]
    end

    subgraph "Quality Validation"
        U1 --> Validate[documenter review]
        U2 --> Validate
        U3 --> Validate
        Validate --> V1[Completeness Check]
        Validate --> V2[Accuracy Verification]
        Validate --> V3[Consistency Review]
    end

    V1 --> Complete([Documentation Updated])
    V2 --> Complete
    V3 --> Complete
```text

### 5. Deployment & Operations Workflows

#### Deployment Pipeline

```mermaid
flowchart TD
    Deploy[/deploy production] --> PreCheck[Pre-deployment Checks]

    subgraph "Validation Phase"
        PreCheck --> Tests[/test all]
        Tests --> Security[/review:security]
        Security --> Build[/build production]
    end

    subgraph "Deployment Phase"
        Build --> BackupDB[Backup Database]
        BackupDB --> DeployCode[Deploy Code]
        DeployCode --> RunMigrations[Run Migrations]
        RunMigrations --> UpdateConfigs[Update Configurations]
    end

    subgraph "Verification Phase"
        UpdateConfigs --> HealthCheck[Health Checks]
        HealthCheck --> SmokeTests[Smoke Tests]
        SmokeTests --> MonitoringCheck[Monitoring Validation]
    end

    subgraph "Rollback Decision"
        MonitoringCheck --> Success{Deployment Successful?}
        Success -->|Yes| Complete[Deployment Complete]
        Success -->|No| Rollback[Automated Rollback]
        Rollback --> Investigate[/analyze:potential-issues]
    end

    Complete --> Notify[Send Success Notifications]
    Investigate --> Report[Generate Failure Report]
```text

### 6. Research & Analysis Workflows

#### Technical Research

```mermaid
mindmap
  root((Technical Research Request))
    Parallel Research Streams
      Agent 1: Framework Analysis
        Latest versions
        Performance benchmarks
        Community adoption
        Security track record
      Agent 2: Alternative Solutions
        Competitor analysis
        Open source options
        Cost comparisons
        Feature matrices
      Agent 3: Integration Requirements
        API compatibility
        Data migration needs
        Deployment complexity
        Team training needs
      Agent 4: Risk Assessment
        Technical risks
        Business risks
        Timeline impacts
        Resource requirements
    Synthesis Phase
      Consolidate findings
      Generate recommendations
      Create decision matrix
      Present options
```text

#### Performance Analysis

```mermaid
sequenceDiagram
    participant User
    participant TO as task-orchestrator
    participant RO as research-orchestrator
    participant Agents as Analysis Agents

    User->>TO: /analyze:performance
    TO->>RO: Coordinate performance analysis

    par Frontend Analysis
        RO->>Agents: Analyze bundle sizes
        RO->>Agents: Check render performance
        RO->>Agents: Audit Core Web Vitals
    and Backend Analysis
        RO->>Agents: Database query analysis
        RO->>Agents: API response times
        RO->>Agents: Memory usage patterns
    and Infrastructure Analysis
        RO->>Agents: Server resource usage
        RO->>Agents: Network latency checks
        RO->>Agents: CDN effectiveness
    end

    Agents-->>RO: Analysis Results
    RO->>RO: Generate Performance Report
    RO->>RO: Identify Bottlenecks
    RO->>RO: Recommend Optimizations
    RO-->>TO: Comprehensive Analysis
    TO-->>User: Performance Insights & Recommendations
```text

## Workflow Selection Guide

### Task Complexity Assessment

```mermaid
flowchart TD
    Request[User Request] --> Assess{Assess Complexity}

    Assess -->|Simple| Simple[Single Command]
    Simple --> S1["/fix:bug-quickly"]
    Simple --> S2["/clean:apply-style-rules"]
    Simple --> S3["/docs:generate"]

    Assess -->|Moderate| Moderate[Sequential Commands]
    Moderate --> M1["/review:code → /clean:improve-readability"]
    Moderate --> M2["/analyze:performance → /refactor:optimize"]
    Moderate --> M3["/test → /docs:update"]

    Assess -->|Complex| Complex[Workflow Commands]
    Complex --> C1["/workflows:run-comprehensive-review"]
    Complex --> C2["/spec-kit:* (full workflow)"]
    Complex --> C3["/workflows:run-cleanup-workflow"]

    Assess -->|Architectural| Architectural[Planning Required]
    Architectural --> A1["Think/Think Hard Mode"]
    Architectural --> A2["Multi-phase Implementation"]
    Architectural --> A3["Cross-team Coordination"]
```

### Agent Selection Matrix

| Task Type | Primary Agent | Secondary Agents | Commands Used |
|-----------|---------------|------------------|---------------|
| **Quick Fixes** | task-orchestrator | bug-fixer | /fix:bug-quickly |
| **Research Tasks** | research-orchestrator | Multiple parallel | /analyze:*, /explain:* |
| **Implementation** | implementation-orchestrator | code-writer, test-writer | /implement, /spec-kit:implement |
| **Code Review** | task-orchestrator | reviewer | /review:*, /workflows:run-comprehensive-review |
| **Documentation** | task-orchestrator | documenter | /docs:*, /workflows:run-docs-workflow |
| **Cleanup Operations** | task-orchestrator | Multiple workers | /clean:*, /workflows:run-cleanup-workflow |
| **Complex Features** | task-orchestrator | All orchestrators | /spec-kit:* (full workflow) |

## Best Practices

### Workflow Optimization

1. **Start Simple**: Use single commands for straightforward tasks
2. **Scale Up**: Move to workflows for complex operations
3. **Parallel When Possible**: Use research-orchestrator for independent tasks
4. **Sequential When Dependent**: Use implementation-orchestrator for ordered operations
5. **Quality Gates**: Include review and analysis steps in complex workflows

### Common Anti-Patterns

❌ **Micro-management**: Breaking simple tasks into unnecessary steps
❌ **Workflow Overuse**: Using complex workflows for simple operations
❌ **Skipping Analysis**: Implementing without understanding requirements
❌ **Ignoring Dependencies**: Running dependent tasks in parallel
❌ **No Quality Gates**: Deploying without review and testing

### Success Metrics

- **Completion Rate**: Percentage of workflows completing successfully
- **Time to Completion**: Average workflow execution time
- **Quality Scores**: Code quality improvements after workflows
- **User Satisfaction**: Feedback on workflow effectiveness
- **Error Reduction**: Decrease in post-workflow issues

These typical workflows demonstrate how the Claude Code Command System orchestrates complex development tasks through
intelligent agent coordination, providing users with powerful automation while maintaining quality and consistency.
