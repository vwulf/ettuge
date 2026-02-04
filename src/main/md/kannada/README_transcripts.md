# YouTube Video Transcript Extraction

This directory contains scripts and transcripts for videos from the MALATIBHAT YouTube channel.

## ⚠️ Important Note

**The transcript extraction script requires internet access to YouTube to function.** You will need to run this script in your local environment or any environment with unrestricted internet access. The transcripts directory is currently empty and will be populated when you run the script.

## Files

- `malatibhat_dns_bhat_videos_links.txt` - Contains 349 YouTube video links from the MALATIBHAT channel
- `../../python/kannada/extract_transcripts.py` - Python script to extract transcripts from the videos
- `transcripts/` - Directory where extracted transcripts are saved

## Requirements

To run the transcript extraction script, you need:

1. Python 3.6 or higher
2. The `youtube-transcript-api` library

Install the required library:
```bash
pip install youtube-transcript-api
```

## Usage

### Running the Script

From the repository root:
```bash
python3 src/main/python/kannada/extract_transcripts.py
```

Or make it executable and run directly:
```bash
chmod +x src/main/python/kannada/extract_transcripts.py
./src/main/python/kannada/extract_transcripts.py
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

The extraction script is located at: `src/main/python/kannada/extract_transcripts.py`

It can be run from the repository root, and it's configured to:
- Read from: `src/main/md/kannada/malatibhat_dns_bhat_videos_links.txt`
- Save to: `src/main/md/kannada/transcripts/`

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
