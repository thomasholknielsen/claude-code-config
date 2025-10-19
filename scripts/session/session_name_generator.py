#!/usr/bin/env python3
"""
Session Name Generator Utility
Generates meaningful session name suggestions from freeform user input.
"""

import re
from typing import Dict


def suggest_session_names(freeform_input: str) -> Dict[str, Dict[str, str]]:
    """
    Generate 3 session name suggestions from freeform input.

    Args:
        freeform_input: User-provided text describing the session topic

    Returns:
        dict: {
            "A": {"name": "direct-suggestion", "type": "Direct", "description": "..."},
            "B": {"name": "contextual-suggestion", "type": "Contextual", "description": "..."},
            "C": {"name": "abstract-suggestion", "type": "Abstract", "description": "..."}
        }

    Example:
        >>> suggest_session_names("fix authentication bug in login")
        {
            "A": {"name": "fix-auth-bug-login", "type": "Direct", ...},
            "B": {"name": "fix-auth-login", "type": "Contextual", ...},
            "C": {"name": "auth-bug-fix", "type": "Abstract", ...}
        }
    """
    # Normalize input: lowercase, extract tokens
    input_lower = freeform_input.lower().strip()

    # Common stop words to filter
    stop_words = {
        "of",
        "the",
        "a",
        "an",
        "is",
        "are",
        "was",
        "were",
        "from",
        "to",
        "for",
        "with",
        "in",
        "on",
        "at",
        "and",
        "or",
        "but",
        "not",
        "i",
        "you",
        "we",
        "it",
        "this",
        "that",
        "these",
        "those",
        "be",
        "have",
        "do",
    }

    # Tokenize: split by non-alphanumeric characters
    tokens = re.findall(r"[a-z0-9]+", input_lower)

    # Remove stop words
    meaningful_tokens = [t for t in tokens if t not in stop_words]

    # If no meaningful tokens, use first few tokens anyway
    if not meaningful_tokens:
        meaningful_tokens = tokens[:3]

    # Limit to reasonable length
    meaningful_tokens = meaningful_tokens[:5]

    # ===== OPTION A: Direct (first N tokens) =====
    direct_name = "-".join(meaningful_tokens[:4]) if meaningful_tokens else "task"
    direct_name = direct_name[:50]  # Max 50 chars
    direct_chars = len(direct_name)

    # ===== OPTION B: Contextual (add action verb + main tokens) =====
    # Infer action from common words
    action_verb = "implement"
    if any(word in input_lower for word in ["fix", "bug", "error"]):
        action_verb = "fix"
    elif any(word in input_lower for word in ["refactor", "redesign", "improve"]):
        action_verb = "refactor"
    elif any(word in input_lower for word in ["add", "create", "new", "feature"]):
        action_verb = "add"
    elif any(word in input_lower for word in ["review", "audit", "analyze", "check"]):
        action_verb = "review"
    elif any(word in input_lower for word in ["integrate", "connect", "link", "sync"]):
        action_verb = "integrate"
    elif any(word in input_lower for word in ["test", "verify"]):
        action_verb = "test"

    contextual_parts = [action_verb] + meaningful_tokens[:3]
    contextual_name = "-".join(contextual_parts)
    contextual_name = contextual_name[:50]  # Max 50 chars
    contextual_chars = len(contextual_name)

    # ===== OPTION C: Abstract (domain + category) =====
    # Infer domain/category from keywords
    domain = "task"

    domain_keywords = {
        "auth": ["auth", "login", "password", "authentication", "security"],
        "api": ["api", "endpoint", "request", "response", "http"],
        "db": ["database", "db", "sql", "query", "migration"],
        "ui": ["ui", "component", "button", "form", "design", "frontend"],
        "test": ["test", "unit", "integration", "e2e"],
        "doc": ["doc", "documentation", "readme", "guide"],
        "infra": ["infrastructure", "deploy", "cloud", "server"],
        "perf": ["performance", "optimize", "speed", "benchmark"],
    }

    for category, keywords in domain_keywords.items():
        if any(kw in input_lower for kw in keywords):
            domain = category
            break

    # Category from action
    category = "work"
    if action_verb == "fix":
        category = "bugfix"
    elif action_verb == "refactor":
        category = "refactor"
    elif action_verb == "add":
        category = "feature"
    elif action_verb == "review":
        category = "review"
    elif action_verb == "test":
        category = "testing"

    abstract_name = f"{domain}-{category}"
    abstract_name = abstract_name[:50]  # Max 50 chars
    abstract_chars = len(abstract_name)

    return {
        "A": {
            "name": direct_name,
            "type": "Direct",
            "description": f"Straightforward from your input ({direct_chars} chars)",
        },
        "B": {
            "name": contextual_name,
            "type": "Contextual",
            "description": f"With action context ({contextual_chars} chars)",
        },
        "C": {"name": abstract_name, "type": "Abstract", "description": f"Domain-based ({abstract_chars} chars)"},
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: session_name_generator.py '<freeform-input>'")
        print("Example: session_name_generator.py 'fix authentication bug'")
        sys.exit(1)

    input_text = " ".join(sys.argv[1:])
    suggestions = suggest_session_names(input_text)

    # Print in markdown table format
    print("\nSession Name Suggestions:")
    print()
    print("| Option | Session Name | Type | Description |")
    print("|--------|--------------|------|-------------|")
    for key in ["A", "B", "C"]:
        s = suggestions[key]
        print(f"| {key} | `{s['name']}` | {s['type']} | {s['description']} |")
    print()
