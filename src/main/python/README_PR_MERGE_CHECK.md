# PR Merge Status Checker

A utility script to check if an open Pull Request's code has already been merged into the base branch.

## Purpose

Sometimes a PR remains open even though its changes have been incorporated into the codebase through other means:
- Changes were cherry-picked from the PR into another branch
- The same changes were implemented in a different PR that got merged
- Commits were rebased and merged under different SHAs

This script helps identify these situations by analyzing the commits in a PR branch and checking if equivalent changes exist in the base branch.

## Features

- **Commit Tracking**: Identifies all commits in the PR that aren't in the base branch
- **Patch Matching**: Detects when the same changes exist under different commit SHAs
- **Clear Output**: Provides both human-readable and JSON output formats
- **Exit Codes**: Returns 0 if fully merged, 1 if not (useful for CI/CD)

## Usage

### Basic Usage

```bash
# Check if a PR branch is merged into master
python3 src/main/python/check_pr_merge_status.py feature-branch master

# Check current branch against main
python3 src/main/python/check_pr_merge_status.py HEAD main

# Check a remote branch
python3 src/main/python/check_pr_merge_status.py origin/feature-branch origin/master
```

### JSON Output

```bash
# Get results in JSON format (useful for automation)
python3 src/main/python/check_pr_merge_status.py feature-branch master --json
```

### Example Output

```
============================================================
PR Merge Status Check
============================================================
PR Branch: copilot/feature-x
Base Branch: master

Result: ✓ MERGED

3/3 commits found in base branch.

Commit Details:
------------------------------------------------------------
✓ a1b2c3d4: Add new feature implementation
✓ e5f6g7h8: Update documentation
✓ i9j0k1l2: Fix edge case handling
============================================================
```

## How It Works

1. **Identify PR Commits**: Uses `git rev-list` to find commits in the PR branch that aren't in the base branch
2. **Check Each Commit**: For each commit, checks if:
   - The exact commit SHA exists in the base branch (via `git merge-base`)
   - An equivalent commit with the same patch exists (by comparing diffs)
3. **Report Status**: Summarizes which commits are merged and which are unique to the PR

## Requirements

- Python 3.6+
- Git 2.0+
- Must be run from within a git repository

## Exit Codes

- `0`: All PR commits are found in the base branch (fully merged)
- `1`: Some or all PR commits are not in the base branch (not merged)

## Limitations

- The patch matching algorithm may not catch all edge cases where changes are significantly refactored
- Performance may be slower for very large repositories or PRs with many commits
- Searches only the most recent 100 commits in the base branch for efficiency

## Use Cases

1. **PR Cleanup**: Identify PRs that can be closed because their changes are already merged
2. **CI/CD Integration**: Automatically check if a PR's changes are already in the release branch
3. **Release Management**: Verify which features from open PRs have made it into a release
4. **Code Review**: Understand if similar changes have already been implemented elsewhere
