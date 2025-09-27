---
description: "Analyzes performance bottlenecks and provides optimization recommendations"
category: "analyze"
agent: "research-orchestrator"
tools: ["Bash", "Read", "Grep", "Task"]
complexity: "complex"
---

# Command: Performance

## Purpose

Identifies performance bottlenecks across frontend, backend, and infrastructure with actionable optimization recommendations.

## Usage

```bash
/analyze:performance [component]
```yaml

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

## Examples

```bash
