# Agent Context Directory

This directory stores session-based context files created by domain analysts during their analysis work.

## File Pattern

```text
.agent/Session-{name}/context/{agent-name}.md
```

**Example**: `.agent/Session-{name}/context/abc123/python-analyst.md`

## Purpose

Domain analysts use these files to:

- Persist comprehensive research findings
- Store detailed analysis results
- Enable coordination between multiple analysts
- Provide context elision (detailed findings here, concise summaries to main thread)

## Retention Policy

**Automatic Cleanup**: Context files older than 30 days should be manually cleaned up.

**Manual Cleanup**:

```
# Remove files older than 30 days
find ~/.claude/.agent/context -name "*.md" -mtime +30 -delete
```

**Session-Based Cleanup**:

```
# Remove all files for a specific session ID
find ~/.claude/.agent/context -name "*-{sessionid}.md" -delete
```

## Security

- **NOT committed to git**: All `.md`, `.json`, and `.log` files are gitignored
- **Session-specific**: Files are isolated per session to prevent cross-contamination
- **Privacy**: Context files may contain sensitive code analysis data

## Directory Structure

```
.agent/
├── context/               # Session context files (gitignored)
│   ├── .gitkeep          # Preserves directory in git
│   └── {YYYY-MM-DD}-{topic}-{sessionid}.md
└── README.md             # This file
```

## Usage by Agents

All 16 domain analysts persist findings here:

- research-analyst, react-analyst, typescript-analyst, python-analyst
- api-analyst, quality-analyst, architecture-analyst, refactoring-analyst
- security-analyst, performance-analyst, testing-analyst, accessibility-analyst
- documentation-analyst, database-analyst, frontend-analyst, shadcn-analyst

Agents obtain session ID via: `python ~/.claude/scripts/session/session_manager.py current`
