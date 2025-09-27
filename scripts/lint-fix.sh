#!/bin/bash

# Comprehensive linting and auto-fix script for Claude Code Command System
# Excludes spec-kit commands from markdown linting as they have special formatting requirements

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔧 Claude Code Linting & Auto-Fix${NC}"
echo "========================================"

# Function to print status
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✅ $2${NC}"
    else
        echo -e "${RED}❌ $2${NC}"
    fi
}

# Check if we're in the right directory
if [ ! -f ".markdownlint.yml" ]; then
    echo -e "${RED}❌ Error: .markdownlint.yml not found. Run this script from the Claude root directory.${NC}"
    exit 1
fi

echo -e "${BLUE}📝 Markdown Linting (excluding spec-kit commands)${NC}"
echo "------------------------------------------------"

# Run markdownlint with auto-fix, excluding spec-kit commands
npx markdownlint "**/*.md" --ignore node_modules --ignore "commands/spec-kit/" --fix 2>/dev/null
markdown_result=$?
print_status $markdown_result "Markdown auto-fix completed"

# Show remaining markdown issues (if any)
markdown_issues=$(npx markdownlint "**/*.md" --ignore node_modules --ignore "commands/spec-kit/" 2>/dev/null | wc -l)
if [ $markdown_issues -gt 0 ]; then
    echo -e "${YELLOW}⚠️  $markdown_issues markdown issues remain (may require manual fixes)${NC}"
else
    echo -e "${GREEN}✅ All markdown files pass linting${NC}"
fi

echo ""
echo -e "${BLUE}🐍 Python Linting${NC}"
echo "------------------"

# Check if ruff is available
if command -v ruff >/dev/null 2>&1; then
    # Run ruff format (auto-fix formatting)
    ruff format . >/dev/null 2>&1
    format_result=$?
    print_status $format_result "Python formatting auto-fix"

    # Run ruff check with auto-fix
    ruff check --fix . >/dev/null 2>&1
    check_result=$?
    print_status $check_result "Python linting auto-fix"

    # Show remaining Python issues
    python_issues=$(ruff check . 2>/dev/null | wc -l)
    if [ $python_issues -gt 0 ]; then
        echo -e "${YELLOW}⚠️  $python_issues Python issues remain${NC}"
    else
        echo -e "${GREEN}✅ All Python files pass linting${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  ruff not found. Install with: pip install ruff${NC}"
fi

echo ""
echo -e "${BLUE}🐚 Shell Script Linting${NC}"
echo "----------------------"

# Check if shellcheck is available
if command -v shellcheck >/dev/null 2>&1; then
    # Find and check shell scripts
    shell_files=$(find scripts -name "*.sh" 2>/dev/null || echo "")
    if [ -n "$shell_files" ]; then
        shellcheck_issues=0
        for file in $shell_files; do
            if ! shellcheck "$file" >/dev/null 2>&1; then
                ((shellcheck_issues++))
            fi
        done

        if [ $shellcheck_issues -eq 0 ]; then
            print_status 0 "Shell scripts pass linting"
        else
            print_status 1 "$shellcheck_issues shell script issues found"
        fi
    else
        echo -e "${YELLOW}⚠️  No shell scripts found to check${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  shellcheck not found. Install with: brew install shellcheck (macOS) or apt install shellcheck (Linux)${NC}"
fi

echo ""
echo -e "${BLUE}📊 Summary${NC}"
echo "----------"

total_issues=$(($(npx markdownlint "**/*.md" --ignore node_modules --ignore "commands/spec-kit/" 2>/dev/null | wc -l) + $(ruff check . 2>/dev/null | wc -l || echo 0)))

if [ $total_issues -eq 0 ]; then
    echo -e "${GREEN}🎉 All linting checks passed! Code quality is excellent.${NC}"
    exit 0
else
    echo -e "${YELLOW}📋 $total_issues total issues remain across all linters${NC}"
    echo ""
    echo "Next steps:"
    echo "- Review remaining markdown issues manually"
    echo "- Fix Python issues that couldn't be auto-fixed"
    echo "- Run individual linters for detailed output"
    exit 1
fi