# Git-Flow vs Conventional Commits Guide

This guide helps you choose between Git-Flow and Conventional Commits workflows for your project.

## Quick Decision Matrix

| Factor | Conventional Commits | Git-Flow |
|--------|---------------------|----------|
| **Team Size** | 1-5 developers | 5+ developers |
| **Release Frequency** | Continuous deployment | Scheduled releases |
| **Branch Strategy** | Single main branch | main + develop branches |
| **Version Management** | Optional | Required (semantic versioning) |
| **Production Hotfixes** | Same as features | Dedicated hotfix workflow |
| **Complexity** | Low | Medium |
| **Best For** | Feature-focused development | Production systems |

## When to Use Conventional Commits (Default)

### Characteristics

- Small teams (1-5 developers)
- Continuous deployment or frequent releases
- Single production branch (main/master)
- Feature-focused development
- Quick iteration cycles
- No formal version management needed

### Branch Model

```text
main ← feat/* / fix/* / docs/* / test/* / chore/*
```

All branches target `main` directly. After PR merge, branch is deleted.

### Workflow

```bash
# Create feature branch
/git:branch feat/user-authentication

# Make changes and commit
/git:commit

# Push and create PR to main
/git:push
/git:pr
```

### Advantages

- ✅ Simple mental model
- ✅ Fast workflow
- ✅ Minimal overhead
- ✅ Easy to understand for new developers
- ✅ Works great for single-environment deployments

### Disadvantages

- ❌ No dedicated develop integration branch
- ❌ No formal release process
- ❌ Harder to manage multiple versions in production
- ❌ Emergency hotfixes use same workflow as features

### Good For

- MVPs and prototypes
- Internal tools
- Single-tenant applications
- Projects with automated testing and deployment
- Teams that deploy multiple times per day

## When to Use Git-Flow

### Characteristics

- Medium to large teams (5+ developers)
- Scheduled release cycles (weekly, monthly, quarterly)
- Multiple environments (production, staging, development)
- Versioned releases (v1.2.0, v2.0.0)
- Need emergency hotfix capability
- Formal QA/testing before production

### Branch Model

```text
main (production)
  ↖ hotfix/* (emergency fixes)
  ↖ release/* (release preparation)
      ↖ develop (integration)
          ↖ feature/* (new features)
```

Hierarchy ensures production stability while allowing parallel development.

### Workflow

```bash
# Feature development
/git-flow:feature user-authentication  # Creates feature branch from develop

# Make changes and commit
/git:commit

# Push and create PR to develop
/git:push
/git:pr  # Auto-targets develop in git-flow mode

# When ready for release
/git-flow:release 1.2.0  # Creates release branch, updates versions, generates changelog

# After release PR merged to main
/git-flow:finish  # Tags, merges to develop, cleanup

# Emergency production fix
/git-flow:hotfix critical-bug  # Branches from main
# Make fix, commit, push, create PR
/git-flow:finish  # Tags, merges to develop
```

### Advantages

- ✅ Clear separation: production (main) vs development (develop)
- ✅ Formal release process with version management
- ✅ Emergency hotfix workflow (bypasses develop)
- ✅ Multiple features in parallel without affecting production
- ✅ Changelog generation from commits
- ✅ Semantic versioning with git tags

### Disadvantages

- ❌ More complex workflow
- ❌ Requires understanding of branch hierarchy
- ❌ Additional merge overhead (dual merging)
- ❌ Longer time from feature to production

### Good For

- SaaS applications with scheduled releases
- Products with multiple versions in production
- Teams with dedicated QA cycles
- Applications requiring formal change management
- Projects with strict version compliance
- Mobile apps with app store submission cycles

## Repository Structure Comparison

### Conventional Commits

```text
my-project/
  main branch (production)
  ├── feat/new-feature (PR → main)
  ├── fix/bug-fix (PR → main)
  └── docs/update-readme (PR → main)
```

### Git-Flow

```text
my-project/
  main branch (production, tagged releases)
  develop branch (integration)
  ├── feature/new-feature (PR → develop)
  ├── feature/another-feature (PR → develop)
  ├── release/v1.2.0 (PR → main, then merge back to develop)
  └── hotfix/critical-bug (PR → main, then merge back to develop)
```

## Command Comparison

### Conventional Commits Commands

```bash
/git:branch feat/feature-name           # Create feature branch from HEAD
/git:commit                             # Commit with conventional format
/git:push                               # Push to remote
/git:pr                                 # Create PR to main
/workflows:git                          # Complete workflow: branch → commit → push → PR
```

### Git-Flow Commands

```bash
/git-flow:feature feature-name          # Create feature from develop
/git:commit                             # Commit with conventional format
/git:push                               # Push to remote
/git:pr                                 # Create PR to develop (auto-detected)
/git-flow:release 1.2.0                 # Create release branch, update versions, generate changelog
/git-flow:hotfix critical-bug           # Create hotfix from main
/git-flow:finish                        # Complete current branch: tag, merge to develop, cleanup
/workflows:git                          # Complete workflow (git-flow aware)
```

## Switching Between Workflows

### From Conventional to Git-Flow

1. **Create develop branch** from main:

   ```bash
   git checkout main
   git checkout -b develop
   git push -u origin develop
   ```

2. **Commands auto-detect git-flow mode** when both main and develop exist

3. **Start using git-flow commands**:

   ```bash
   /git-flow:feature new-feature    # Creates feature branch from develop
   /git:pr                          # Now targets develop
   ```

### From Git-Flow to Conventional

1. **Complete all open releases/hotfixes**

2. **Merge develop to main**:

   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```

3. **Delete develop branch**:

   ```bash
   git branch -d develop
   git push origin --delete develop
   ```

4. **Commands revert to conventional mode** when develop doesn't exist

## Auto-Detection

Commands automatically detect your workflow mode:

```bash
# Repository detection
if (main branch exists AND develop branch exists):
  MODE = "git-flow"
  - feature/* branches from develop
  - feature/* PRs target develop
  - release/* and hotfix/* workflows available
else:
  MODE = "conventional"
  - feat/fix/docs/* branches from HEAD
  - All PRs target main
  - No release/hotfix workflows
```

**You don't need to tell commands which mode to use - they detect it automatically!**

## Hybrid Approach (Advanced)

Some teams use a hybrid approach:

### Option 1: Git-Flow Lite

- Use main + develop branches (git-flow structure)
- Skip formal release branches (just merge develop → main)
- Use hotfix/* for emergencies only

```bash
# Regular features
/git-flow:feature name
# PR to develop

# When ready to release
git checkout main
git merge develop
git tag v1.2.0
```

### Option 2: Conventional + Versioning

- Use conventional commits (single main branch)
- Add git tags for releases manually
- Use conventional PR process

```bash
# Regular development
/git:branch feat/name
# PR to main

# Tag releases manually
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
```

## Migration Examples

### Example 1: Startup → Enterprise

**Scenario**: Started with conventional commits, now need formal releases.

**Before** (Conventional):

```text
main
├── feat/feature-a (merged)
├── feat/feature-b (merged)
└── fix/bug-fix (merged)
```

**After** (Git-Flow):

```text
main (v1.0.0 tagged)
develop (created from main)
├── feature/feature-c (in progress)
└── feature/feature-d (in progress)
```

**Migration Steps**:

1. Tag current main as v1.0.0
2. Create develop from main
3. Start using feature/ branches
4. First release: `/git-flow:release 1.1.0`

### Example 2: Enterprise → Continuous Deployment

**Scenario**: Moving to continuous deployment, don't need formal releases.

**Before** (Git-Flow):

```text
main (production)
develop
├── feature/a
└── feature/b
```

**After** (Conventional):

```text
main (production + development)
├── feat/feature-c
└── feat/feature-d
```

**Migration Steps**:

1. Complete all open releases
2. Merge develop → main
3. Delete develop
4. Use feat/ instead of feature/

## FAQ

### Q: Can I use both workflows in the same repository

**A**: Not simultaneously. Commands detect either git-flow mode (main + develop) or conventional mode (main only). Choose one workflow for consistency.

### Q: What if I only want releases, not the full git-flow

**A**: Use conventional commits for development, add git tags manually for releases:

```bash
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
```

### Q: Can I use conventional commit messages with git-flow

**A**: Yes! Git-flow is about branch strategy. Conventional commits are about message format. `/git:commit` works in both modes and always uses conventional format.

### Q: How do I know which mode my repository is in

**A**: Run `/git-flow:status` to check the current mode and status:

```bash
/git-flow:status
# Output: ✓ Git-Flow mode detected
#         ✓ Current branch: feature/test (from develop)
```

### Q: What about trunk-based development

**A**: Trunk-based development is similar to conventional commits with even shorter-lived branches. Use conventional commits and merge to main frequently (multiple times per day).

## Recommendations by Project Type

### Web Applications (SaaS)

- **Pre-MVP**: Conventional Commits
- **Post-MVP, < 5 devs**: Conventional Commits
- **Post-MVP, 5+ devs**: Git-Flow
- **High traffic, formal releases**: Git-Flow

### Mobile Applications

- **All stages**: Git-Flow
- **Reason**: App store submission requires version management

### Libraries/Packages

- **All stages**: Git-Flow
- **Reason**: Semantic versioning required for package managers

### Internal Tools

- **All stages**: Conventional Commits
- **Reason**: Simpler workflow, continuous deployment

### Open Source Projects

- **Small contributors**: Conventional Commits
- **Large contributors**: Git-Flow
- **Many releases**: Git-Flow

## Next Steps

### Starting with Conventional Commits

1. Read: [Typical Workflows](typical-workflows.md)
2. Try: `/workflows:git` for complete workflow
3. Practice: Create feature, commit, PR

### Starting with Git-Flow

1. Read: [Git-Flow Workflows](git-flow-workflows.md)
2. Initialize: Create develop branch
3. Try: `/git-flow:feature test`
4. Practice: Complete feature → release → hotfix cycle

### Need Help

```bash
/guru git-flow  # Get personalized git-flow guidance
/guru git       # Get general git workflow help
```

## Resources

- **Commands**: See [Command Decision Guide](../command-decision-guide.md)
- **Workflows**: See [Git-Flow Workflows](git-flow-workflows.md)
- **Conventional Commits**: <https://www.conventionalcommits.org>
- **Git-Flow**: <https://nvie.com/posts/a-successful-git-branching-model/>
- **Semantic Versioning**: <https://semver.org>
