---
description: Performance bottleneck analysis with optimization recommendations
category: performance
tools: Bash, Read, Grep
---

# Performance Profiling

I'll analyze performance bottlenecks and provide optimization recommendations.

Arguments: `$ARGUMENTS` - specific component, endpoint, or performance area to analyze

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
- Establish baseline performance metrics
- Run profiling tools appropriate for the platform
- Collect data on identified performance areas
- Generate comparative benchmarks

**Analysis phase:**
- Identify top performance bottlenecks
- Calculate optimization impact potential
- Prioritize fixes by effort vs. impact ratio
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