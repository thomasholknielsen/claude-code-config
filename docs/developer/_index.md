# Developer Documentation

Documentation for contributors and developers working on the Claude Code Command System.

## Core Development Guides

- **[Developer Guide](developer-guide.md)** - Architecture, patterns, and contribution workflow
- **[Command Template](command-template.md)** - Standard format for creating new commands
- **[Hooks System](hooks-system.md)** - Cross-platform automation and integration
- **[Developer Workflows](developer-workflows.md)** - Advanced development patterns

## Quick Start for Contributors

### First-Time Contributors

1. Read the [Developer Guide](developer-guide.md) for architecture overview
2. Study the [Command Template](command-template.md) for standards
3. Review [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution process
4. Set up your development environment per the guides

### Experienced Contributors

- Reference [Command Template](command-template.md) for new commands
- Check [Hooks System](hooks-system.md) for automation patterns
- Use [Developer Workflows](developer-workflows.md) for advanced scenarios

## Development Areas

### Command Development

- **Template**: [Command Template](command-template.md)
- **Validation**: Use `scripts/validate_commands.py`
- **Standards**: Follow Agent Orchestra patterns

### Agent Development

- **Framework**: See [Concepts](../concepts/agent-specialist-framework.md)
- **Patterns**: Domain Analyst Framework patterns
- **Integration**: Command delegation and coordination

### Documentation

- **Standards**: Follow Diátaxis framework (tutorials, guides, reference, explanation)
- **Audience**: User, Developer, Admin, Concepts
- **Cross-Platform**: Include Windows/macOS/Linux instructions

### Testing and Quality

- **Validation**: Automated template compliance checking
- **Security**: Security constraint verification
- **Cross-Platform**: Multi-platform testing requirements

## Architecture Reference

| Component | Documentation | Purpose |
|-----------|---------------|---------|
| Commands | [Command Template](command-template.md) | Atomic operations standard |
| Agents | [Domain Analyst Framework](../concepts/agent-specialist-framework.md) | Coordination framework |
| Hooks | [Hooks System](hooks-system.md) | Automation and integration |
| Workflows | [Developer Workflows](developer-workflows.md) | Complex development patterns |

## Development Tools

### Scripts and Automation

- `scripts/validate_commands.py` - Template compliance checking
- `scripts/fix_command_templates.py` - Automated standardization
- `hooks/security_enforcement.py` - Security control verification

### Quality Gates

- Template validation before commits
- Security constraint verification
- Cross-platform compatibility testing
- Documentation completeness checks

## Best Practices

### Code Quality

- Follow existing patterns and conventions
- Use cross-platform Python patterns
- Implement proper error handling
- Include comprehensive logging

### Security

- Respect Git operation constraints
- Implement input validation
- Use secure path handling
- Follow MCP tool restrictions

### Documentation

- Include practical examples
- Cover all supported platforms
- Maintain up-to-date integration points
- Follow audience-based organization

## Getting Help

- **Technical Questions**: Check existing documentation first
- **Architecture Decisions**: Review [Concepts](../concepts/) documentation
- **Contribution Process**: See [CONTRIBUTING.md](../../CONTRIBUTING.md)
- **Security Issues**: Follow [SECURITY.md](../../SECURITY.md) procedures

Ready to contribute? Start with the [Developer Guide](developer-guide.md)! 🛠️
