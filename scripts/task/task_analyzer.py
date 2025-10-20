#!/usr/bin/env python3
"""
Task Analyzer - Smart Metadata Extraction for Task Management

Analyzes noisy user input to intelligently infer structured task metadata:
- Dependencies (temporal language, explicit references)
- Epic assignment (context keywords)
- Priority (hint patterns: [BLOCKER], [URGENT])
- Category (language analysis: fix→bug, add→feature)
- Related tasks (semantic matching)

Uses 10-phase pipeline:
1. Extract Explicit References (TASK-XXX, #issues)
2. Parse Hint Patterns ([BLOCKER], after X, related to, etc.)
3. Extract Keywords (tokenize, remove stopwords)
4. Semantic Matching (find related tasks)
5. Detect Epic (explicit mentions + context)
6. Infer Priority (from hints + relationships)
7. Detect Category (language patterns)
8. Infer Dependencies (main logic)
9. Calculate Confidence (score each inference)
10. Generate Reasoning (explain decisions)
"""

import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional, Tuple

from config import TaskAnalyzerConfig
from markdown_parser import parse_task_blocks, parse_task_full
from task_matcher import TaskMatcher


class TaskAnalyzer:
    """
    Analyzes noisy task descriptions to extract structured metadata.
    Zero prompts, pure inference from text analysis.
    """

    # ========================================================================
    # INITIALIZATION
    # ========================================================================

    def __init__(self, tasks: List[Dict], epics: Optional[List[str]] = None) -> None:
        """
        Initialize TaskAnalyzer with existing tasks and epics.

        Args:
            tasks: List of task dicts with id, title, description, epic, status, priority
            epics: List of epic names (auto-extracted from tasks if not provided)
        """
        # Common stopwords to ignore during analysis
        self.stopwords = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "from",
            "up",
            "we",
            "this",
            "that",
            "is",
            "be",
            "have",
            "do",
            "should",
            "could",
            "would",
            "need",
            "after",
            "before",
            "then",
            "during",
            "when",
            "where",
            "what",
            "which",
            "who",
            "how",
            "it",
            "its",
            "was",
            "were",
            "been",
            "being",
            "am",
            "are",
            "has",
            "had",
            "having",
            "does",
            "did",
            "doing",
            "will",
            "shall",
            "can",
            "may",
            "might",
            "must",
            "not",
            "no",
            "as",
            "if",
            "so",
            "too",
            "also",
            "only",
            "just",
            "very",
            "get",
            "got",
            "make",
            "made",
            "more",
            "most",
            "some",
            "such",
            "these",
            "those",
            "all",
            "each",
            "every",
            "both",
            "either",
            "neither",
            "any",
            "many",
            "much",
            "few",
        }

        # Initialize tasks and task_by_id
        self.tasks = tasks
        self.task_by_id = {t["id"]: t for t in tasks}

        # Build epic list from tasks or use provided
        if epics:
            self.epics = epics
        else:
            self.epics = list({t.get("epic") for t in tasks if t.get("epic")})

        # Pre-build keyword index for all tasks
        self.keywords_by_task = self._build_keyword_index(tasks)

        # Initialize task matcher for semantic search (extracted for Single Responsibility)
        self.matcher = TaskMatcher(self.tasks, self.keywords_by_task)

    def analyze(self, user_input: str) -> Dict:
        """
        Main entry point: convert noisy input to structured metadata.

        Args:
            user_input: Noisy task description from user

        Returns:
            Dict with keys:
            - depends_on: List of TASK-XXX IDs
            - epic: Epic name (or None)
            - priority: "low", "medium", "high", "critical"
            - category: "feature", "bug", "refactor", "docs", "chore", "research"
            - confidence: Dict of confidence scores
            - reasoning: List of human-readable explanations
            - related: List of related TASK-XXX IDs
        """
        # Phase 1: Extract explicit references
        explicit_tasks = self._extract_task_references(user_input)
        explicit_issues = self._extract_issue_references(user_input)

        # Phase 2: Parse hint patterns
        hints = self._parse_hint_patterns(user_input)

        # Phase 3: Extract keywords and tokenize
        keywords = self._extract_keywords(user_input)

        # Phase 4: Semantic matching against existing tasks
        task_matches = self._semantic_search_tasks(keywords)

        # Phase 5: Detect epic from context
        epic, epic_confidence = self._detect_epic(user_input, keywords, task_matches)

        # Phase 6: Determine priority
        priority = self._infer_priority(hints, task_matches)

        # Phase 7: Detect category
        category = self._detect_category(user_input, keywords)

        # Phase 8: Infer dependencies (main logic)
        depends_on = self._infer_dependencies(explicit_tasks, hints, keywords, task_matches, user_input)

        # Phase 9: Build confidence scores
        confidence = self._calculate_confidence(depends_on, epic, priority, category, hints, explicit_tasks)

        # Phase 10: Generate reasoning for user
        reasoning = self._generate_reasoning(
            user_input, explicit_tasks, hints, task_matches, epic, depends_on, priority, category
        )

        # Infer related tasks
        related = self._infer_related(task_matches, depends_on)

        return {
            "depends_on": depends_on,
            "epic": epic,
            "priority": priority,
            "category": category,
            "confidence": confidence,
            "reasoning": reasoning,
            "related": related,
            "explicit_issues": explicit_issues,
        }

    # ========================================================================
    # PHASE 1: Extract Explicit References
    # ========================================================================

    def _extract_task_references(self, text: str) -> List[str]:
        """
        Find explicit TASK-XXX references in text.
        Most reliable: explicit user reference.

        Example:
            "after TASK-015" → ["TASK-015"]
        """
        pattern = r"TASK-(\d+)"
        matches = re.findall(pattern, text)
        return [f"TASK-{m}" for m in matches]

    def _extract_issue_references(self, text: str) -> List[str]:
        """Find GitHub issue references: #123"""
        pattern = r"#(\d+)"
        matches = re.findall(pattern, text)
        return [f"#{m}" for m in matches]

    # ========================================================================
    # PHASE 2: Parse Hint Patterns
    # ========================================================================

    def _parse_hint_patterns(self, text: str) -> Dict[str, bool]:
        """
        Extract structured hints from special markers and keywords.
        These provide strong signals about task nature.

        Example:
            "[BLOCKER] fix auth after TASK-015"
            → {blocker: True, temporal: 'after', depends_on_phrase: False}
        """
        hints = {}

        # Blocker/Urgency markers
        hints["blocker"] = bool(re.search(r"\[BLOCKER\]", text, re.I))
        hints["urgent"] = bool(re.search(r"\[URGENT\]", text, re.I))
        hints["followup"] = bool(re.search(r"\[FOLLOW.?UP\]", text, re.I))

        # Temporal relationships
        hints["temporal"] = None
        if re.search(r"\bafter\s+(?:TASK-\d+|(?:we|the|this|fixing|completing))", text, re.I):
            hints["temporal"] = "after"
        elif re.search(r"\bbefore\s+(?:TASK-\d+|(?:we|the|this|starting))", text, re.I):
            hints["temporal"] = "before"
        elif re.search(r"\bthen\s+", text, re.I):
            hints["temporal"] = "sequential"

        # Dependency signals
        hints["depends_on_phrase"] = bool(re.search(r"depends\s+on", text, re.I))
        hints["blocks_phrase"] = bool(re.search(r"blocks?\s+", text, re.I))
        hints["unblocks_phrase"] = bool(re.search(r"unblocks?\s+", text, re.I))

        # Relationship signals
        hints["related_to_phrase"] = bool(re.search(r"related\s+to", text, re.I))
        hints["similar_to_phrase"] = bool(re.search(r"similar\s+to", text, re.I))
        hints["part_of_phrase"] = bool(re.search(r"part\s+of", text, re.I))

        return hints

    # ========================================================================
    # PHASE 3: Extract Keywords
    # ========================================================================

    def _extract_keywords(self, text: str) -> List[str]:
        """
        Extract meaningful keywords from text.
        Remove stopwords, lowercase, tokenize.

        Example:
            "fix the auth validation thing after context refactor"
            → ["fix", "auth", "validation", "thing", "context", "refactor"]
        """
        # Tokenize and clean
        tokens = re.findall(r"\b[a-z0-9_-]+\b", text.lower())
        keywords = [t for t in tokens if t not in self.stopwords and len(t) > 2]
        return keywords

    # ========================================================================
    # PHASE 4: Semantic Matching Against Existing Tasks
    # ========================================================================

    def _semantic_search_tasks(self, keywords: List[str]) -> List[Tuple[Dict, float]]:
        """
        Find existing tasks that match keywords semantically.
        Delegates to TaskMatcher (extracted for Single Responsibility Principle).

        Example:
            keywords: ["auth", "validation"]
            → [(TASK-016, 0.92), (TASK-010, 0.87), (TASK-003, 0.45)]
        """
        return self.matcher.find_matches(keywords)

    # ========================================================================
    # PHASE 5: Detect Epic
    # ========================================================================

    def _detect_epic(
        self, user_input: str, keywords: List[str], task_matches: List[Tuple[Dict, float]]
    ) -> Tuple[Optional[str], float]:
        """
        Determine which epic this task belongs to.
        Uses: explicit mentions, task_matches context, keyword matching.

        Example:
            user_input: "align agents with template"
            keywords: ["align", "agents", "template"]
            task_matches: [(TASK-003 in "Template Standardization", 0.92), ...]
            → ("Template Standardization", 0.91)
        """
        candidate_epics = {}  # epic_name → confidence_score

        # Check for explicit epic mention
        for epic_name in self.epics:
            if epic_name.lower() in user_input.lower():
                candidate_epics[epic_name] = TaskAnalyzerConfig.EXPLICIT_EPIC_CONFIDENCE

        # Infer from top matching tasks
        for task, score in task_matches[:3]:
            if task.get("epic"):
                epic_name = task["epic"]
                if epic_name not in candidate_epics:
                    candidate_epics[epic_name] = 0
                # Boost if multiple tasks point to same epic
                candidate_epics[epic_name] += score * TaskAnalyzerConfig.TASK_MATCH_EPIC_BOOST

        # Infer from keywords
        for keyword in keywords:
            for epic_name in self.epics:
                if keyword in epic_name.lower():
                    if epic_name not in candidate_epics:
                        candidate_epics[epic_name] = 0
                    candidate_epics[epic_name] += TaskAnalyzerConfig.KEYWORD_EPIC_BOOST

        # Return highest scoring epic
        if candidate_epics:
            best_epic = max(candidate_epics, key=candidate_epics.get)
            confidence = min(1.0, candidate_epics[best_epic])
            return (best_epic, confidence)

        return (None, 0)

    # ========================================================================
    # PHASE 6: Infer Priority
    # ========================================================================

    def _infer_priority(self, hints: Dict[str, bool], task_matches: List[Tuple[Dict, float]]) -> str:
        """
        Determine priority from hints and task context.
        [BLOCKER] → critical
        [URGENT] → high
        Default → medium
        """
        if hints.get("blocker"):
            return "critical"

        if hints.get("urgent"):
            return "high"

        # Check if matching other critical tasks
        for task, score in task_matches:
            if task.get("priority") == "critical" and score > TaskAnalyzerConfig.CRITICAL_TASK_PRIORITY_THRESHOLD:
                return "high"

        return "medium"

    # ========================================================================
    # PHASE 7: Detect Category
    # ========================================================================

    def _detect_category(self, _user_input: str, keywords: List[str]) -> str:
        """
        Detect task category: feature, bug, refactor, docs, chore, research
        Based on language patterns and keywords.
        """
        # Bug indicators
        if any(word in keywords for word in ["fix", "bug", "issue", "error", "broken", "crash", "failure"]):
            return "bug"

        # Feature indicators
        if any(word in keywords for word in ["add", "implement", "new", "support", "enable", "feature"]):
            return "feature"

        # Refactor indicators
        if any(word in keywords for word in ["refactor", "refine", "improve", "clean", "optimize", "reorganize"]):
            return "refactor"

        # Documentation indicators
        if any(word in keywords for word in ["docs", "document", "guide", "readme", "documentation"]):
            return "docs"

        # Research indicators
        if any(word in keywords for word in ["research", "evaluate", "analyze", "test", "explore", "investigate"]):
            return "research"

        # Default to chore for maintenance
        return "chore"

    # ========================================================================
    # PHASE 8: Infer Dependencies (Main Logic)
    # ========================================================================

    def _infer_dependencies(
        self,
        explicit_tasks: List[str],
        hints: Dict[str, bool],
        _keywords: List[str],
        task_matches: List[Tuple[Dict, float]],
        user_input: str,
    ) -> List[str]:
        """
        Infer which tasks must complete before this one.
        This is the most critical inference logic.

        Signals (in priority order):
        1. Explicit TASK-XXX references in temporal context
        2. Temporal hints (after X, then)
        3. Dependency phrases
        4. Semantic relationship with high-confidence matches
        """
        dependencies = []

        # Signal 1: Explicit task references in temporal context
        if hints.get("temporal") == "after":
            # Find TASK-XXX mentioned after "after"
            after_match = re.search(
                r"after\s+([A-Z0-9\-\,\s]+?)(?:\s+(?:we|then|next|complete|finish)|$)",
                user_input,
                re.I,
            )
            if after_match:
                referenced_text = after_match.group(1)
                explicit_in_context = self._extract_task_references(referenced_text)
                dependencies.extend(explicit_in_context)

        # Signal 2: Direct TASK-XXX references (always high confidence)
        dependencies.extend(explicit_tasks)

        # Signal 3: Dependency phrases
        if hints.get("depends_on_phrase"):
            # "depends on TASK-015" or "depends on template work"
            depends_match = re.search(r"depends\s+on\s+([^\.]*?)(?:\.|$)", user_input, re.I)
            if depends_match:
                dependency_text = depends_match.group(1)
                explicit_deps = self._extract_task_references(dependency_text)
                if explicit_deps:
                    dependencies.extend(explicit_deps)
                # Also match semantic references
                else:
                    for task, score in task_matches:
                        if score > TaskAnalyzerConfig.HIGH_CONFIDENCE_MATCH_THRESHOLD:
                            dependencies.append(task["id"])
                            break

        # Signal 4: Don't infer dependencies for blocking tasks
        # [BLOCKER] tasks typically don't depend on others
        if hints.get("blocker") or hints.get("urgent"):
            pass  # This likely unblocks work, not depends on it

        # Deduplicate
        dependencies = list(set(dependencies))

        # Only return dependencies that exist and aren't completed
        valid_deps = []
        for dep_id in dependencies:
            if self._task_exists(dep_id) and not self._task_completed(dep_id):
                valid_deps.append(dep_id)

        return sorted(valid_deps)

    def _task_exists(self, task_id: str) -> bool:
        """Check if task exists"""
        return task_id in self.task_by_id

    def _task_completed(self, task_id: str) -> bool:
        """Check if task is already completed"""
        task = self.task_by_id.get(task_id)
        return task and task.get("status") == "completed"

    # ========================================================================
    # PHASE 9: Calculate Confidence Scores
    # ========================================================================

    def _calculate_confidence(
        self,
        depends_on: List[str],
        epic: Optional[str],
        priority: str,
        category: str,
        hints: Dict[str, bool],
        explicit_tasks: List[str],
    ) -> Dict[str, float]:
        """
        Generate confidence scores for each inference.
        Higher = more certain.
        Used to indicate which inferences were explicit vs semantic.
        """
        confidence = {
            "epic": self._score_epic_confidence(epic, hints),
            "depends_on": self._score_depends_confidence(depends_on, hints, explicit_tasks),
            "priority": self._score_priority_confidence(priority, hints),
            "category": self._score_category_confidence(category, hints),
        }

        # Calculate overall confidence as average
        confidence["overall"] = sum(confidence.values()) / len(confidence)

        return confidence

    def _score_depends_confidence(
        self, depends_on: List[str], hints: Dict[str, bool], explicit_tasks: List[str]
    ) -> float:
        """
        Dependencies inferred from:
        - Explicit refs (0.95+)
        - Temporal hints like "after" (0.85-0.90)
        - Semantic matching (0.70-0.80)
        """
        if not depends_on:
            return TaskAnalyzerConfig.CONFIDENCE_NO_DEPENDENCIES

        if any(dep in explicit_tasks for dep in depends_on):
            return TaskAnalyzerConfig.CONFIDENCE_EXPLICIT_TASK_REF

        if hints.get("depends_on_phrase"):
            return TaskAnalyzerConfig.CONFIDENCE_EXPLICIT_PHRASE

        if hints.get("temporal"):
            return TaskAnalyzerConfig.CONFIDENCE_TEMPORAL_HINT

        return TaskAnalyzerConfig.CONFIDENCE_SEMANTIC_DEPENDENCY

    def _score_epic_confidence(self, epic: Optional[str], hints: Dict[str, bool]) -> float:
        if not epic:
            return TaskAnalyzerConfig.CONFIDENCE_EPIC_NOT_FOUND

        if hints.get("part_of_phrase"):
            return TaskAnalyzerConfig.EXPLICIT_EPIC_CONFIDENCE

        return TaskAnalyzerConfig.CONFIDENCE_EPIC_SEMANTIC

    def _score_priority_confidence(self, _priority: str, hints: Dict[str, bool]) -> float:
        if hints.get("blocker") or hints.get("urgent"):
            return TaskAnalyzerConfig.CONFIDENCE_EXPLICIT_PRIORITY

        return TaskAnalyzerConfig.CONFIDENCE_DEFAULT_PRIORITY

    def _score_category_confidence(self, _category: str, _hints: Dict[str, bool]) -> float:
        # Lower confidence for category - often inferred
        return TaskAnalyzerConfig.CONFIDENCE_CATEGORY

    # ========================================================================
    # PHASE 10: Generate Reasoning
    # ========================================================================

    def _generate_reasoning(
        self,
        user_input: str,
        explicit_tasks: List[str],
        hints: Dict[str, bool],
        task_matches: List[Tuple[Dict, float]],
        epic: Optional[str],
        depends_on: List[str],
        priority: str,
        category: str,
    ) -> List[str]:
        """
        Generate human-readable explanation of why inference was made.
        Helps user understand and debug the system.
        """
        reasons = []

        if depends_on:
            if explicit_tasks:
                reasons.append(f"Detected explicit task reference(s): {', '.join(depends_on)}")
            if hints.get("temporal"):
                reasons.append(f"Found temporal relationship: '{hints['temporal']}'")
            if hints.get("depends_on_phrase"):
                reasons.append("Found explicit 'depends on' phrase")
        else:
            reasons.append("No dependencies detected")

        if epic:
            explicit_epic = any(word in user_input.lower() for word in epic.lower().split())
            if explicit_epic:
                reasons.append(f"Matched epic from explicit mention: {epic}")
            else:
                reasons.append(f"Inferred epic from similar tasks: {epic}")
        else:
            reasons.append("Could not determine epic (will auto-assign)")

        if priority != "medium":
            if hints.get("blocker"):
                reasons.append(f"Priority elevated to '{priority}' due to [BLOCKER] marker")
            elif hints.get("urgent"):
                reasons.append(f"Priority set to '{priority}' due to [URGENT] marker")

        reasons.append(f"Category inferred as '{category}' from language patterns")

        if task_matches:
            top_match = task_matches[0]
            reasons.append(f"Related task: {top_match[0]['id']} ({top_match[0]['title'][:50]}...)")

        return reasons

    # ========================================================================
    # Helper Methods
    # ========================================================================

    def _infer_related(self, task_matches: List[Tuple[Dict, float]], depends_on: List[str]) -> List[str]:
        """Return contextually related tasks (not dependencies)"""
        related = [t["id"] for t, score in task_matches[:3] if score > 0.5]
        # Remove if already in depends_on
        related = [t for t in related if t not in depends_on]
        return related

    def _build_keyword_index(self, tasks: List[Dict]) -> Dict[str, List[str]]:
        """Pre-process: build keyword index for all tasks"""
        index = {}
        for task in tasks:
            title = task.get("title", "")
            description = task.get("description", "")
            keywords = self._extract_keywords(f"{title} {description}")
            index[task["id"]] = keywords
        return index


# ============================================================================
# CLI Interface
# ============================================================================


def load_tasks_from_file(tasks_file: Path) -> List[Dict]:
    """Load tasks from tasks.md file using shared markdown parser."""
    if not tasks_file.exists():
        raise FileNotFoundError(f"Tasks file not found: {tasks_file}")

    content = tasks_file.read_text()
    tasks = []

    # Parse markdown using shared parser (single source of truth)
    blocks = parse_task_blocks(content)

    for task_id, task_block in blocks:
        # Extract title from markdown header
        pattern = r"^##\s+\[TASK-\d{3}\]\s+(.+?)$"
        first_line = task_block.split("\n")[0] if task_block else ""
        title_match = re.match(pattern, first_line)
        title = title_match.group(1).strip() if title_match else task_id

        # Parse task fields using shared parser
        task_data = parse_task_full(task_id, task_block, include_optional=True)

        tasks.append(
            {
                "id": task_id,
                "title": title,
                "status": task_data["status"],
                "priority": task_data["priority"],
                "category": task_data.get("category", "chore"),
                "epic": task_data["epic"],
                "description": task_data.get("description", ""),
            }
        )

    return tasks


def main() -> None:
    """CLI interface for task analyzer"""
    if len(sys.argv) < 2:
        print("Usage: task_analyzer.py analyze <tasks-file> <user-input>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "analyze":
        if len(sys.argv) < 4:
            print("Usage: task_analyzer.py analyze <tasks-file> <user-input>")
            sys.exit(1)

        tasks_file = Path(sys.argv[2].replace("~", str(Path.home())))
        user_input = " ".join(sys.argv[3:])

        try:
            tasks = load_tasks_from_file(tasks_file)
            analyzer = TaskAnalyzer(tasks)
            result = analyzer.analyze(user_input)

            print(json.dumps(result, indent=2))
            sys.exit(0)

        except Exception as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)

    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
