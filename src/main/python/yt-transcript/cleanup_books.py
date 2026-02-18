#!/usr/bin/env python3
"""
Script to cleanup books in dnsbhat directory by replacing garbled content
with cleaned content from transcripts_cleaned directory.

This script:
1. Scans all book files in dnsbhat directories
2. Identifies video IDs embedded in each book
3. Checks if cleaned transcripts exist for those video IDs
4. Replaces garbled paragraph content with cleaned content
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set

# Paths
REPO_ROOT = Path(__file__).parent.parent.parent.parent.parent
KANNADA_MD = REPO_ROOT / "src" / "main" / "md" / "kannada"
DNSBHAT_DIR = KANNADA_MD / "dnsbhat"
TRANSCRIPTS_DIR = KANNADA_MD / "transcripts"
TRANSCRIPTS_CLEANED_DIR = KANNADA_MD / "transcripts_cleaned"


def extract_video_id_from_url(url: str) -> str:
    """Extract YouTube video ID from URL."""
    match = re.search(r'watch\?v=([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)
    return ""


def find_video_ids_in_book(book_path: Path) -> List[str]:
    """Find all YouTube video IDs referenced in a book file."""
    video_ids = []
    content = book_path.read_text(encoding='utf-8')
    
    # Find all YouTube URLs
    urls = re.findall(r'https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+', content)
    for url in urls:
        video_id = extract_video_id_from_url(url)
        if video_id and video_id not in video_ids:
            video_ids.append(video_id)
    
    return video_ids


def get_cleaned_video_ids() -> Set[str]:
    """Get set of video IDs that have cleaned transcripts available."""
    cleaned_ids = set()
    if TRANSCRIPTS_CLEANED_DIR.exists():
        for file in TRANSCRIPTS_CLEANED_DIR.glob("*.txt"):
            # Remove .txt extension to get video ID
            cleaned_ids.add(file.stem)
    return cleaned_ids


def read_transcript(video_id: str, use_cleaned: bool = False) -> str:
    """Read transcript content for a video ID."""
    transcript_dir = TRANSCRIPTS_CLEANED_DIR if use_cleaned else TRANSCRIPTS_DIR
    transcript_file = transcript_dir / f"{video_id}.txt"
    
    if not transcript_file.exists():
        return ""
    
    content = transcript_file.read_text(encoding='utf-8')
    
    # Extract just the transcript content (skip header lines)
    lines = content.split('\n')
    transcript_lines = []
    in_transcript = False
    
    for line in lines:
        if '=' * 20 in line and 'TRANSCRIPT' in content[:content.index(line) + len(line)]:
            in_transcript = True
            continue
        if in_transcript:
            transcript_lines.append(line)
    
    # If we didn't find the separator, try to extract after known headers
    if not transcript_lines:
        skip_count = 0
        for i, line in enumerate(lines):
            if line.startswith('Video Link:') or line.startswith('Video ID:'):
                skip_count = i
        if skip_count > 0:
            # Skip header lines and empty lines
            for line in lines[skip_count+1:]:
                if line.strip() and '=' not in line:
                    transcript_lines.append(line)
                elif transcript_lines:  # Already started collecting
                    transcript_lines.append(line)
    
    return '\n'.join(transcript_lines).strip()


def extract_transcript_from_book_section(content: str, start_idx: int) -> Tuple[str, int, int]:
    """
    Extract the transcript section from book content starting at given index.
    Returns (transcript_text, start_position, end_position)
    """
    # Find the TRANSCRIPT marker
    transcript_marker = content.find('TRANSCRIPT:', start_idx)
    if transcript_marker == -1:
        return "", -1, -1
    
    # Find the separator line
    sep_start = content.find('=', transcript_marker)
    if sep_start == -1:
        return "", -1, -1
    
    # Find end of separator line
    sep_end = content.find('\n', sep_start)
    if sep_end == -1:
        return "", -1, -1
    
    # Find the next section or end of file
    # Look for next "## Part" or "---" or end of file
    next_section = len(content)
    for marker in ['\n## Part', '\n---', '\n# ']:
        pos = content.find(marker, sep_end + 1)
        if pos != -1 and pos < next_section:
            next_section = pos
    
    transcript_text = content[sep_end + 1:next_section].strip()
    return transcript_text, sep_end + 1, next_section


def update_book_with_cleaned_transcripts(book_path: Path, dry_run: bool = False) -> Dict:
    """
    Update a book file by replacing garbled transcripts with cleaned ones.
    Returns dict with statistics about the update.
    """
    stats = {
        'book': book_path.name,
        'video_ids': [],
        'cleaned_available': [],
        'updated': False,
        'sections_replaced': 0
    }
    
    content = book_path.read_text(encoding='utf-8')
    video_ids = find_video_ids_in_book(book_path)
    cleaned_ids = get_cleaned_video_ids()
    
    stats['video_ids'] = video_ids
    stats['cleaned_available'] = [vid for vid in video_ids if vid in cleaned_ids]
    
    if not stats['cleaned_available']:
        return stats
    
    # For each video ID with cleaned transcript, replace the content
    new_content = content
    
    for video_id in stats['cleaned_available']:
        # Find the YouTube link for this video
        pattern = f'https://www\\.youtube\\.com/watch\\?v={video_id}'
        match = re.search(pattern, new_content)
        
        if not match:
            continue
        
        # Extract the current transcript section
        old_transcript, start_pos, end_pos = extract_transcript_from_book_section(
            new_content, match.start()
        )
        
        if start_pos == -1:
            continue
        
        # Read the cleaned transcript
        cleaned_transcript = read_transcript(video_id, use_cleaned=True)
        
        if not cleaned_transcript:
            continue
        
        # Replace the old transcript with cleaned one
        new_content = (
            new_content[:start_pos] + 
            cleaned_transcript + '\n\n' +
            new_content[end_pos:]
        )
        
        stats['sections_replaced'] += 1
        stats['updated'] = True
        
        print(f"  ✓ Replaced section for video {video_id}")
    
    # Write the updated content
    if stats['updated'] and not dry_run:
        book_path.write_text(new_content, encoding='utf-8')
    
    return stats


def main(dry_run=False):
    """Main function to process all books."""
    print("=" * 80)
    print("Cleaning up dnsbhat books with transcripts_cleaned content")
    if dry_run:
        print("(DRY RUN MODE - no files will be modified)")
    print("=" * 80)
    print()
    
    # Get all cleaned video IDs
    cleaned_ids = get_cleaned_video_ids()
    print(f"Found {len(cleaned_ids)} cleaned transcripts available")
    print()
    
    # Process each book
    all_stats = []
    
    for book_dir in sorted(DNSBHAT_DIR.glob("*")):
        if not book_dir.is_dir():
            continue
        
        # Find the book file
        book_files = list(book_dir.glob("*.md"))
        if not book_files:
            continue
        
        book_path = book_files[0]
        print(f"Processing: {book_path.relative_to(REPO_ROOT)}")
        
        stats = update_book_with_cleaned_transcripts(book_path, dry_run=dry_run)
        all_stats.append(stats)
        
        if stats['video_ids']:
            print(f"  Found {len(stats['video_ids'])} video ID(s) in book")
            print(f"  {len(stats['cleaned_available'])} cleaned transcript(s) available")
        
        if stats['updated']:
            print(f"  ✓ Updated {stats['sections_replaced']} section(s)")
        else:
            if stats['cleaned_available']:
                print(f"  ⚠ No sections replaced (might be already clean)")
            else:
                print(f"  - No cleaned transcripts available for this book")
        print()
    
    # Print summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_books = len(all_stats)
    updated_books = sum(1 for s in all_stats if s['updated'])
    total_sections = sum(s['sections_replaced'] for s in all_stats)
    
    print(f"Total books processed: {total_books}")
    print(f"Books updated: {updated_books}")
    print(f"Total sections replaced: {total_sections}")
    print()
    
    # Show details of updated books
    if updated_books > 0:
        print("Updated books:")
        for stats in all_stats:
            if stats['updated']:
                print(f"  - {stats['book']}: {stats['sections_replaced']} section(s) replaced")
                print(f"    Video IDs: {', '.join(stats['cleaned_available'])}")


if __name__ == "__main__":
    import sys
    
    # Check for --dry-run flag
    dry_run = "--dry-run" in sys.argv
    
    main(dry_run=dry_run)
