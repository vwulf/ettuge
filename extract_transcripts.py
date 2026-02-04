#!/usr/bin/env python3
"""
Script to extract transcripts from YouTube videos listed in malatibhat_dns_bhat_videos_links.txt
and save them as text files with the original link.
"""

import re
import os
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    # Pattern for standard YouTube URLs
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/v\/([a-zA-Z0-9_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_id):
    """
    Get transcript for a video ID.
    Returns transcript text or None if unavailable.
    """
    try:
        # Create API instance
        api = YouTubeTranscriptApi()
        
        # Try to get transcript in any available language
        # Try Kannada (kn) first, then English (en), then Hindi (hi), then any available
        transcript_list = api.list(video_id)
        
        # Try to get manually created transcript first
        try:
            transcript = transcript_list.find_manually_created_transcript(['kn', 'en', 'hi'])
            transcript_data = transcript.fetch()
        except:
            # If no manual transcript, get any generated transcript
            try:
                transcript = transcript_list.find_generated_transcript(['kn', 'en', 'hi'])
                transcript_data = transcript.fetch()
            except:
                # Get any available transcript
                transcript = next(iter(transcript_list))
                transcript_data = transcript.fetch()
        
        # Combine all transcript segments into one text
        full_text = ' '.join([entry['text'] for entry in transcript_data])
        return full_text
        
    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video"
    except NoTranscriptFound:
        return None, "No transcript found"
    except VideoUnavailable:
        return None, "Video is unavailable"
    except Exception as e:
        return None, f"Error: {str(e)}"


def main():
    # Input file path
    input_file = Path('/home/runner/work/ettuge/ettuge/src/main/md/kannada/malatibhat_dns_bhat_videos_links.txt')
    
    # Output directory for transcripts
    output_dir = Path('/home/runner/work/ettuge/ettuge/src/main/md/kannada/transcripts')
    output_dir.mkdir(exist_ok=True)
    
    # Read video links
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Process each video link
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    print(f"Processing {len(lines)} links...")
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Skip channel link (first link)
        if '@MALATIBHAT' in line:
            print(f"{i}. Skipping channel link: {line}")
            skipped_count += 1
            continue
        
        # Extract video ID
        video_id = extract_video_id(line)
        
        if not video_id:
            print(f"{i}. Could not extract video ID from: {line}")
            error_count += 1
            continue
        
        # Check if transcript already exists
        output_file = output_dir / f"{video_id}.txt"
        if output_file.exists():
            print(f"{i}. Transcript already exists for {video_id}, skipping...")
            success_count += 1
            continue
        
        print(f"{i}. Processing video {video_id}...")
        
        # Get transcript
        result = get_transcript(video_id)
        
        if isinstance(result, tuple):
            transcript, error_msg = result
            if transcript is None:
                print(f"   ERROR: {error_msg}")
                error_count += 1
                # Save error info
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"Video Link: {line}\n")
                    f.write(f"Video ID: {video_id}\n")
                    f.write(f"\nERROR: {error_msg}\n")
                continue
        else:
            transcript = result
        
        # Save transcript with original link
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Video Link: {line}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"\n{'='*80}\n")
                f.write(f"TRANSCRIPT:\n")
                f.write(f"{'='*80}\n\n")
                f.write(transcript)
            
            print(f"   SUCCESS: Saved transcript ({len(transcript)} characters)")
            success_count += 1
            
        except Exception as e:
            print(f"   ERROR saving transcript: {str(e)}")
            error_count += 1
    
    print("\n" + "="*80)
    print(f"SUMMARY:")
    print(f"  Total processed: {len(lines)}")
    print(f"  Successful: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Transcripts saved to: {output_dir}")
    print("="*80)


if __name__ == '__main__':
    main()
