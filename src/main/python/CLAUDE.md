# Python Directory — CLAUDE.md

YouTube transcript extraction and processing pipeline.

## Setup
```bash
cd src/main/python/yt-transcript
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Script Execution Order
1. `extract_transcripts.py` — raw extraction from YouTube
2. `extract_smart.py` — smart extraction with language detection
3. `cleanup_with_claude.py` — clean transcripts via Claude API
4. `cleanup_books.py` — update books catalog with cleaned transcripts
5. `extract_kannada_only.py` — filter Kannada-only content
6. `transliterate_devanagari.py` — convert Devanagari to Eke romanization

## Critical Notes
- DO NOT bypass proxy rotation or rate-limiting delays in scripts
- `youtube-transcript-api` requires internet access; expect YouTube rate limiting
- Outputs go to `src/main/md/kannada/transcripts/` (raw) and `transcripts_cleaned/` (processed)