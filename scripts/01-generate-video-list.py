#!/usr/bin/env python3
"""
Script to generate a CSV file with all videos from brazil_farm1/good/, 
brazil_farm2/good/, and ubc_farm_2022_compressed buckets with their accessible URLs.

Usage:
    python scripts/01-generate-video-list.py [--output-dir OUTPUT_DIR] [--filename FILENAME]

Examples:
    python scripts/01-generate-video-list.py
    python scripts/01-generate-video-list.py --output-dir ./data --filename arbutus_videos.csv
    python scripts/01-generate-video-list.py --output-dir /path/to/output
"""

import argparse
import csv
import os
import subprocess
from pathlib import Path
from typing import List, Tuple

def get_s3_files(bucket_path: str) -> List[Tuple[str, str, int]]:
    """
    Get list of files from S3 bucket using s3cmd.
    Returns list of tuples: (filename, full_s3_path, size)
    """
    try:
        result = subprocess.run(['s3cmd', 'ls', '-r', bucket_path], 
                              capture_output=True, text=True, check=True)
        files = []
        
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                # Parse s3cmd output: date time size s3://bucket/path/filename
                parts = line.split()
                if len(parts) >= 4 and parts[3].startswith('s3://'):
                    size = int(parts[2])
                    s3_path = parts[3]
                    filename = s3_path.split('/')[-1]
                    files.append((filename, s3_path, size))
        
        return files
    except subprocess.CalledProcessError as e:
        print(f"Error listing {bucket_path}: {e}")
        return []
    except FileNotFoundError:
        print("Error: s3cmd not found. Please make sure s3cmd is installed and in your PATH.")
        print("You may need to activate the conda environment: conda activate arbutus")
        return []

def generate_video_csv(output_dir: str = "./data", filename: str = "arbutus_videos_list.csv"):
    """Generate CSV file with all videos and their URLs."""
    
    # Define the buckets and their paths
    buckets = [
        ('brazil_farm1', 's3://brazil_farm1/good/'),
        ('brazil_farm2', 's3://brazil_farm2/good/'),
        ('ubc_farm_2022', 's3://ubc_farm_2022/short_videos_by_cow/'),
        ('ubc_farm_2022_compressed', 's3://ubc_farm_2022_compressed/')
    ]
    
    all_videos = []
    
    # Collect videos from all buckets
    for bucket_name, bucket_path in buckets:
        print(f"Processing {bucket_name}...")
        files = get_s3_files(bucket_path)
        
        for filename_s3, s3_path, size in files:
            # Extract bucket and file path from s3 path
            # s3://bucket_name/path/to/file -> bucket_name/path/to/file
            path_without_s3 = s3_path.replace('s3://', '')
            
            # Generate the HTTP URL
            url = f"http://object-arbutus.cloud.computecanada.ca/{path_without_s3}"
            
            all_videos.append({
                'bucket': bucket_name,
                'filename': filename_s3,
                'size_bytes': size,
                'url': url
            })
    
    if not all_videos:
        print("No videos found. Please check your s3cmd configuration and bucket access.")
        return
    
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create full output file path
    output_file = output_path / filename
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['bucket', 'filename', 'size_bytes', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for video in all_videos:
            writer.writerow(video)
    
    print(f"\nCSV file generated: {output_file}")
    print(f"Total videos: {len(all_videos)}")
    
    # Print summary by bucket
    bucket_counts = {}
    for video in all_videos:
        bucket = video['bucket']
        bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
    
    print("\nVideos per bucket:")
    for bucket, count in bucket_counts.items():
        print(f"  {bucket}: {count} videos")

def main():
    """Main function with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate CSV file with Arbutus S3 video listings and URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s
  %(prog)s --output-dir ./data --filename arbutus_videos.csv
  %(prog)s --output-dir /path/to/output
        """
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        default='./data',
        help='Output directory for the CSV file (default: ./data)'
    )
    
    parser.add_argument(
        '--filename', '-f',
        default='arbutus_videos_list.csv',
        help='Output filename (default: arbutus_videos_list.csv)'
    )
    
    args = parser.parse_args()
    
    # Convert to absolute path for clarity
    output_dir = os.path.abspath(args.output_dir)
    print(f"Output directory: {output_dir}")
    print(f"Output filename: {args.filename}")
    print()
    
    generate_video_csv(output_dir, args.filename)

if __name__ == "__main__":
    main()
