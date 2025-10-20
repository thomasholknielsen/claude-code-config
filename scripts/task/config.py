#!/usr/bin/env python3
"""Task analyzer configuration module.

Centralized location for algorithm parameters and thresholds.
Single source of truth for tuning algorithm behavior.
"""


class TaskAnalyzerConfig:
    """Configuration for algorithm thresholds and scoring."""

    # Similarity/Matching Parameters
    SIMILARITY_BOOST_MULTIPLIER = 1.3  # Boost for exact phrase matches
    SIMILARITY_THRESHOLD = 0.2  # Minimum similarity to include in results
    TOP_N_MATCHES = 5  # Number of top task matches to return

    # Epic Detection Parameters
    EXPLICIT_EPIC_CONFIDENCE = 0.95  # Confidence when epic explicitly mentioned
    TASK_MATCH_EPIC_BOOST = 0.6  # Multiplier for task match contribution to epic
    KEYWORD_EPIC_BOOST = 0.4  # Base boost for keyword match in epic name

    # Priority/Matching Thresholds
    CRITICAL_TASK_PRIORITY_THRESHOLD = 0.7  # Score threshold to infer high priority
    HIGH_CONFIDENCE_MATCH_THRESHOLD = 0.75  # Score for high confidence dependency match

    # Confidence Scoring (0.0-1.0 scale, higher = more confident)
    CONFIDENCE_NO_DEPENDENCIES = 1.0  # No dependencies inferred
    CONFIDENCE_EXPLICIT_TASK_REF = 0.95  # Explicit TASK-XXX reference
    CONFIDENCE_EXPLICIT_PHRASE = 0.95  # Explicit "depends on" phrase
    CONFIDENCE_TEMPORAL_HINT = 0.90  # Temporal hint like "after"
    CONFIDENCE_SEMANTIC_DEPENDENCY = 0.75  # Semantic inference
    CONFIDENCE_EPIC_NOT_FOUND = 0.5  # Could not determine epic
    CONFIDENCE_EPIC_SEMANTIC = 0.80  # Epic inferred semantically
    CONFIDENCE_EXPLICIT_PRIORITY = 0.99  # Explicit priority marker ([BLOCKER])
    CONFIDENCE_DEFAULT_PRIORITY = 0.60  # Priority inferred or default
    CONFIDENCE_CATEGORY = 0.65  # Category confidence (often inferred)
