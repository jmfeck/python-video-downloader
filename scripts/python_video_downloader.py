# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import os
import sys
import pandas as pd
import logging
from yt_dlp import YoutubeDL
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Folder and file paths
input_foldername = 'input'
output_foldername = 'output'
log_foldername = 'logs'
input_filename = 'video_links.xlsx'
log_filename = f"{timestamp}_log.log"
input_sheetname = input_filename.split('.')[0]

# Define paths
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_input = os.path.join(path_project, input_foldername)
path_output = os.path.join(path_project, output_foldername)
path_log_folder = os.path.join(path_project, log_foldername)
path_log = os.path.join(path_log_folder, log_filename)
path_input_file = os.path.join(path_input, input_filename)

# Set up logging
os.makedirs(path_log_folder, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[logging.FileHandler(path_log), logging.StreamHandler()]
)

logging.info("Video Downloader: Starting")
logging.info(f"Video Downloader: Reading Excel file '{input_filename}'...")

# Read Excel input file
try:
    df = pd.read_excel(path_input_file, sheet_name=input_sheetname)
except Exception as e:
    logging.error(f"Video Downloader: Error reading Excel file: {e}")
    sys.exit()

num_links = len(df)
logging.info(f"Video Downloader: {num_links} link(s) found")

# Check if there are any links to process
if df.empty or 'Link' not in df.columns:
    logging.info("Video Downloader: No valid links found. Exiting the program.")
    sys.exit()

# Ensure the output folder exists
os.makedirs(path_output, exist_ok=True)

# Default values
default_extension = 'mp4'
default_quality = 'bestvideo+bestaudio/best'
default_audio_only = False

# Process each link
for idx, row in df.iterrows():
    url = row['Link']
    file_extension = row['File Extension'] if pd.notna(row.get('File Extension')) else default_extension
    quality = row['Quality'] if pd.notna(row.get('Quality')) else default_quality
    audio_only = row['Audio Only'] if pd.notna(row.get('Audio Only')) else default_audio_only
    filename = row['Filename'] if pd.notna(row.get('Filename')) else '%(title)s'

    logging.info(f"Video Downloader: Processing '{url}'")

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else quality,
        'outtmpl': os.path.join(path_output, f"{filename}.{file_extension}"),
        'quiet': True,
        'ignoreerrors': True,
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_extension,
            'preferredquality': '192',
        }]

    # Download the video
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logging.info(f"Video Downloader: Successfully downloaded '{url}'")
    except Exception as e:
        logging.error(f"Video Downloader: Error downloading '{url}': {e}")

logging.info("Video Downloader: Process completed successfully.")
