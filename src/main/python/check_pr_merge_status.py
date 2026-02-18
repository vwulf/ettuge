#!/usr/bin/env python3
"""
Check if an open PR's code has already been merged into the base branch.

This script helps identify situations where:
- A PR is still open but its changes have been merged via another PR
- Commits from an open PR have been cherry-picked to the base branch
- The changes already exist in the base branch
"""

import sys
import argparse
import subprocess
import json
from typing import Dict, List, Set, Optional


def run_git_command(args: List[str]) -> str:
    """Run a git command and return its output."""
    try:
        result = subprocess.run(
            ['git'] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}", file=sys.stderr)
        print(f"stderr: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def get_pr_commits(pr_branch: str, base_branch: str) -> List[str]:
    """Get the list of commit SHAs in the PR branch that aren't in base."""
    commits = run_git_command([
        'rev-list',
        f'{base_branch}..{pr_branch}'
    ])
    return commits.split('\n') if commits else []


def get_commit_patch(commit_sha: str) -> str:
    """Get the patch (diff) for a specific commit."""
    return run_git_command(['show', '--format=', commit_sha])


def get_commit_subject(commit_sha: str) -> str:
    """Get the subject line of a commit."""
    return run_git_command(['log', '--format=%s', '-n', '1', commit_sha])


def find_commit_in_base(commit_sha: str, base_branch: str) -> Optional[str]:
    """
    Check if a commit exists in the base branch.
    Returns the SHA if found, None otherwise.
    """
    # First, try to find the exact commit in the base branch
    # Check if base_branch is an ancestor of commit (meaning commit is reachable from base)
    result = subprocess.run(
        ['git', 'merge-base', '--is-ancestor', base_branch, commit_sha],
        capture_output=True
    )
    # If base is ancestor of commit, then commit is ahead of base (not in base)
    # We need the opposite: check if commit is in base's history
    result2 = subprocess.run(
        ['git', 'merge-base', '--is-ancestor', commit_sha, base_branch],
        capture_output=True
    )
    if result2.returncode == 0:
        return commit_sha
    
    # If not found directly, look for the same patch in base branch
    pr_patch = get_commit_patch(commit_sha)
    pr_subject = get_commit_subject(commit_sha)
    
    # Get commits reachable from base branch only
    base_commits = run_git_command([
        'rev-list',
        base_branch,
        '-100'  # Limit to recent 100 commits for performance
    ])
    
    if not base_commits:
        return None
    
    # Check each base commit for matching patch
    for base_commit in base_commits.split('\n'):
        if not base_commit or base_commit == commit_sha:
            continue
        
        base_patch = get_commit_patch(base_commit)
        base_subject = get_commit_subject(base_commit)
        
        # Match by patch content (only if patch is non-empty)
        if pr_patch and base_patch and pr_patch == base_patch:
            return base_commit
        elif pr_subject == base_subject and pr_patch and len(pr_patch) > 100:
            # If subjects match and patches are similar (and non-trivial), consider it a match
            # This handles cases where patches might differ slightly due to context
            pr_lines = set(pr_patch.split('\n'))
            base_lines = set(base_patch.split('\n'))
            if pr_lines and len(pr_lines & base_lines) / len(pr_lines) > 0.9:
                return base_commit
    
    return None


def check_pr_merge_status(pr_branch: str, base_branch: str) -> Dict:
    """
    Check if the code from a PR branch has been merged into the base branch.
    
    Returns a dictionary with:
    - merged: bool - whether all commits are found in base
    - total_commits: int - total commits in PR
    - merged_commits: int - commits found in base
    - unmerged_commits: list - commits not found in base
    - details: list - detailed info about each commit
    """
    # Ensure we have the latest from both branches
    print(f"Analyzing PR branch '{pr_branch}' against base '{base_branch}'...")
    
    pr_commits = get_pr_commits(pr_branch, base_branch)
    
    if not pr_commits:
        return {
            'merged': True,
            'total_commits': 0,
            'merged_commits': 0,
            'unmerged_commits': [],
            'details': [],
            'message': 'No commits found in PR branch that are not in base branch.'
        }
    
    total_commits = len(pr_commits)
    merged_commits = 0
    unmerged_commits = []
    details = []
    
    print(f"Found {total_commits} commit(s) in PR branch...")
    
    for commit in pr_commits:
        subject = get_commit_subject(commit)
        found_in_base = find_commit_in_base(commit, base_branch)
        
        if found_in_base:
            merged_commits += 1
            details.append({
                'sha': commit[:8],
                'subject': subject,
                'status': 'merged',
                'found_as': found_in_base[:8] if found_in_base != commit else 'same'
            })
        else:
            unmerged_commits.append(commit)
            details.append({
                'sha': commit[:8],
                'subject': subject,
                'status': 'not_merged'
            })
    
    all_merged = merged_commits == total_commits
    
    return {
        'merged': all_merged,
        'total_commits': total_commits,
        'merged_commits': merged_commits,
        'unmerged_commits': unmerged_commits,
        'details': details,
        'message': f"{merged_commits}/{total_commits} commits found in base branch."
    }


def main():
    parser = argparse.ArgumentParser(
        description='Check if an open PR\'s code has been merged into the base branch.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check if PR branch 'feature-x' is merged into 'main'
  %(prog)s feature-x main
  
  # Check current branch against master
  %(prog)s HEAD master
  
  # Output in JSON format
  %(prog)s feature-x main --json
        """
    )
    
    parser.add_argument(
        'pr_branch',
        help='The PR branch to check (e.g., "feature-branch" or "origin/feature-branch")'
    )
    
    parser.add_argument(
        'base_branch',
        help='The base branch to check against (e.g., "main" or "master")',
        default='master',
        nargs='?'
    )
    
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results in JSON format'
    )
    
    args = parser.parse_args()
    
    # Check if we're in a git repository
    result = subprocess.run(['git', 'rev-parse', '--git-dir'], capture_output=True)
    if result.returncode != 0:
        print("Error: Not in a git repository", file=sys.stderr)
        sys.exit(1)
    
    # Perform the check
    result = check_pr_merge_status(args.pr_branch, args.base_branch)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        # Human-readable output
        print("\n" + "="*60)
        print(f"PR Merge Status Check")
        print("="*60)
        print(f"PR Branch: {args.pr_branch}")
        print(f"Base Branch: {args.base_branch}")
        print(f"\nResult: {'✓ MERGED' if result['merged'] else '✗ NOT MERGED'}")
        print(f"\n{result['message']}")
        
        if result['details']:
            print(f"\nCommit Details:")
            print("-"*60)
            for detail in result['details']:
                status_icon = "✓" if detail['status'] == 'merged' else "✗"
                print(f"{status_icon} {detail['sha']}: {detail['subject']}")
                if detail['status'] == 'merged' and detail.get('found_as') != 'same':
                    print(f"  (found as {detail['found_as']})")
        
        print("="*60)
        
        # Exit with appropriate code
        sys.exit(0 if result['merged'] else 1)


if __name__ == '__main__':
    main()
