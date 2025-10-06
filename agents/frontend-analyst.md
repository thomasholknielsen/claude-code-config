---
name: frontend-analyst
description: "Use PROACTIVELY for frontend analysis - provides component architecture evaluation, state management patterns, bundle optimization, and UI framework best practices. This agent conducts comprehensive frontend analysis and returns actionable recommendations for improving component architecture and performance. It does NOT implement changes - it only analyzes frontend code and persists findings to .agent/context/frontend-*.md files. The main thread is responsible for executing recommended frontend improvements based on the analysis. Expect a concise summary with critical architecture issues, bundle optimization strategies, and a reference to the full frontend analysis artifact. Invoke when: keywords include 'frontend', 'component', 'React', 'Vue', 'bundle', 'state', 'UI'; contexts include frontend architecture review, performance optimization, component refactoring; files include React/Vue/Svelte components, frontend build configs."
color: green
model: inherit
tools:

- Read
- Grep
- Glob
- WebSearch
- mcp__context7
