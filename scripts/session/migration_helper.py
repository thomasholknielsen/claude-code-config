#!/usr/bin/env python3
"""
Migration Helper for Context Management Refactoring
Migrates legacy .agent/context/ files to new hierarchical session structure

Usage:
    python3 migration_helper.py [--dry-run] [--verbose]

Options:
    --dry-run    Show what would be migrated without making changes
    --verbose    Show detailed progress information
"""

import argparse
import sys


# Import session_manager functions
try:
    from session_manager import get_context_base_dir, migrate_legacy_contexts
except ImportError:
    # Handle relative import when run from scripts/session/ directory
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    from session_manager import get_context_base_dir, migrate_legacy_contexts


def print_banner():
    """Print migration banner"""
    print("=" * 60)
    print("Context Management Migration Helper")
    print("Migrates legacy .agent/context/ files to hierarchical structure")
    print("=" * 60)
    print()


def check_legacy_files(verbose=False):
    """
    Check for legacy context files that need migration.

    Args:
        verbose: Show detailed file listing

    Returns:
        tuple: (file_count, total_size_bytes)
    """
    legacy_dir = get_context_base_dir()

    if not legacy_dir.exists():
        return 0, 0

    # Find all markdown files in legacy directory
    legacy_files = [f for f in legacy_dir.glob("*.md") if f.is_file()]

    if verbose and legacy_files:
        print(f"Found {len(legacy_files)} legacy context files:")
        for f in sorted(legacy_files):
            size = f.stat().st_size
            print(f"  - {f.name} ({size} bytes)")
        print()

    total_size = sum(f.stat().st_size for f in legacy_files)

    return len(legacy_files), total_size


def run_migration(dry_run=False, verbose=False):
    """
    Execute migration of legacy context files.

    Args:
        dry_run: If True, show what would be migrated without making changes
        verbose: Show detailed progress

    Returns:
        int: Exit code (0 = success, 1 = error)
    """
    print_banner()

    # Check for legacy files
    print("Scanning for legacy context files...")
    file_count, total_size = check_legacy_files(verbose=verbose)

    if file_count == 0:
        print("✓ No legacy context files found. Migration not needed.")
        print()
        return 0

    print(f"Found {file_count} legacy context files ({total_size / 1024:.2f} KB total)")
    print()

    if dry_run:
        print("DRY RUN MODE - No files will be modified")
        print()
        print("Migration would:")
        print("  1. Parse each legacy filename for date, topic, session-id")
        print("  2. Create Session-{date}-{id}/ directory structure")
        print("  3. Create session.md metadata file")
        print("  4. Copy context file to new location")
        print("  5. Original files remain untouched (manual cleanup)")
        print()
        print("To execute migration, run without --dry-run flag")
        print()
        return 0

    # Confirm migration
    print("This migration will:")
    print("  • Create new Session-{YYYY-MM-DD}-{id}/ directories")
    print("  • Copy legacy files to new structure")
    print("  • Generate session.md metadata files")
    print("  • Original files will NOT be deleted (manual cleanup recommended)")
    print()

    response = input("Proceed with migration? (yes/no): ").strip().lower()

    if response not in ["yes", "y"]:
        print("Migration cancelled.")
        print()
        return 0

    print()
    print("Starting migration...")
    print()

    # Execute migration via session_manager.migrate_legacy_contexts()
    try:
        stats = migrate_legacy_contexts()

        print()
        print("Migration Results:")
        print(f"  ✓ Migrated: {stats['migrated']} files")
        print(f"  ⊘ Skipped:  {stats['skipped']} files (invalid format)")
        print(f"  ✗ Errors:   {stats['errors']} files (failed)")
        print()

        if stats["migrated"] > 0:
            print("✓ Migration completed successfully!")
            print()
            print("Next steps:")
            print("  1. Verify migrated files in .agent/Session-*/")
            print("  2. Review skipped/errored files if any")
            print("  3. Manually delete legacy files from .agent/context/ when satisfied")
            print()

        return 0 if stats["errors"] == 0 else 1

    except Exception as e:
        print(f"✗ Migration failed: {e}")
        print()
        return 1


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Migrate legacy context files to hierarchical session structure",
        epilog="Example: python3 migration_helper.py --dry-run --verbose",
    )

    parser.add_argument("--dry-run", action="store_true", help="Show what would be migrated without making changes")

    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed progress information")

    args = parser.parse_args()

    return run_migration(dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
