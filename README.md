# Claude Code Configuration

Personal configuration repository for Claude Code customizations and extensions.

## Overview

This repository contains a comprehensive set of custom configurations, agents, and commands to enhance the Claude Code development experience. It includes intelligent notification systems, specialized development agents, and workflow automation tools.

## Directory Structure

### Core Configuration
- **settings.json**: Main configuration file with hook definitions for macOS notifications
- **scripts/**: Supporting scripts for system integration and smart notifications
- **.gitignore**: Version control configuration to track only essential directories

### Extensions & Customizations
- **agents/**: Custom agent definitions for specialized development workflows
  - `engineering/`: Engineering-focused agents
  - `specialized/`: Domain-specific agents
  - `stage-0-prototype/`: Prototyping agents
  - `stage-1-mvp/`: MVP development agents
- **commands/**: Custom commands extending Claude Code functionality
  - `act`, `commit`, `clean`: Development workflow commands
  - `add-to-changelog`, `context-prime`: Documentation and context tools

### Project Management
- **projects/**: Project-specific Claude Code configurations
- **todos/**: Task tracking and todo management system
- **shell-snapshots/**: Shell session snapshots for debugging and history
- **ide/**: IDE-specific configurations and integrations
- **plugins/**: Custom plugins and extensions
- **statsig/**: Analytics and feature flag configurations

## Key Features

### Smart Notifications
- **Intelligent macOS Integration**: Automatic notifications with context-aware messages
- **Transcript Analysis**: Extracts and displays relevant completion messages
- **Multiple Notification Methods**: Support for both `terminal-notifier` and native `osascript`
- **Session Context**: Shows current working directory in notifications

### Development Workflow
- **Custom Agents**: Specialized AI agents for different development phases
- **Workflow Commands**: Streamlined commands for common development tasks
- **Project-Specific Configs**: Tailored settings per project
- **Hook System**: Event-driven automation for development workflows

## Setup & Usage

This repository serves as the `~/.claude` configuration directory for Claude Code. Upon installation:

1. Clone or initialize this repository in `~/.claude/`
2. Ensure scripts are executable: `chmod +x scripts/*.sh`
3. Configure notification preferences in `scripts/notify-smart.sh`
4. Customize agents and commands based on your development needs

The configuration is automatically loaded when using the Claude Code CLI tool.

## Notification System

The smart notification system (`scripts/notify-smart.sh`) provides:
- Real-time task completion notifications
- Context-aware message extraction from transcripts
- Configurable notification methods (terminal-notifier/osascript)
- Session directory identification
- Message truncation and formatting for optimal display

## Customization

- **Agents**: Add new specialized agents in the `agents/` directory
- **Commands**: Extend functionality with custom commands in `commands/`
- **Hooks**: Configure additional automation in `settings.json`
- **Projects**: Create project-specific configurations in `projects/`