# Software Development AI Agents

A comprehensive collection of 57 specialized AI agents designed to accelerate software development across all stages and domains. Each agent is an expert in their field, ready to be invoked when their expertise is needed. Optimized for rapid development cycles with framework-agnostic design.

## 📥 Installation

1. **Download or clone this repository**
2. **Copy agents to your Claude Code agents directory:**
   ```bash
   cp -r agents/* ~/.claude/agents/
   ```
3. **Restart Claude Code** to load the new agents

## 🚀 Quick Start

Agents are automatically available in Claude Code. Simply describe your task and the appropriate agent will be triggered. You can also explicitly request an agent by mentioning their name.

### Example Usage
- "Create a new web app for task management" → `rapid-prototyper` or `universal-scaffolder`
- "Review this Python code for issues" → `code-reviewer` & `security-auditor`
- "Our npm/pip dependencies have security alerts" → `dependency-manager`
- "Set up CI/CD for our Java/Go/Python project" → `devops-automator`
- "Add authentication to our Django/Rails/Express app" → `backend-architect`
- "Create tests for our new feature (any language)" → `test-writer-fixer`

## 📁 Directory Structure

Agents are organized by department for efficient software development workflows:

```
agents/
├── engineering/           # Core development agents
├── testing/              # Quality assurance agents
├── design/               # UI/UX and visual design
├── operations/           # DevOps, infrastructure, security
├── product/              # Planning, analysis, coordination
├── maintenance/          # Code quality and refactoring
├── specialized/          # Cross-cutting concerns
└── domain-experts/       # Industry-specific expertise
```

## 📋 Complete Agent List

### Engineering Department (`engineering/`)
- **universal-scaffolder** - Set up projects and components across any tech stack
- **rapid-prototyper** - Build MVPs and prototypes quickly (stack-agnostic)
- **backend-architect** - Design scalable server systems and infrastructure
- **api-developer** - Build developer-friendly APIs with proper documentation and security
- **frontend-developer** - Build responsive user interfaces with performance optimization
- **javascript-developer** - Master modern JavaScript ES2024+ with advanced patterns
- **typescript-developer** - Build type-safe applications with advanced TypeScript features
- **database-migration-manager** - Handle schema changes safely (SQL/NoSQL)
- **graphql-architect** - Design GraphQL schemas and resolvers
- **error-debugger** - Troubleshoot and fix bugs systematically
- **integration-specialist** - Connect with third-party APIs and services
- **ai-engineer** - Integrate AI/ML capabilities
- **mobile-app-builder** - Create native mobile applications
- **code-reviewer** - Perform comprehensive code reviews (any language)
- **dependency-manager** - Manage packages and dependencies (npm, pip, maven, etc.)

### Testing Department (`testing/`)
- **test-writer-fixer** - Write and maintain tests (Jest, pytest, JUnit, RSpec, etc.)
- **api-tester** - Test API functionality and performance (any protocol)
- **performance-benchmarker** - Measure and optimize performance (any platform)
- **analytics-engine** - Analyze test results and metrics

### Design Department (`design/`)
- **ui-designer** - Create beautiful, functional interfaces
- **ux-researcher** - Understand user needs and behaviors

### Operations Department (`operations/`)
- **devops-automator** - Automate deployments and CI/CD
- **azure-platform-architect** - Design cloud infrastructure
- **monitoring-engineer** - Set up observability and alerting
- **infrastructure-maintainer** - Maintain and scale systems
- **edge-cdn-optimizer** - Optimize content delivery
- **security-auditor** - Perform security audits and compliance

### Product Department (`product/`)
- **mvp-planner** - Define and scope product features
- **sprint-prioritizer** - Prioritize features and manage roadmaps
- **task-planner** - Break down work into actionable tasks
- **data-analyst** - Analyze user data, product metrics, and performance reporting
- **delivery-coordinator** - Coordinate releases and launches
- **feedback-synthesizer** - Process user feedback into insights
- **trend-researcher** - Identify market opportunities

### Maintenance Department (`maintenance/`)
- **codebase-cleanup-conductor** - Orchestrate systematic code cleanup
- **code-standards-enforcer** - Enforce coding standards and quality gates
- **debloat** - Remove dead code and unused imports
- **modernizer** - Update code to modern patterns and reorganize structure
- **refactorer** - Improve code structure, readability, and reduce complexity
- **workflow-optimizer** - Improve development processes
- **tool-evaluator** - Evaluate and recommend development tools

### Specialized Department (`specialized/`)
- **search-tuner** - Optimize search functionality across any technology
- **documentation-specialist** - Create and maintain technical documentation
- **financial-guardian** - Manage development costs and budgets
- **gdpr-dpo** - Ensure data privacy compliance
- **legal-compliance-checker** - Handle regulatory requirements
- **threat-modeler** - Assess security risks proactively
- **pwa-optimizer** - Optimize Progressive Web App performance
- **localization-expert** - Handle internationalization and localization
- **project-management/** - Structured project management agents
  - **cli-command-router** - Route CLI commands to appropriate agents
  - **feature-steward** - Manage feature development lifecycle
  - **memorybank-guardian** - Maintain project memory and context
  - **missing-memory-sentinel** - Handle missing project context
  - **scope-gatekeeper** - Enforce project scope boundaries
  - **task-steward** - Manage individual task execution

### Domain Experts (`domain-experts/`)
- **food-beverage/** - Specialized agents for food and beverage applications
  - **recipe-specialist** - Handle recipe data, import, and intelligence

## 🌐 Framework-Agnostic Design

All agents are designed to work across technology stacks:

**Language Support**: JavaScript/TypeScript, Python, Java, C#, Go, Rust, Ruby, PHP, and more
**Framework Detection**: Automatically detect React, Vue, Django, Spring, Rails, Express, etc.
**Pattern Recognition**: Understand MVC, microservices, component-based, and other architectures
**Tool Integration**: Work with npm, pip, maven, cargo, composer, and other package managers

**Key Features**:
- **Context Detection**: Agents analyze your project structure before making recommendations
- **Convention Respect**: Follow existing patterns rather than imposing new ones
- **Multi-Language Examples**: Agents provide relevant examples for your tech stack
- **Universal Patterns**: Apply the same principles across different technologies

## 🎯 Proactive Agents

Some agents trigger automatically in specific contexts:
- **code-reviewer** - After significant code changes (any language)
- **test-writer-fixer** - After implementing features or fixing bugs
- **security-auditor** - When handling sensitive data or authentication
- **dependency-manager** - When package updates or conflicts occur

## 💡 Best Practices

1. **Let agents collaborate** - Complex tasks often benefit from multiple agents working together
2. **Be specific** - Clear task descriptions help agents perform optimally
3. **Trust the expertise** - Each agent is designed for their specific domain
4. **Iterate quickly** - Agents support rapid development and deployment cycles
5. **Maintain quality** - Use testing and review agents throughout development

## 🔧 Technical Details

### Agent Structure
Each agent includes:
- **name**: Unique identifier
- **description**: When to use with detailed examples
- **color**: Visual identification in Claude Code
- **tools**: Specific tools the agent can access
- **System prompt**: Comprehensive expertise and instructions

### Adding Custom Agents
1. Create a new `.md` file in the appropriate department folder
2. Follow the existing YAML frontmatter format
3. Include 3-4 detailed usage examples with context
4. Write comprehensive system prompt (500+ words)
5. Test the agent with real development tasks

## 📊 Agent Performance

Track agent effectiveness through:
- Task completion time and quality
- Bug reduction and code quality metrics
- Developer productivity improvements
- Security vulnerability detection
- User satisfaction scores

## 🛠️ Customization

### Adapting for Your Team
- Modify examples to reflect your technology stack
- Adjust tool permissions based on your workflow
- Customize department structure if needed
- Add company-specific best practices
- Create domain-specific agents for your industry

### Department-Specific Guidelines
- **Engineering**: Focus on code quality, testing, and maintainability
- **Testing**: Emphasize comprehensive coverage and automation
- **Design**: Prioritize user experience and accessibility
- **Operations**: Ensure reliability, security, and scalability
- **Product**: Balance user needs with technical constraints
- **Maintenance**: Prevent technical debt accumulation

## 🚀 Recent Improvements (2025)

### Optimization & Consolidation
- **Reduced agent overlap**: Merged 3 redundant agents for cleaner organization
- **Enhanced performance**: Added explicit performance metrics and targets to core agents
- **Improved security**: Integrated comprehensive security patterns across engineering agents
- **Better language support**: Added specialized JavaScript and TypeScript agents with ES2024+ features

### New Specialized Agents
- **javascript-developer**: Modern JavaScript patterns, performance optimization, memory management
- **typescript-developer**: Advanced type system, generics, enterprise TypeScript architecture  
- **api-developer**: Dedicated API design, documentation, and developer experience
- **code-standards-enforcer**: Automated quality gates, linting, and team consistency

### Enhanced Existing Agents
- **frontend-developer**: Added security implementation and advanced performance patterns
- **backend-architect**: Comprehensive scalability, monitoring, and security architecture
- **data-analyst**: Merged analytics reporting capabilities for complete data intelligence
- **refactorer**: Expanded to include complexity reduction and simplification patterns

## 🚦 Status

- ✅ **Production Ready**: 57 thoroughly tested and documented agents
- 🧪 **Beta**: Continuous improvement based on real-world usage
- 🚧 **Development**: Framework-agnostic patterns for all major tech stacks

## 🤝 Contributing

To improve existing agents or suggest new ones:
1. Follow the agent customization guidelines
2. Test thoroughly with real projects  
3. Document performance improvements
4. Contribute back successful patterns

## 📚 Resources

- [Claude Code Sub-Agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Agent Development Best Practices](https://docs.anthropic.com/en/docs/claude-code/custom-agents)

---

*Built for rapid software development across all domains and technology stacks.*