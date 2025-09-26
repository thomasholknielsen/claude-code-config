---
description: Comprehensive documentation workflow that analyzes, generates, updates, and validates all project documentation
category: workflow
tools: TodoWrite, Task, Bash
argument-hint: [scope] [--skip-step1,step2] [--mode=audit|update|generate|release]
---

# Documentation Workflow

I'll execute a comprehensive documentation workflow that ensures your project has complete, accurate, and professional documentation.

Arguments: `$ARGUMENTS` - optional scope (files/directories), skip flags, and mode selection

## Documentation Orchestration

I'll run documentation commands in this strategic sequence for maximum effectiveness:

### **Phase 1: Documentation Discovery & Analysis**
1. **Project analysis** - Understand codebase structure and technology stack
2. **Documentation inventory** - Map all existing documentation files
3. **Coverage analysis** - Identify gaps and outdated content
4. **Quality assessment** - Evaluate documentation health

### **Phase 2: Foundation Documentation (GitHub-Friendly Structure)**
5. **README.md** - Concise entry point with project overview and quick start
6. **docs/ folder setup** - Organized comprehensive documentation structure
7. **docs/API.md** - Complete API references and schemas
8. **docs/ARCHITECTURE.md** - System design and component patterns
9. **docs/INSTALLATION.md** - Detailed setup and configuration
10. **docs/CONFIGURATION.md** - Environment variables and settings

### **Phase 3: Specialized Documentation (Complete docs/ Structure)**
11. **docs/DEPLOYMENT.md** - Production deployment guides and procedures
12. **docs/CONTRIBUTING.md** - Development workflow and contribution guidelines
13. **docs/TROUBLESHOOTING.md** - Common issues and solutions
14. **docs/CHANGELOG.md** - Version history and release notes (or in root)
15. **Code documentation** - Add/update inline comments and docstrings

### **Phase 4: Quality Assurance & Integration**
16. **Cross-reference validation** - Check README links to docs/ and internal references
17. **GitHub compatibility** - Ensure mobile-friendly rendering and navigation
18. **Accuracy verification** - Ensure docs match actual implementation
19. **Architecture compliance** - Verify GitHub-friendly structure is maintained
20. **Release preparation** - Update version info and changelogs

## Workflow Modes

### **Audit Mode** (Default)
```bash
/workflows run-docs-workflow --mode=audit
```
- Comprehensive analysis of documentation health
- Gap identification and prioritized improvement plan
- Quality metrics and recommendations
- No modifications, pure assessment

### **Update Mode**
```bash
/workflows run-docs-workflow --mode=update
```
- Update existing documentation to match current codebase
- Refresh outdated content and broken links
- Maintain existing structure and style
- Focus on accuracy and freshness

### **Generate Mode**
```bash
/workflows run-docs-workflow --mode=generate
```
- Generate missing documentation from code analysis
- Create comprehensive documentation suite
- Fill gaps identified in audit phase
- Professional templates and formatting

### **Release Mode**
```bash
/workflows run-docs-workflow --mode=release
```
- Prepare documentation for release
- Update CHANGELOG with recent changes
- Validate all documentation is current
- Generate release notes and migration guides

## Command Sequence by Mode

### Audit Mode Execution
```bash
1. /explain architecture          # Understand project structure
2. /docs analyze                  # Comprehensive documentation analysis
3. /docs api --validate          # Verify API documentation accuracy
4. Quality report generation      # Consolidated findings and recommendations
```

### Update Mode Execution
```bash
1. /explain architecture          # Re-analyze current structure
2. /docs analyze                  # Find what needs updating
3. /docs update                   # Update existing documentation
4. /docs api                      # Refresh API documentation
5. /docs changelog               # Update version history
6. Validation and cross-checks   # Ensure consistency
```

### Generate Mode Execution
```bash
1. /explain architecture          # Understand what to document
2. /docs analyze                  # Identify missing documentation
3. /docs generate                 # Create missing documentation
4. /docs api                      # Generate API documentation
5. /docs changelog               # Create/update CHANGELOG
6. Integration and formatting     # Ensure consistent style
```

### Release Mode Execution
```bash
1. /test all                      # Ensure everything works
2. /docs analyze                  # Verify documentation completeness
3. /docs changelog --release      # Prepare release notes
4. /docs update                   # Final documentation updates
5. /docs api --validate          # Confirm API docs accuracy
6. Release preparation            # Version bumps and final checks
```

## Smart Workflow Features

### **Parallel Execution Where Possible**
- Run independent documentation tasks simultaneously
- Optimize for speed while maintaining quality
- Coordinate related tasks efficiently

### **Technology Detection**
Automatically adapt workflow based on project type:
- **JavaScript/TypeScript** - JSDoc, TypeScript definitions, npm scripts
- **Python** - Docstrings, Sphinx, requirements documentation
- **Java** - JavaDoc, Maven/Gradle documentation
- **Go** - Go doc, module documentation
- **Multi-language** - Comprehensive coverage for all languages

### **Framework-Specific Enhancements**
- **Web APIs** - OpenAPI/Swagger generation and validation
- **React/Vue** - Component documentation and prop definitions
- **Django/Rails** - Model and route documentation
- **CLI tools** - Command and option documentation
- **Libraries** - Usage examples and API references

## Workflow Customization

### Scope Control
```bash
/workflows run-docs-workflow docs/           # Only docs folder
/workflows run-docs-workflow src/api/        # Only API documentation
/workflows run-docs-workflow README.md       # Only README updates
```

### Skip Specific Steps
```bash
/workflows run-docs-workflow --skip-api,changelog
# Skip API documentation and changelog updates

/workflows run-docs-workflow --skip-generate
# Skip generation phase, only update existing docs
```

### Combined Operations
```bash
/workflows run-docs-workflow --mode=update --skip-changelog
# Update mode but skip changelog updates

/workflows run-docs-workflow --mode=generate docs/ --skip-api
# Generate docs only in docs folder, skip API generation
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

## Success Metrics

After completion, the workflow provides:
- **Coverage Report** - Percentage of project documented
- **Quality Score** - Documentation health metrics
- **Action Items** - Prioritized improvements for next iteration
- **Maintenance Plan** - Schedule for keeping docs current

This workflow ensures your project maintains professional, comprehensive documentation that serves both current development and future maintenance needs.