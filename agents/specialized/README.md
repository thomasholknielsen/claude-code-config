# Specialized Agents

**Purpose**: Domain-specific and workflow management agents used across all stages

**When to activate**: As needed throughout development lifecycle

## Domain-Specific Agents

### Recipe Domain Expert
- **recipe-specialist** - Everything recipe-related: import, export, scaling, nutrition

## Workflow Management (Project Management)

### Context & Memory Management
- **memorybank-guardian** - Maintain .memorybank/ structure and context
- **scope-gatekeeper** - Enforce scope transitions and progression rules  
- **missing-memory-sentinel** - Handle missing context gracefully

### Task & Feature Management
- **feature-steward** - Create and manage feature lifecycle
- **task-steward** - Create and manage task lifecycle
- **cli-command-router** - Parse and dispatch CLI-style commands

### Code Quality Orchestration
- **codebase-cleanup-conductor** - Orchestrate 7-stage cleanup workflow

## Usage Notes

**Domain Specialists**: Use throughout development when domain expertise is needed.

**Workflow Management**: Use when you want structured .memorybank/ discipline and CLI-style command workflows. These add overhead but provide strict scope control.

**Optional**: These agents are not required for basic development but provide enhanced structure and domain expertise when needed.