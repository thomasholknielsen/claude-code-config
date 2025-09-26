---
description: "Generates comprehensive documentation from codebase structure and code analysis"
category: "docs"
agent: "documenter"
tools: ["Read", "Write", "Glob", "Grep"]
complexity: "moderate"
---

# Command: Generate Documentation

## Purpose
Creates comprehensive documentation from codebase analysis, matching project structure and conventions.

## Usage
```
/docs:generate [type]
```

**Arguments**: Optional documentation type (api, user, developer, or all)

## Process
1. Analyze project structure to understand architecture and patterns
2. Extract information from code, configurations, and existing documentation
3. Generate contextually appropriate documentation for the project type
4. Follow established documentation standards and formats
5. Ensure consistency with existing style and conventions

## Agent Integration
- **Primary Agent**: documenter - Handles complete documentation generation workflow

## Generation Scope

### Core Documentation (GitHub-Friendly Structure)
Following the standardized documentation architecture:

**Root-Level (GitHub Special Files):**
- **README.md** - Concise project overview, quick start, links to docs/
- **LICENSE** - Legal license terms (required for open source)
- **CHANGELOG.md** - Version history and release notes
- **CONTRIBUTING.md** - Contribution guidelines (GitHub integration)
- **SECURITY.md** - Security vulnerability reporting instructions
- **CODE_OF_CONDUCT.md** - Community behavior guidelines
- **CODEOWNERS** - GitHub automatic review assignments

**docs/ Folder (Hierarchical by Audience):**
- **docs/user/** - End-user documentation (getting-started/, tutorials/, guides/)
- **docs/developer/** - Developer documentation (api-reference/, contributing/, architecture/)
- **docs/admin/** - Administrator documentation (configuration/, deployment/)
- **docs/concepts/** - Conceptual documentation (architecture, design principles)

### Code-Derived Documentation
- **API references** - From route definitions and handlers
- **Function documentation** - From code analysis and signatures
- **Class/module docs** - From code structure and relationships
- **Configuration options** - From config schemas and defaults
- **CLI documentation** - From command definitions and help text
- **Database schema** - From models and migration files

### Workflow Documentation
- **Setup instructions** - From package.json, requirements.txt, etc.
- **Development workflow** - From scripts and common patterns
- **Testing guides** - From test files and configurations
- **Deployment docs** - From CI/CD configs and deployment scripts
- **Troubleshooting guides** - From common patterns and error handling

## Technology-Specific Generation

### JavaScript/TypeScript Projects
- **JSDoc generation** - Extract and format JSDoc comments
- **API docs from Express** - Route documentation from definitions
- **React component docs** - Props and usage from components
- **Package.json scripts** - Document available npm commands
- **TypeScript interfaces** - Generate type documentation

### Python Projects
- **Sphinx documentation** - Generate reStructuredText docs
- **Docstring compilation** - Extract Python docstrings
- **Django model docs** - Database schema from models
- **Flask route docs** - API documentation from decorators
- **Poetry/pip docs** - Dependency and installation guides

### Other Languages
- **Java** - JavaDoc extraction and formatting
- **Go** - Go doc comment compilation
- **Rust** - Rustdoc integration and crate docs
- **C#** - XML documentation processing
- **PHP** - PHPDoc extraction and API docs

## Generation Modes

### Quick Start Package (Default)
Generate industry-standard essential documentation:
```
├── README.md - Concise overview, quick start, links to docs/
├── LICENSE - Legal license terms
├── CONTRIBUTING.md - Basic contribution guidelines
└── docs/
    ├── user/
    │   └── getting-started/
    │       ├── _index.md
    │       └── installation.md
    └── developer/
        └── api-reference/
            └── _index.md
```

### Complete Documentation Suite
Generate comprehensive industry-standard structure:
```
├── README.md - Entry point with project overview and quick start
├── LICENSE - Legal license terms (required for open source)
├── CHANGELOG.md - Version history and release notes
├── CONTRIBUTING.md - Contribution guidelines (GitHub integration)
├── SECURITY.md - Security vulnerability reporting
├── CODE_OF_CONDUCT.md - Community behavior guidelines
├── CODEOWNERS - GitHub review assignments
└── docs/
    ├── user/
    │   ├── _index.md
    │   ├── getting-started/
    │   │   ├── _index.md
    │   │   ├── installation.md
    │   │   └── quick-start.md
    │   ├── tutorials/
    │   │   └── _index.md
    │   └── guides/
    │       ├── _index.md
    │       └── troubleshooting.md
    ├── developer/
    │   ├── _index.md
    │   ├── api-reference/
    │   │   ├── _index.md
    │   │   ├── authentication.md
    │   │   └── endpoints/
    │   ├── contributing/
    │   │   ├── _index.md
    │   │   ├── development-setup.md
    │   │   └── coding-standards.md
    │   └── architecture/
    │       ├── _index.md
    │       └── system-overview.md
    ├── admin/
    │   ├── _index.md
    │   ├── configuration/
    │   │   ├── _index.md
    │   │   └── environment-variables.md
    │   └── deployment/
    │       ├── _index.md
    │       └── production-deployment.md
    └── concepts/
        ├── _index.md
        ├── architecture.md
        └── design-principles.md
```

### Specialized Generation
Focus on specific areas:
- `/docs generate root` - GitHub special files only (LICENSE, SECURITY.md, etc.)
- `/docs generate user` - End-user documentation (tutorials, guides)
- `/docs generate developer` - Developer documentation (API, architecture)
- `/docs generate admin` - Administrator documentation (deployment, config)

## Smart Generation Features

### Intelligent Content Creation
- **Example generation** - Create usage examples from tests
- **Configuration discovery** - Document all environment variables
- **Dependency analysis** - List and explain all dependencies
- **Script documentation** - Explain package.json/Makefile scripts
- **Error handling docs** - Document common error scenarios

### Format Adaptation
I automatically choose appropriate formats:
- **Markdown** - For general documentation
- **OpenAPI/Swagger** - For REST APIs
- **JSDoc** - For JavaScript documentation
- **reStructuredText** - For Python Sphinx docs
- **AsciiDoc** - For technical documentation
- **MDX** - For documentation with interactive components

### Template System
Use industry-standard templates:
- **GitHub README templates** - Open source project standards
- **API documentation** - Industry-standard API reference format
- **Contributing guidelines** - Best practices for collaboration
- **Security policies** - Standard security documentation
- **Code of conduct** - Community guidelines

## Integration with Development

### Generation Triggers
Automatically generate docs:
- **After project scaffold** - Initial documentation setup
- **After major features** - New API or component documentation
- **Before releases** - Complete documentation review
- **After architecture changes** - Updated system documentation

### Command Combinations
```bash
/explain architecture && /docs generate
# Analyze structure, then generate architectural documentation

/docs analyze && /docs generate
# Find gaps, then generate missing documentation

/scaffold component && /docs generate api
# Create new component, then document its API
```

## Generation Rules

### Content Quality Standards
- **Accurate information** - Always reflect actual code implementation
- **Clear explanations** - Use simple, accessible language
- **Working examples** - All code samples must be functional
- **Complete coverage** - Document all public APIs and features
- **Consistent style** - Follow project's existing documentation patterns

### File Management
- **Never overwrite** - Always ask before replacing existing files
- **Backup originals** - Preserve existing content when updating
- **Merge intelligently** - Combine generated content with manual additions
- **Respect structure** - Follow existing documentation organization

## Output Customization

### Style Matching
I automatically detect and match:
- **Existing documentation style** - Tone, formatting, structure
- **Project conventions** - Naming, organization, standards
- **Brand guidelines** - If present in existing docs
- **Community standards** - Language/framework-specific conventions

### Content Levels
Choose appropriate detail level:
- **Beginner-friendly** - Detailed explanations and examples
- **Developer-focused** - Technical reference material
- **API reference** - Comprehensive parameter and response docs
- **Quick reference** - Concise usage guides

This generator creates professional, comprehensive documentation that makes your project accessible and maintainable for both current and future developers.