# Documentation Analyzer

I'll comprehensively analyze your project's documentation coverage, quality, and freshness to identify gaps and improvement opportunities.

**My analysis approach:**
1. **Map all documentation** - Find every doc file in the project
2. **Analyze code vs docs** - Compare implementation with documentation
3. **Check freshness** - Identify outdated or stale content
4. **Assess completeness** - Find undocumented features and APIs
5. **Report findings** - Prioritized recommendations for improvement

## Analysis Scope

### Documentation Discovery (GitHub-Friendly Structure)
I'll find and analyze following the standardized architecture:

**Root-Level Documentation (GitHub Special Files):**
- **README.md** - Entry point quality and GitHub optimization
- **LICENSE** - Legal license presence and validity
- **CHANGELOG.md** - Version history and release notes
- **CONTRIBUTING.md** - Contribution guidelines (GitHub integration)
- **SECURITY.md** - Security vulnerability reporting instructions
- **CODE_OF_CONDUCT.md** - Community behavior guidelines
- **CODEOWNERS** - GitHub review assignment configuration

**docs/ Folder Documentation (Hierarchical Structure):**
- **docs/user/** - End-user documentation organization and completeness
- **docs/developer/** - Developer documentation (API reference, architecture)
- **docs/admin/** - Administrator documentation (configuration, deployment)
- **docs/concepts/** - Conceptual documentation (design principles, glossary)

**Code-Level Documentation:**
- **Inline comments** - Code documentation, docstrings
- **API annotations** - OpenAPI specs, JSDoc
- **Spec-kit docs** - Feature specifications in `.specify/`

### Coverage Analysis
For each area, I'll check:
- **API endpoints** - Are all routes documented?
- **Functions/classes** - Missing docstrings or comments?
- **Configuration** - Are all options explained?
- **Dependencies** - Are requirements documented?
- **Setup/deployment** - Complete installation guides?
- **Architecture** - System design documentation?

### Quality Assessment
I'll evaluate:
- **Accuracy** - Does documentation match implementation?
- **Completeness** - Are all features covered?
- **Consistency** - Uniform style and structure?
- **Freshness** - Recently updated content?
- **Accessibility** - Clear for new developers?
- **Examples** - Working code samples?

## Analysis Output

### Comprehensive Report
```
DOCUMENTATION ANALYSIS REPORT
Generated: [timestamp]

OVERVIEW
├── Total files: 15
├── Coverage score: 73%
├── Last updated: 2 weeks ago
└── Quality score: 82%

STRUCTURE COMPLIANCE (Industry Standards)
├── README.md: ✓ Present, concise entry point with docs/ links
├── LICENSE: ✓ Present, valid open source license
├── CONTRIBUTING.md: ✓ Present, GitHub integration enabled
├── SECURITY.md: ⚠ Present but needs security contact update
├── CODE_OF_CONDUCT.md: ❌ Missing
├── docs/ hierarchy: ✓ Audience-organized structure
├── _index.md files: ⚠ Missing in 3 directories
├── Naming convention: ✓ Underscores used correctly
└── Hierarchy depth: ✓ Maximum 2 levels maintained

COVERAGE BY CATEGORY
├── Root Documentation (GitHub Special Files)
│   ├── README.md: 90% complete (missing docs/ section links)
│   ├── LICENSE: 100% complete
│   ├── CHANGELOG.md: 60% (6 months outdated)
│   ├── CONTRIBUTING.md: 80% (good GitHub integration)
│   ├── SECURITY.md: 70% (needs contact update)
│   └── CODE_OF_CONDUCT.md: ❌ Missing entirely
├── docs/ Hierarchical Documentation
│   ├── user/: 75% (missing tutorials section)
│   │   ├── getting-started/: 90% complete
│   │   └── guides/: 60% (troubleshooting incomplete)
│   ├── developer/: 85% well-organized
│   │   ├── api-reference/: 85% (17/20 endpoints)
│   │   ├── contributing/: 90% complete
│   │   └── architecture/: 80% (system overview good)
│   ├── admin/: 70% needs expansion
│   │   ├── configuration/: 90% (env vars documented)
│   │   └── deployment/: 60% (production guide incomplete)
│   └── concepts/: 50% foundational content missing
└── Code Documentation: 45% (90/200 functions documented)

QUALITY ISSUES
├── Critical (4)
│   ├── CODE_OF_CONDUCT.md - Missing entirely (required for GitHub)
│   ├── Missing _index.md files in 3 docs/ directories
│   ├── README.md - Missing navigation links to docs/ hierarchy
│   └── docs/developer/api-reference/ - 3 endpoints undocumented
├── High (6)
│   ├── CHANGELOG.md - 6 months outdated
│   ├── SECURITY.md - Needs current security contact info
│   ├── docs/user/tutorials/ - Missing tutorial content
│   ├── docs/concepts/ - Foundational content incomplete
│   └── [other issues...]
└── Medium (10)
    ├── docs/admin/deployment/ - Production guide incomplete
    ├── Filename conventions - 2 files need underscores
    └── [minor issues...]

RECOMMENDATIONS
1. Create CODE_OF_CONDUCT.md using GitHub template (priority: critical)
2. Add missing _index.md files to all docs/ directories (priority: critical)
3. Update README.md with clear docs/ navigation structure (priority: critical)
4. Complete docs/developer/api-reference/ documentation (priority: critical)
5. Update CHANGELOG.md with recent 6 months of changes (priority: high)
6. Expand docs/concepts/ with foundational content (priority: high)
```

### Detailed Findings

For each documentation file, I'll provide:
- **Status**: Current, outdated, missing, or broken
- **Completeness**: Percentage of covered topics
- **Last modified**: When it was last updated
- **Issues found**: Specific problems and recommendations
- **Improvement suggestions**: Actionable next steps

### Code Documentation Analysis
- **Functions without docstrings**: List with file locations
- **Complex logic uncommented**: Areas needing explanation
- **API endpoints undocumented**: Routes missing documentation
- **Configuration undocumented**: Settings without explanations

## Integration with Development Workflow

### Automated Analysis Triggers
Run analysis:
- **Before releases** - Ensure docs are ready for public consumption
- **After major features** - Check if new functionality is documented
- **During code reviews** - Verify documentation standards
- **Monthly health checks** - Keep documentation current

### Command Combinations
```bash
/docs analyze && /docs update
# Analyze gaps, then update documentation to fix issues

/explain architecture && /docs analyze
# Understand current architecture, then analyze doc coverage

/docs analyze && /docs generate
# Find gaps, then generate missing documentation
```

## Language/Framework Awareness

### Technology Detection
I automatically detect and adapt analysis for:
- **JavaScript/TypeScript** - JSDoc, TypeScript definitions
- **Python** - Docstrings, Sphinx documentation
- **Java** - JavaDoc, Maven documentation
- **Go** - Go doc comments, module documentation
- **Rust** - Rustdoc, crate documentation
- **C#/.NET** - XML documentation, NuGet docs

### Framework-Specific Analysis
- **Express.js** - Route documentation, middleware docs
- **React** - Component prop documentation, story files
- **Django** - Model documentation, admin docs
- **Spring Boot** - Annotation documentation, API specs
- **Rails** - Model/controller documentation, route docs

## Analysis Depth Levels

### Quick Analysis (Default)
- File inventory and basic coverage metrics
- Critical missing documentation identification
- Quick quality assessment
- 30-second overview for daily use

### Deep Analysis
- Line-by-line documentation review
- Cross-reference validation between docs
- Comprehensive gap analysis
- Detailed improvement roadmap
- Use when preparing for releases or audits

### Focus Analysis
Analyze specific areas:
- `/docs analyze api` - Focus on API documentation only
- `/docs analyze setup` - Focus on installation/setup docs
- `/docs analyze code` - Focus on inline code documentation

## Quality Metrics

### Documentation Health Score
Calculated from:
- **Coverage**: Percentage of features documented
- **Freshness**: How recently docs were updated
- **Accuracy**: Alignment with actual implementation
- **Completeness**: Presence of required sections
- **Consistency**: Uniform style and structure

### Trending Analysis
Track changes over time:
- Documentation coverage improvements
- Quality score evolution
- Most/least documented areas
- Update frequency patterns

This analysis helps prioritize documentation work and maintains high-quality, comprehensive project documentation.