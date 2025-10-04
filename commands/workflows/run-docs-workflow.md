---
description: "Comprehensive documentation workflow that analyzes, generates, updates, and validates all project documentation"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/docs:*)
---

# Command: Run Docs Workflow

## Purpose

Orchestrates a comprehensive documentation workflow by executing atomic documentation commands in logical sequence to analyze, generate, update,
and validate all project documentation.

## Usage

```bash
/workflows:run-docs-workflow
```

## Process

1. **Analyze Documentation Coverage** - Execute `/docs:analyze` to assess current documentation state and identify gaps
2. **Extract External Documentation** - Execute `/docs:extract-external` to fetch latest framework/library documentation
3. **Generate Core Documentation** - Execute `/docs:generate` to create comprehensive documentation from codebase
4. **Update API Documentation** - Execute `/docs:api` to generate current API documentation
5. **Update Existing Documentation** - Execute `/docs:update` to refresh outdated content and maintain accuracy
6. **Generate Changelog** - Execute `/docs:changelog` to maintain version history and release notes
7. **Validate Documentation Quality** - Verify all documentation meets quality standards and GitHub compatibility

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential execution of atomic documentation commands ensuring comprehensive coverage

## Implementation Steps

### Step 1: Documentation Analysis

```bash
# Analyze current documentation state
SlashCommand("/docs:analyze")
```

### Step 2: External Documentation Integration

```bash
# Fetch latest external documentation
SlashCommand("/docs:extract-external")
```

### Step 3: Core Documentation Generation

```bash
# Generate comprehensive project documentation
SlashCommand("/docs:generate")
```

### Step 4: API Documentation

```bash
# Generate current API documentation
SlashCommand("/docs:api")
```

### Step 5: Documentation Updates

```bash
# Update existing documentation for accuracy
SlashCommand("/docs:update")
```

### Step 6: Changelog Management

```bash
# Update changelog with recent changes
SlashCommand("/docs:changelog")
```

## Examples

```bash
# Execute complete documentation workflow
/workflows:run-docs-workflow

# Result: Executes all documentation commands in sequence:
# 1. /docs:analyze
# 2. /docs:extract-external
# 3. /docs:generate
# 4. /docs:api
# 5. /docs:update
# 6. /docs:changelog
```

## Integration Points

### **Development Workflow Integration**

- Run after major feature implementation
- Include in pre-commit hooks for documentation updates
- Integrate with CI/CD for automated doc validation
- Schedule regular documentation health checks

### **Quality Assurance & Architecture Compliance**

- Validate all generated/updated documentation
- Ensure GitHub-friendly structure: concise README.md + comprehensive docs/
- Check README links to docs/ sections work correctly
- Verify mobile-friendly GitHub rendering
- Ensure examples work and code samples are accurate
- Maintain consistent style and formatting across README and docs/

### **Team Collaboration**

- Generate onboarding documentation for new team members
- Create handoff documentation for project transfers
- Maintain consistent documentation standards across team
- Support multiple documentation formats and audiences

## Command Dependencies

This workflow orchestrates these atomic commands:

- `/docs:analyze` - Documentation coverage analysis
- `/docs:extract-external` - External documentation integration
- `/docs:generate` - Core documentation generation
- `/docs:api` - API documentation creation
- `/docs:update` - Documentation updates and maintenance
- `/docs:changelog` - Version history management
