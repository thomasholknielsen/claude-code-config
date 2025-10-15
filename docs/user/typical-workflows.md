# Typical Workflows Documentation

## Overview

This document illustrates common development workflows using the Claude Code Command System, showing how users interact with
commands, specialist agents provide advisory consultation, and the system delivers results. Each workflow demonstrates the integration between user requests,
Agent Specialist Framework consultation, and command execution.

## Core Workflow Pattern

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant TAS as task-analysis-specialist
    participant Spec as Specialist (Advisory)
    participant Command as Slash Command
    participant System as File System

    User->>Claude: Submit Request
    Claude->>TAS: Consult Analysis Specialist
    TAS-->>Claude: Provide Task Assessment
    alt Simple Task
        Claude->>Spec: Consult Domain Specialist
        Spec-->>Claude: Provide Advisory Guidance
        Claude->>Command: Execute Slash Command
        Command->>System: Perform Operations
        System-->>Command: Results
        Command-->>Claude: Command Complete
    else Complex Task
        Claude->>TAS: Consult for Task Breakdown
        TAS-->>Claude: Provide Strategy Recommendations
        loop For Each Subtask
            Claude->>Spec: Consult Relevant Specialist
            Spec-->>Claude: Provide Domain Guidance
            Claude->>Command: Execute Command
            Command->>System: Operations
            System-->>Claude: Results
        end
    end
    Claude-->>User: Present Results
```

## Workflow Categories

### 1. Feature Development Workflows

#### Quick Feature Implementation

```mermaid
flowchart TD
    Start([User: "Add login button"]) --> Analyze{Complexity Assessment}

    Analyze -->|Simple| Direct[Main Thread consults code-writer]
    Direct --> Implement[Execute /implement:small]
    Implement --> CodeGen[Generate Code]
    CodeGen --> Review[Auto Review]
    Review --> Done1([Login Button Added])

    Analyze -->|Complex| Research[Main Thread consults research-analysis-specialist]
    Research --> Strategy[Get Research Strategy]
    Strategy --> Execute[Main Thread executes parallel tools]
    Execute --> R1[Read UI Patterns]
    Execute --> R2[Grep Auth Flows]
    Execute --> R3[WebFetch Security Docs]

    R1 --> Synthesize[Main Thread synthesizes]
    R2 --> Synthesize
    R3 --> Synthesize

    Synthesize --> Plan[Consult implementation-strategy-specialist]
    Plan --> Sequence[Execute Sequential Commands]

    Sequence --> S1[/implement UI Component]
    S1 --> S2[/implement Event Handlers]
    S2 --> S3[/test component coverage]
    S3 --> S4[/review:security]
    S4 --> S5[/docs:update]
    S5 --> Done2([Complex Feature Complete])
```

#### Full Spec-Kit Workflow

```mermaid
graph TB
    UserStory["User Story: E-commerce Checkout"] --> Constitution[/speckit:constitution]

    Constitution --> Principles{Project Principles}
    Principles --> P1[Security First]
    Principles --> P2[Performance Standards]
    Principles --> P3[Accessibility Requirements]

    P1 --> Specify[/speckit:specify]
    P2 --> Specify
    P3 --> Specify

    Specify --> Requirements{Requirements Analysis}
    Requirements --> Functional[Functional Requirements]
    Requirements --> NonFunc[Non-Functional Requirements]
    Requirements --> UserStories[User Stories]

    Functional --> Clarify1[/speckit:clarify Round 1]
    NonFunc --> Clarify1
    UserStories --> Clarify1

    Clarify1 --> Questions1[Questions about Edge Cases]
    Questions1 --> Answers1[User Provides Answers]
    Answers1 --> Clarify2[/speckit:clarify Round 2]

    Clarify2 --> Questions2[Questions about Integration]
    Questions2 --> Answers2[User Provides Answers]
    Answers2 --> Plan[/speckit:plan]

    Plan --> Architecture{Architecture Design}
    Architecture --> Frontend[Frontend Strategy]
    Architecture --> Backend[Backend Strategy]
    Architecture --> Database[Database Design]

    Frontend --> Tasks[/speckit:tasks]
    Backend --> Tasks
    Database --> Tasks

    Tasks --> TaskList{Task Breakdown}
    TaskList --> Setup[Setup Tasks]
    TaskList --> Core[Core Implementation]
    TaskList --> Integration[Integration Tasks]
    TaskList --> Testing[Testing Tasks]

    Setup --> Analyze[/speckit:analyze]
    Core --> Analyze
    Integration --> Analyze
    Testing --> Analyze

    Analyze --> Quality{Quality Assessment}
    Quality -->|Pass| Implement[/speckit:implement]
    Quality -->|Fail| FixIssues[Address Issues]
    FixIssues --> Analyze

    Implement --> Done([Checkout Feature Complete])
```

### 2. Code Quality Workflows

#### Comprehensive Code Review

```mermaid
sequenceDiagram
    participant User
    participant TAS as task-analysis-specialist
    participant RAS as research-analysis-specialist
    participant Rev as reviewer
    participant CW as code-writer

    User->>Claude: /workflows:run-comprehensive-review
    Claude->>TAS: Consult for Review Strategy
    TAS-->>Claude: Recommend Parallel Approach
    Claude->>RAS: Consult for Review Coordination
    RAS-->>Claude: Provide Review Plan

    par Security Review
        Claude->>Claude: Execute /review:security
        Note over Claude: OWASP Analysis
        Note over Claude: Vulnerability Scan
        Note over Claude: Generate Security Report
    and Code Quality Review
        Claude->>Claude: Execute /review:code
        Note over Claude: Style Compliance
        Note over Claude: Complexity Analysis
        Note over Claude: Generate Quality Report
    and Design Review
        Claude->>Claude: Execute /review:design
        Note over Claude: Architecture Assessment
        Note over Claude: Pattern Validation
        Note over Claude: Generate Design Report
    end

    Claude->>Claude: Consolidate Review Results
    Claude->>CW: Consult for Fix Recommendations
    CW-->>Claude: Provide Fix Strategy
    Claude->>Claude: Prioritize and Execute Fixes
    Claude-->>User: Present Consolidated Results
```

#### Automated Cleanup Workflow

```mermaid
flowchart LR
    subgraph "Cleanup Initiation"
        Start([/workflows:run-cleanup-workflow]) --> Assess[Consult task-analysis-specialist]
    end

    subgraph "Parallel Cleanup Operations"
        Assess --> P1[Execute /clean:apply-style-rules]
        Assess --> P2[Execute /clean:improve-readability]
        Assess --> P3[Execute /clean:development-artifacts]
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
```

### 3. Bug Fix Workflows

#### Quick Bug Fix

```mermaid
stateDiagram-v2
    [*] --> Reported
    Reported --> QuickFix : /fix:bug-quickly "Login broken"

    state QuickFix {
        [*] --> Analyze
        Analyze --> Reproduce : Main thread reproduces issue
        Reproduce --> Isolate : Identify root cause
        Isolate --> Fix : Apply fix
        Fix --> Verify : Test fix works
        Verify --> [*]
    }

    QuickFix --> TestFix : Execute automated tests
    TestFix --> CodeReview : Execute /review:code
    CodeReview --> Documentation : Execute /docs:update
    Documentation --> [*]

    note right of QuickFix : Main thread handles\nentire fix process
```

#### Complex Bug Investigation

```mermaid
flowchart TD
    BugReport[Complex Performance Issue] --> TAS[Consult task-analysis-specialist]
    TAS --> RAS[Consult research-analysis-specialist]

    subgraph "Main Thread Parallel Tools"
        RAS --> I1[Bash: Profile Performance]
        RAS --> I2[Grep: Analyze Database Queries]
        RAS --> I3[WebFetch: Check Network Patterns]
        RAS --> I4[Read: Review Error Logs]
        RAS --> I5[Bash: Test User Scenarios]
    end

    I1 --> Findings[Main Thread Consolidates]
    I2 --> Findings
    I3 --> Findings
    I4 --> Findings
    I5 --> Findings

    Findings --> RootCause{Root Cause Identified?}
    RootCause -->|Yes| Plan[Consult implementation-strategy-specialist]
    RootCause -->|No| DeepDive[Execute /analyze:potential-issues]

    DeepDive --> MoreInvestigation[Extended Research]
    MoreInvestigation --> RootCause

    Plan --> FixStrategy[Get Fix Strategy]
    FixStrategy --> Implementation[Sequential Command Execution]

    subgraph "Fix Implementation"
        Implementation --> F1[Execute /implement fix]
        F1 --> F2[Execute /test performance]
        F2 --> F3[Execute /review:security]
        F3 --> F4[Execute /docs:update]
    end

    F4 --> Verified[Bug Fixed & Documented]
```

### 4. Documentation Workflows

#### API Documentation Generation

```mermaid
sequenceDiagram
    participant User
    participant TAS as task-analysis-specialist
    participant RAS as research-analysis-specialist
    participant Doc as documenter
    participant CW as code-writer

    User->>Claude: /docs:api
    Claude->>TAS: Consult for API Documentation Strategy
    TAS-->>Claude: Recommend Analysis Approach
    Claude->>RAS: Consult for Research Strategy
    RAS-->>Claude: Provide Research Plan

    par Code Analysis Tools
        Claude->>Claude: Grep API endpoints
        Claude->>Claude: Read schema files
        Claude->>Claude: Glob pattern matching
    and Example Generation
        Claude->>CW: Consult for Example Patterns
        CW-->>Claude: Recommend Example Structure
        Claude->>Claude: Generate samples
    end

    Claude->>Claude: Analyze Results
    Claude->>Doc: Consult for Documentation Format
    Doc-->>Claude: Recommend Structure

    Claude->>Claude: Create OpenAPI spec
    Claude->>Claude: Generate markdown docs
    Claude->>Claude: Create interactive examples
    Claude-->>User: API docs generated
```

#### Comprehensive Documentation Update

```mermaid
graph LR
    subgraph "Documentation Audit"
        Start([/workflows:docs]) --> Audit[Execute /docs:analyze]
        Audit --> Gaps[Identify Documentation Gaps]
    end

    subgraph "Content Generation"
        Gaps --> Generate[Execute /docs:generate]
        Generate --> G1[API Documentation]
        Generate --> G2[User Guides]
        Generate --> G3[Developer Guides]
    end

    subgraph "Content Updates"
        G1 --> Update[Execute /docs:update]
        G2 --> Update
        G3 --> Update
        Update --> U1[Version Updates]
        Update --> U2[Link Validation]
        Update --> U3[Example Updates]
    end

    subgraph "Quality Validation"
        U1 --> Validate[Consult documenter for review]
        U2 --> Validate
        U3 --> Validate
        Validate --> V1[Completeness Check]
        Validate --> V2[Accuracy Verification]
        Validate --> V3[Consistency Review]
    end

    V1 --> Complete([Documentation Updated])
    V2 --> Complete
    V3 --> Complete
```

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
```

### 6. Research & Analysis Workflows

#### Technical Research

```mermaid
mindmap
  root((Technical Research Request))
    Parallel Research Streams
      Specialist 1: Framework Analysis
        Latest versions
        Performance benchmarks
        Community adoption
        Security track record
      Specialist 2: Alternative Solutions
        Competitor analysis
        Open source options
        Cost comparisons
        Feature matrices
      Specialist 3: Integration Requirements
        API compatibility
        Data migration needs
        Deployment complexity
        Team training needs
      Specialist 4: Risk Assessment
        Technical risks
        Business risks
        Timeline impacts
        Resource requirements
    Synthesis Phase
      Consolidate findings
      Generate recommendations
      Create decision matrix
      Present options
```

#### Performance Analysis

```mermaid
sequenceDiagram
    participant User
    participant TAS as task-analysis-specialist
    participant RAS as research-analysis-specialist
    participant Specialists as Analysis Specialists

    User->>Claude: /analyze:performance
    Claude->>TAS: Consult for Performance Strategy
    TAS-->>Claude: Recommend Analysis Approach
    Claude->>RAS: Consult for Analysis Coordination
    RAS-->>Claude: Provide Performance Analysis Plan

    par Frontend Analysis Tools
        Claude->>Claude: Grep bundle configs
        Claude->>Claude: Read performance metrics
        Claude->>Claude: Bash Core Web Vitals audit
    and Backend Analysis Tools
        Claude->>Claude: Grep database queries
        Claude->>Claude: Bash API performance tests
        Claude->>Claude: Read memory usage logs
    and Infrastructure Analysis Tools
        Claude->>Claude: Bash server resource check
        Claude->>Claude: WebFetch network latency
        Claude->>Claude: Read CDN configuration
    end

    Claude->>Claude: Consolidate Analysis Results
    Claude->>Claude: Generate Performance Report
    Claude->>Claude: Identify Bottlenecks
    Claude->>Claude: Generate Optimization Recommendations
    Claude-->>User: Performance Insights & Recommendations
```

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
    Complex --> C2["/speckit:* (full workflow)"]
    Complex --> C3["/workflows:run-cleanup-workflow"]

    Assess -->|Architectural| Architectural[Planning Required]
    Architectural --> A1["Think/Think Hard Mode"]
    Architectural --> A2["Multi-phase Implementation"]
    Architectural --> A3["Cross-team Coordination"]
```

### Agent Selection Matrix

| Task Type | Domain Analysts Used | Commands Used |
|-----------|----------------------|---------------|
| **Quick Fixes** | debugger-analyst, code-quality-analyst | Manual fixes → /git:commit |
| **Research Tasks** | research-codebase-analyst, research-web-analyst | /explain:*, domain analysts |
| **Implementation** | architecture-analyst, relevant domain analysts | /speckit:implement, manual implementation |
| **Code Review** | Multiple domain analysts in parallel | /workflows:run-comprehensive-review |
| **Documentation** | docs-analyst (multi-perspective), architecture-analyst | /workflows:docs, /docs:changelog |
| **Cleanup Operations** | code-quality-analyst, refactoring-analyst | /workflows:run-cleanup-workflow, /lint:correct-all |
| **Complex Features** | All relevant domain analysts | /speckit:* (full workflow) |

## Best Practices

### Workflow Optimization

1. **Start Simple**: Use single commands for straightforward tasks
2. **Scale Up**: Move to workflows for complex operations
3. **Parallel When Possible**: Use main thread parallel tools for independent tasks
4. **Sequential When Dependent**: Use specialist advisory guidance for ordered operations
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

These typical workflows demonstrate how the Claude Code Command System coordinates complex development tasks through the Agent Specialist
Framework, where Claude Code orchestrates parallelization and tool execution while specialist agents provide advisory consultation and
recommendations, ensuring powerful automation with quality and consistency.

**Note**: Only the main Claude Code thread can coordinate parallelization and execute tools. All specialist agents function as advisory
consultants that provide specialized analysis and strategic recommendations to the main Claude Code coordinator.
