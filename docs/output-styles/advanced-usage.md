# Advanced Usage

Master professional output styles with advanced features and customization.

## 🔄 Style Switching Strategies

### Context-Based Switching

Switch styles within the same conversation to get different professional perspectives:

```bash
# Analyze a business problem from multiple angles
/output-style strategic-consultant
"What's our market position in the SaaS space?"

/output-style data-scientist
"What metrics should we track to validate this analysis?"

/output-style product-manager
"How should we prioritize initiatives based on this insight?"
```

### Workflow Integration

Integrate styles into your professional workflows:

**Feature Development Workflow:**

1. `/output-style product-manager` - Define requirements and user stories
2. `/output-style technical-writer` - Create technical specifications
3. `/output-style quality-assurance` - Plan testing strategy
4. `/output-style project-coordinator` - Organize implementation timeline

**Business Analysis Workflow:**

1. `/output-style strategic-consultant` - High-level market analysis
2. `/output-style data-scientist` - Quantitative validation
3. `/output-style marketing-strategist` - Go-to-market strategy
4. `/output-style presentation-designer` - Executive presentation

## 🎯 Confidence Scoring

All professional styles include confidence indicators to help gauge certainty:

### Confidence Levels

- **9-10/10**: High confidence based on established data/frameworks
- **7-8/10**: Medium-high confidence with minor assumptions
- **5-6/10**: Moderate confidence requiring validation
- **3-4/10**: Low confidence suggesting further research needed
- **1-2/10**: Very low confidence with significant uncertainty

### Using Confidence Scores

```text
Example Response:
"Market expansion into Europe shows strong potential with €12M opportunity.

**Confidence Level**: 7/10
- High confidence in market size data (recent reports)
- Medium confidence in competitive analysis (limited intel)
- Requires validation of regulatory complexity"
```

## 🏗️ Professional Frameworks

Each style automatically applies industry-standard frameworks:

### Business & Strategy

- **SWOT Analysis**: Strengths, Weaknesses, Opportunities, Threats
- **RICE Prioritization**: Reach × Impact × Confidence ÷ Effort
- **Porter's Five Forces**: Competitive analysis framework
- **BCG Matrix**: Business portfolio analysis

### Technical & Analysis

- **Scientific Method**: Hypothesis → Test → Analyze → Conclude
- **Statistical Analysis**: Significance testing, confidence intervals
- **System Design**: Architecture patterns, scalability considerations

### Creative & Design

- **Design Thinking**: Empathize → Define → Ideate → Prototype → Test
- **User Journey Mapping**: Touchpoint analysis and optimization
- **Brand Strategy**: Positioning, voice, personality development

### Operations & Compliance

- **Risk Management**: Identification, assessment, mitigation
- **Project Management**: WBS, critical path, resource allocation
- **Quality Assurance**: Prevention, detection, correction cycles

## 🛠️ Customization Guide

### Organization-Specific Adaptations

Customize styles for your organization's needs:

1. **Copy Base Style**

   ```bash
   cp ~/.claude/output-styles/product-manager.md ./custom-pm.md
   ```

2. **Modify Instructions**

   ```yaml
   ---
   name: "Acme Product Manager"
   description: "Product management with Acme frameworks and terminology"
   ---

   # Custom instructions here
   Use Acme's proprietary IMPACT framework instead of RICE...
   Always reference our user research database...
   Include competitive analysis against [specific competitors]...
   ```

3. **Add Company Context**
   - Internal process terminology
   - Specific tools and platforms used
   - Company values and communication style
   - Industry-specific regulations or requirements

### Team Style Libraries

Create shared style libraries for teams:

```text
team-styles/
├── engineering/
│   ├── senior-engineer.md
│   ├── tech-lead.md
│   └── architect.md
├── marketing/
│   ├── content-specialist.md
│   ├── campaign-manager.md
│   └── growth-hacker.md
└── operations/
    ├── scrum-master.md
    ├── release-manager.md
    └── devops-engineer.md
```

## 🚀 Performance Optimization

### Token Efficiency Tips

Professional styles are designed for efficiency:

- **50% token reduction**: Focused communication eliminates verbose explanations
- **Structured output**: Consistent formatting reduces repetitive context
- **Framework shortcuts**: Professional patterns replace lengthy descriptions
- **Confidence scoring**: Replaces uncertain hedging language

### Best Practices

1. **Choose the right style**: Match style to task for maximum efficiency
2. **Use style switching**: Get multiple perspectives without separate conversations
3. **Leverage frameworks**: Let styles apply professional structures automatically
4. **Trust confidence scores**: Use uncertainty indicators to guide follow-up questions

## 🔗 Integration with Claude Code

### Command Integration

Combine styles with Claude Code commands:

```bash
# Analyze codebase with technical style
/output-style technical-writer
/analyze:performance

# Document findings with presentation style
/output-style presentation-designer
/docs:generate

# Plan implementation with project coordination
/output-style project-coordinator
/implement:plan
```

### Agent Orchestra Coordination

Professional styles work with Claude Code's agent system:

- **Orchestrators** can switch styles based on task complexity
- **Workers** can use domain-appropriate styles automatically
- **Review processes** can apply multiple style perspectives

## 📊 Measuring Effectiveness

Track the impact of professional styles:

### Quantitative Metrics

- Response length reduction (target: 30-50% shorter)
- Time to useful output (faster professional formatting)
- Context efficiency (fewer clarification rounds needed)

### Qualitative Improvements

- Professional communication quality
- Stakeholder satisfaction with outputs
- Consistency across team communications
- Framework application accuracy

## Next Steps

- **[Examples →](examples.md)** - See advanced techniques in action
- **[Troubleshooting →](troubleshooting.md)** - Solve common issues
- **[Style Catalog →](style-catalog.md)** - Explore all available styles

---

**🎯 Advanced Tip**: Create style workflows for your most common professional tasks to maximize
efficiency and maintain consistency across your team's AI interactions.
