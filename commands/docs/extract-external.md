---
description: "Fetch and integrate up-to-date documentation from external sources using Context7 MCP"
category: "docs"
agent: "documenter"
tools: ["mcp__context7__resolve-library-id", "mcp__context7__get-library-docs", "Write", "Read"]
complexity: "moderate"
---

# Extract External Documentation

I'll fetch and integrate up-to-date documentation from external sources using Context7 MCP to ensure commands and agents have current information.

**My specialized approach:**
1. **Identify documentation needs** - Analyze which libraries/frameworks need current docs
2. **Resolve library identifiers** - Map package names to Context7 IDs
3. **Extract relevant documentation** - Pull focused, topic-specific content
4. **Integrate contextually** - Provide docs in actionable format
5. **Cache intelligently** - Store frequently accessed docs locally

**I focus on actionable integration** - Use `/docs:generate` for project docs or `/docs:update` for maintaining existing documentation.

## Context7 Integration Patterns

### Library Resolution
I automatically identify and resolve:
- **Framework documentation** - React, Vue, Django, Express, Spring, etc.
- **API documentation** - REST APIs, GraphQL schemas, service docs
- **Tool documentation** - Build tools, testing frameworks, deployment platforms
- **Language documentation** - Latest language features and best practices
- **Security documentation** - Vulnerability databases, security best practices

### Smart Documentation Extraction
For each library, I extract:
- **Current API references** - Latest method signatures and examples
- **Best practices** - Recommended patterns and anti-patterns
- **Migration guides** - Version upgrade instructions
- **Security advisories** - Vulnerability information and patches
- **Examples** - Working code samples and use cases
- **Configuration** - Setup and configuration options

## Framework-Specific Extraction

### JavaScript/Node.js Ecosystem
- **React** - Hooks, components, performance patterns
- **Vue** - Composition API, reactivity, SSR
- **Express** - Routing, middleware, security
- **Next.js** - App router, server components, deployment
- **TypeScript** - Latest features, strict mode, utility types

### Python Ecosystem
- **Django** - Models, views, security, deployment
- **FastAPI** - Async patterns, dependency injection, OpenAPI
- **Flask** - Blueprints, extensions, testing
- **SQLAlchemy** - ORM patterns, migrations, performance

### Other Languages
- **Spring Boot** - Annotations, security, testing
- **Ruby on Rails** - Active Record, routing, deployment
- **Go** - Concurrency, modules, testing
- **Rust** - Ownership, async, cargo

## Integration Use Cases

### Command Enhancement
Commands that benefit from external docs:
- **`/docs:api`** - Current API documentation standards
- **`/review:security`** - Latest vulnerability databases
- **`/analyze:dependencies`** - Current security advisories
- **`/implement`** - Framework best practices
- **`/refactor:*`** - Modern refactoring patterns

### Agent Knowledge Updates
Agents that benefit from current docs:
- **documenter** - Latest documentation standards and formats
- **code-writer** - Current framework patterns and APIs
- **reviewer** - Updated security best practices and code standards
- **bug-fixer** - Known issues and resolution patterns

## Atomic Usage Patterns

### Library-Specific Extraction
```bash
/docs:extract-external react
# Get latest React documentation and patterns

/docs:extract-external django --topic security
# Focus on Django security documentation

/docs:extract-external typescript --topic utility-types
# Extract TypeScript utility type documentation
```

### Security-Focused Extraction
```bash
/docs:extract-external owasp --topic web-security
# Get current OWASP security guidelines

/docs:extract-external cve-database --topic node-js
# Extract Node.js security vulnerabilities
```

### Framework Migration Support
```bash
/docs:extract-external react --topic migration-guide
# Get React version migration information

/docs:extract-external django --topic 4.2-to-5.0
# Extract Django upgrade documentation
```

## Integration Workflows

### Documentation Enhancement Flow
```bash
# Enhance existing documentation with current info
/docs:extract-external react --topic hooks
/docs:update --integrate-external
# Extract React hooks docs, then integrate into project docs
```

### Security Review Flow
```bash
# Get current security information for review
/docs:extract-external owasp --topic api-security
/review:security --use-external-docs
# Extract OWASP API security docs, then run security review
```

### Implementation Support Flow
```bash
# Get current patterns before implementation
/docs:extract-external nextjs --topic app-router
/implement --use-patterns-from-docs
# Extract Next.js app router docs, then implement with current patterns
```

## Output Formats

### Contextual Integration
Choose appropriate integration:
- **Inline reference** - Embed docs directly in commands
- **Side-by-side** - Show external docs alongside local content
- **Cached extraction** - Store frequently used docs locally
- **Link enhancement** - Add current documentation links
- **Pattern matching** - Apply external patterns to local code

### Documentation Formats
Support multiple output formats:
- **Markdown** - For general documentation integration
- **JSON** - For structured API documentation
- **Code snippets** - For immediate implementation use
- **Configuration** - For setup and deployment docs
- **Security reports** - For vulnerability information

## Quality Assurance

### Verification & Accuracy
- **Source validation** - Verify Context7 library accuracy
- **Version matching** - Ensure docs match project dependencies
- **Content freshness** - Use most current documentation available
- **Relevance filtering** - Extract only applicable information
- **Conflict resolution** - Handle contradicting information

### Integration Safety
- **Non-destructive** - Never overwrite existing documentation
- **Selective integration** - Choose what to integrate carefully
- **Rollback capability** - Maintain ability to revert changes
- **Conflict highlighting** - Show where external docs differ
- **Update tracking** - Record what was integrated and when

## Cache Management

### Smart Caching
- **Frequency-based** - Cache frequently accessed docs
- **Project-specific** - Store relevant docs per project
- **Version-aware** - Update cache when dependencies change
- **Size-optimized** - Keep cache manageable
- **Expiration** - Refresh stale documentation

### Cache Operations
```bash
/docs:extract-external --cache-status
# Show current cache status

/docs:extract-external --clear-cache react
# Clear cached React documentation

/docs:extract-external --refresh-cache
# Update all cached documentation
```

## Command Integration

### With Other Commands
Seamlessly integrate with existing commands:
- **Before implementation** - Get current patterns
- **During code review** - Check against best practices
- **After dependency updates** - Get migration information
- **For security analysis** - Get current threat information
- **During documentation** - Include external references

### Error Handling
Handle common scenarios:
- **Library not found** - Suggest alternatives
- **Documentation unavailable** - Graceful fallbacks
- **Network issues** - Use cached content
- **Invalid topics** - Show available topics
- **Rate limiting** - Implement respectful retry logic

This command bridges the gap between your project and the ever-evolving ecosystem of external documentation, ensuring your development process stays current with the latest best practices and security information.