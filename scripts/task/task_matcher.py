#!/usr/bin/env python
"""Task semantic matching module.

Handles finding existing tasks that match keywords semantically.
Extracted from TaskAnalyzer to follow Single Responsibility Principle.
"""

from typing import Dict, List, Set, Tuple

from config import TaskAnalyzerConfig


class TaskMatcher:
    """Matches keywords against existing tasks semantically."""

    def __init__(self, tasks: List[Dict], keywords_by_task: Dict[str, List[str]]):
        """Initialize matcher with task list and pre-computed keywords.

        Args:
            tasks: List of task dictionaries
            keywords_by_task: Dict mapping task_id → extracted keywords
        """
        self.tasks = tasks
        self.keywords_by_task = keywords_by_task

    def find_matches(self, keywords: List[str]) -> List[Tuple[Dict, float]]:
        """Find tasks matching keywords semantically.

        Args:
            keywords: List of keywords to match

        Returns:
            List of (task, similarity_score) tuples, sorted by score descending
        """
        scores = []
        keywords_set = set(keywords)

        for task in self.tasks:
            if task.get("status") == "deleted":
                continue

            # Get task keywords
            task_keywords = self.keywords_by_task.get(task["id"], [])
            task_keywords_set = set(task_keywords)

            # Calculate Jaccard similarity
            similarity_score = self._calculate_similarity(keywords_set, task_keywords_set)

            # Boost for exact phrase matches
            if self._phrase_in_task(keywords, task):
                similarity_score = min(1.0, similarity_score * TaskAnalyzerConfig.SIMILARITY_BOOST_MULTIPLIER)

            if similarity_score > TaskAnalyzerConfig.SIMILARITY_THRESHOLD:
                scores.append((task, similarity_score))

        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[: TaskAnalyzerConfig.TOP_N_MATCHES]

    def _calculate_similarity(self, keywords_set: Set[str], task_keywords_set: Set[str]) -> float:
        """Calculate Jaccard similarity between two keyword sets.

        Args:
            keywords_set: Set of input keywords
            task_keywords_set: Set of task keywords

        Returns:
            Similarity score 0.0-1.0
        """
        matches = keywords_set & task_keywords_set
        union = keywords_set | task_keywords_set

        # Handle edge case: both sets empty
        if not union:
            return 0.0

        return len(matches) / len(union)

    def _phrase_in_task(self, keywords: List[str], task: Dict) -> bool:
        """Check if phrase appears verbatim in task.

        Args:
            keywords: List of keywords forming the phrase
            task: Task dictionary

        Returns:
            True if phrase found in title or description
        """
        phrase = " ".join(keywords).lower()
        title = task.get("title", "").lower()
        description = task.get("description", "").lower()
        return phrase in title or phrase in description
