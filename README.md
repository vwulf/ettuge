For general shared examples:
[ettuge](https://github.com/vwulf/ettuge/)

Readable docs are in:
[mds](https://github.com/vwulf/ettuge/blob/master/src/main/md)

## Translation Task Status

📊 **Current Status**: Translation work in progress - see [TRANSLATION_SUMMARY.md](TRANSLATION_SUMMARY.md) for quick overview or [TRANSLATION_STATUS.md](TRANSLATION_STATUS.md) for detailed report.

- **PR #6**: Kannada translation of Eke.md created
- **Issue #7**: Revision needed to use DNS Bhat's word formation system
- **Next Steps**: Revise translation to follow native Kannada methodology

## PR Merge Status Checker

Check if an open Pull Request's code has already been merged into the base branch. Useful for identifying PRs that can be closed because their changes were incorporated through other means (cherry-picking, rebasing, etc.).

**Quick Start:**
```bash
# Check if a PR branch is merged into master
python3 src/main/python/check_pr_merge_status.py <pr-branch> master

# Example: Check current PR
python3 src/main/python/check_pr_merge_status.py copilot/check-open-pr-status master
```

See [README_PR_MERGE_CHECK.md](src/main/python/README_PR_MERGE_CHECK.md) for detailed documentation.

## YouTube Transcript Extraction

This repository includes a script to extract transcripts from YouTube videos. See [extract_transcripts.py](src/main/python/yt-transcript/extract_transcripts.py) and the [README](src/main/python/yt-transcript/README.md) for details.

**Quick Start:**
```bash
pip install -r src/main/python/yt-transcript/requirements.txt
python3 src/main/python/yt-transcript/extract_transcripts.py
```

Some interesting ones:
1. [Eke](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md)
1. [Reading types in haskell](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/reflection.md)
1. [Morphisms, diamonds and kannaDa](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/%E0%B2%95%E0%B2%B3%E0%B3%8D%E0%B2%B3.md)
1. [Monoids are everywhere](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/monoids-and-semigroups.md)
1. [A lazy take on (un)fold](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/qsortof.md)
1. [rangapura vihAra](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/hsom.md)
1. [Kojo](https://github.com/vwulf/ettuge/blob/master/src/main/md/kojo/cloud_flowers_and.md)
1. [ॐλ](https://github.com/vwulf/ettuge/blob/master/src/main/md/pl/%E0%A5%90%CE%BB.md)
1. [Forays into FP](src/main/md/pl/FP.md)
