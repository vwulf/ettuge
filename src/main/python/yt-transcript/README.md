# YouTube Video Transcript Extraction and Book Cleanup

This directory contains scripts and configuration for:
1. Extracting transcripts from videos in the MALATIBHAT YouTube channel
2. Cleaning up and correcting transcripts using AI
3. Updating book files with cleaned transcripts

## ⚠️ Important Note

**The transcript extraction script requires internet access to YouTube to function.** You will need to run this script in your local environment or any environment with unrestricted internet access. The transcripts directory is currently empty and will be populated when you run the script.

## Files

- `extract_transcripts.py` - Python script to extract transcripts from the videos
- `extract_smart.py` - Smart extraction with language detection and transliteration
- `cleanup_with_claude.py` - AI-based transcript cleaning using Claude API
- `cleanup_books.py` - Script to update book files with cleaned transcripts
- `transliterate_devanagari.py` - Transliteration utilities for Devanagari to Kannada
- `extract_kannada_only.py` - Extract only Kannada language transcripts
- `requirements.txt` - Python dependencies (youtube-transcript-api)
- `README.md` - This file
- Video links are in: `../../md/kannada/malatibhat_dns_bhat_videos_links.txt`
- Transcripts are saved to: `../../md/kannada/transcripts/`
- Cleaned transcripts are in: `../../md/kannada/transcripts_cleaned/`
- Book files are in: `../../md/kannada/dnsbhat/`

## Requirements

To run the transcript extraction script, you need:

1. Python 3.6 or higher
2. The `youtube-transcript-api` library

Install the required library:
```bash
pip install -r requirements.txt
```

Or from the repository root:
```bash
pip install -r src/main/python/yt-transcript/requirements.txt
```

## Usage

### Running the Script

From the repository root:
```bash
python3 src/main/python/yt-transcript/extract_transcripts.py
```

Or make it executable and run directly:
```bash
chmod +x src/main/python/yt-transcript/extract_transcripts.py
./src/main/python/yt-transcript/extract_transcripts.py
```

### Script Features

The script will:
1. Read all video links from `malatibhat_dns_bhat_videos_links.txt`
2. Extract the video ID from each URL
3. Attempt to download the transcript in the following order of preference:
   - Manually created transcripts in Kannada (kn), English (en), or Hindi (hi)
   - Auto-generated transcripts in Kannada, English, or Hindi
   - Any other available transcript
4. Save each transcript as a text file named `{video_id}.txt` in the `transcripts/` directory
5. Include the original video link and video ID at the top of each transcript file
6. Skip videos that already have transcripts downloaded (allows resuming)
7. Handle errors gracefully and create error log files for videos without transcripts

### Output Format

Each transcript file will contain:
```
Video Link: https://www.youtube.com/watch?v={video_id}
Video ID: {video_id}

================================================================================
TRANSCRIPT:
================================================================================

[Full transcript text here...]
```

### Error Handling

For videos without available transcripts, the script will create a file containing:
```
Video Link: https://www.youtube.com/watch?v={video_id}
Video ID: {video_id}

ERROR: [Error message explaining why transcript is unavailable]
```

Common error messages:
- "Transcripts are disabled for this video" - The video owner has disabled transcripts
- "No transcript found" - No transcript is available for this video
- "Video is unavailable" - The video cannot be accessed (may be private or deleted)

## Script Location

The scripts are located at: `src/main/python/yt-transcript/`

Configuration paths:
- Read from: `src/main/md/kannada/malatibhat_dns_bhat_videos_links.txt`
- Raw transcripts: `src/main/md/kannada/transcripts/`
- Cleaned transcripts: `src/main/md/kannada/transcripts_cleaned/`
- Book files: `src/main/md/kannada/dnsbhat/`

## cleanup_books.py - Update Books with Cleaned Transcripts

This script updates book files in the `dnsbhat` directory by replacing garbled transcript sections with cleaned versions from `transcripts_cleaned/`.

### What It Does

The script:
1. Scans all book markdown files in the `dnsbhat/` directory
2. Identifies YouTube video IDs referenced in each book
3. Checks if cleaned transcripts exist for those video IDs
4. Replaces garbled transcript content with cleaned versions
5. Provides detailed reporting of changes made

### Why It's Needed

Some transcripts were auto-transcribed by YouTube in non-Kannada languages (Hindi, Arabic, English) and then transliterated to Kannada script. This resulted in garbled text that doesn't make sense. The `transcripts_cleaned/` directory contains AI-corrected versions that have been processed by Claude to reconstruct proper Kannada text.

### Usage

Run the script from the repository root:

```bash
# Update all books with cleaned transcripts
python3 src/main/python/yt-transcript/cleanup_books.py

# Dry-run mode (preview changes without modifying files)
python3 src/main/python/yt-transcript/cleanup_books.py --dry-run
```

### Output

The script provides:
- Progress updates for each book processed
- Count of video IDs found vs. cleaned transcripts available
- Number of sections replaced per book
- Summary statistics at the end

Example output:
```
Processing: src/main/md/kannada/dnsbhat/05-mathina-olaguttu/05-mathina-olaguttu.md
  Found 40 video ID(s) in book
  30 cleaned transcript(s) available
  ✓ Updated 30 section(s)

SUMMARY
Total books processed: 13
Books updated: 10
Total sections replaced: 128
```

### Results

As of the last run:
- 10 out of 13 books were updated
- 128 transcript sections were replaced with cleaned content
- Books without cleaned transcripts available remain unchanged



## Notes

- The script processes approximately 349 videos
- Processing time depends on your internet connection speed
- The script will automatically create the `transcripts/` directory if it doesn't exist
- Transcripts are saved in UTF-8 encoding to properly handle Kannada text
- The script can be stopped and resumed - it will skip videos that already have transcript files

## Troubleshooting

### No Internet Connection
If you encounter network errors, ensure you have an active internet connection and can access YouTube.

### Rate Limiting
If you encounter rate limiting errors from YouTube, try:
- Adding delays between requests
- Running the script in smaller batches
- Using a proxy if available

### Missing Transcripts
Not all videos have transcripts available. This is normal and the script will log these as errors but continue processing other videos.
