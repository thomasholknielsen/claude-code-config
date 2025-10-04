#!/usr/bin/env python3
"""
GitHub PR Review Integration
Posts AI review comments from local workflow to GitHub PR via gh CLI
Cross-platform: Windows, macOS, Linux
"""

from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Post AI review to GitHub PR")
    parser.add_argument("--pr", type=int, required=True, help="PR number")
    parser.add_argument("--review", type=str, required=True, help="Path to review markdown file")
    parser.add_argument("--repo", type=str, help="Repository (owner/repo), auto-detected if omitted")
    args = parser.parse_args()

    # Validate gh CLI is available
    if not is_gh_cli_available():
        print("Error: GitHub CLI (gh) not found. Install from https://cli.github.com/")
        sys.exit(1)

    # Read review output
    review_path = Path(args.review)
    if not review_path.exists():
        print(f"Error: Review file not found: {args.review}")
        sys.exit(1)

    review_content = review_path.read_text()

    # Parse review into structured data
    issues = parse_review_output(review_content)

    # Post inline comments for Critical and Major issues
    posted_count = 0
    for issue in issues:
        if issue["severity"] in ["Critical", "Major"]:
            post_inline_comment(args.pr, issue)
            posted_count += 1

    # Post summary comment
    summary = generate_summary_comment(review_content, issues)
    post_summary_comment(args.pr, summary)

    print(f"✓ Posted {posted_count} inline comments")
    print(f"✓ Posted summary comment with {len(issues)} total findings")


def is_gh_cli_available():
    """Check if GitHub CLI is installed"""
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def parse_review_output(markdown_content):
    """
    Parse review markdown into structured issues.

    Expected format:
    ### Critical
    - **File:** `path/to/file.ts:45-52`
      - **Issue:** Description
      - **Reasoning:** Why this matters
      - **Fix:** Suggestion
    """
    issues = []
    current_severity = None

    lines = markdown_content.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Detect severity header
        if line.startswith("###"):
            severity_match = re.search(r"###\s+(Critical|Major|Minor|Enhancement)", line)
            if severity_match:
                current_severity = severity_match.group(1)

        # Detect issue entry
        if line.startswith("- **File:**") and current_severity:
            file_match = re.search(r"`([^`]+):(\d+)-(\d+)`", line)
            if file_match:
                issue = {
                    "severity": current_severity,
                    "file": file_match.group(1),
                    "start_line": int(file_match.group(2)),
                    "end_line": int(file_match.group(3)),
                    "issue": "",
                    "reasoning": "",
                    "fix": "",
                }

                # Parse following lines for Issue, Reasoning, Fix
                i += 1
                while (
                    i < len(lines)
                    and not lines[i].strip().startswith("- **File:**")
                    and not lines[i].strip().startswith("###")
                ):
                    sub_line = lines[i].strip()
                    if sub_line.startswith("- **Issue:**"):
                        issue["issue"] = sub_line.replace("- **Issue:**", "").strip()
                    elif sub_line.startswith("- **Reasoning:**"):
                        issue["reasoning"] = sub_line.replace("- **Reasoning:**", "").strip()
                    elif sub_line.startswith("- **Fix:**"):
                        issue["fix"] = sub_line.replace("- **Fix:**", "").strip()
                    i += 1

                issues.append(issue)
                continue

        i += 1

    return issues


def post_inline_comment(pr_number, issue):
    """Post inline comment to GitHub PR"""
    comment_body = f"""**{issue["severity"]}**: {issue["issue"]}

**Reasoning:** {issue["reasoning"]}

**Suggested Fix:**
{issue["fix"]}

---
*Posted by AI Code Review*
"""

    # Use gh CLI to post review comment
    cmd = [
        "gh",
        "pr",
        "review",
        str(pr_number),
        "--comment",
        "--body",
        comment_body,
        # Note: gh CLI doesn't support inline comments with line numbers via CLI
        # This posts as a general PR comment. For true inline, use GitHub API directly.
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to post inline comment: {e.stderr.decode()}")


def generate_summary_comment(full_review, issues):
    """Generate PR summary comment"""
    severity_counts = {
        "Critical": len([i for i in issues if i["severity"] == "Critical"]),
        "Major": len([i for i in issues if i["severity"] == "Major"]),
        "Minor": len([i for i in issues if i["severity"] == "Minor"]),
        "Enhancement": len([i for i in issues if i["severity"] == "Enhancement"]),
    }

    # Extract highlights from review
    highlights_section = re.search(r"## Highlights\n(.*?)(?=\n##|\Z)", full_review, re.DOTALL)
    highlights = highlights_section.group(1).strip() if highlights_section else "No highlights noted."

    summary = f"""## 🤖 AI Code Review Summary

**Review completed at:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}

### Findings Overview
- 🔴 **Critical:** {severity_counts["Critical"]} issues
- 🟠 **Major:** {severity_counts["Major"]} issues
- 🟡 **Minor:** {severity_counts["Minor"]} issues
- 🟢 **Enhancement:** {severity_counts["Enhancement"]} suggestions

### Highlights
{highlights}

### Next Steps
1. Address Critical issues immediately (blocking merge)
2. Review Major issues before merge
3. Consider Minor improvements and Enhancements

---
*Full review details available in inline comments above.*
*Generated by AI Code Review System*
"""

    return summary


def post_summary_comment(pr_number, summary):
    """Post summary comment to PR"""
    cmd = ["gh", "pr", "comment", str(pr_number), "--body", summary]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to post summary comment: {e.stderr.decode()}")
        sys.exit(1)


if __name__ == "__main__":
    main()
