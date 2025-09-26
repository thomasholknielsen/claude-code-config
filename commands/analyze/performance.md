---
description: "Analyzes performance bottlenecks and provides optimization recommendations"
category: "analyze"
agent: "research-orchestrator"
tools: ["Bash", "Read", "Grep", "Task"]
complexity: "complex"
---

# Command: Analyze Performance

## Purpose
Identifies performance bottlenecks across frontend, backend, and infrastructure with actionable optimization recommendations.

## Usage
```
/analyze:performance [component]
```

**Arguments**: Optional specific component, endpoint, or performance area to analyze

## Process
1. Coordinate parallel performance analysis across multiple domains
2. Analyze runtime performance, memory usage, and resource consumption
3. Evaluate database queries, API responses, and rendering performance
4. Generate comprehensive performance report with optimization recommendations
5. Prioritize improvements by impact and implementation complexity

## Agent Integration
- **Primary Agent**: research-orchestrator - Coordinates parallel performance analysis
- **Secondary Agents**: Multiple analysis workers for different performance domains

## Profiling Areas

**Runtime Performance:**
- Function execution times and call frequency
- Memory allocation patterns and leaks
- CPU usage hotspots and blocking operations
- Database query performance and N+1 issues

**Resource Analysis:**
- Bundle size analysis and code splitting opportunities
- Image and asset optimization potential
- Network request patterns and caching effectiveness
- Dependency impact on load times

**User Experience Metrics:**
- Core Web Vitals (LCP, FID, CLS)
- Time to interactive and first paint
- Loading states and perceived performance
- Mobile performance characteristics

## Profiling Process

**Measurement phase:**
- Check `.specify/` for performance requirements and targets
- Establish baseline performance metrics
- Run profiling tools appropriate for the platform
- Collect data on identified performance areas
- Generate comparative benchmarks

**Analysis phase:**
- Identify top performance bottlenecks
- Calculate optimization impact potential
- Prioritize fixes by effort vs. impact ratio
- Cross-reference with spec requirements (if `.specify/` exists)
- Document findings with specific recommendations

**Optimization phase:**
- Apply targeted performance improvements
- Measure impact of changes
- Verify no regressions introduced
- Update performance documentation

## Tools Integration

**Automatic tool detection:**
- Browser dev tools for frontend profiling
- Node.js profiler for backend analysis
- Database query analyzers for data layer
- Build analyzers for bundle optimization

## Usage Examples

```
/profile api/users              # Profile user API endpoints
/profile "homepage load time"   # Analyze page load performance  
/profile database               # Database query performance
/profile bundle                 # Bundle size and dependencies
```

Quick performance analysis with actionable optimization recommendations.