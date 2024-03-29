'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

import os

#setup log level
import logconfig
import logging as log
logconfig.logsetup()

from pydub import AudioSegment
from mutagen import File
import os


def get_audio_metadata(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        log.warning("File does not exist")
        return "File does not exist", ""

    try:
        # Get audio length
        audio = AudioSegment.from_file(file_path)
        length_seconds = len(audio) / 1000
        
    except Exception as e:
        log.critical("File does not exist")
        return f"Error processing audio length: {e}", ""

    try:
        # Get metadata with mutagen
        # Using easy=True to simplify metadata, otherwise album would come as TALB, date as TDRC, etc
        #TCON: Death Metal TDRC: 2024 TALB: WhisperMe TIT2: SpeechTest TPE1: Shreyan
        audio_file = File(file_path, easy=True)
        metadata = audio_file.tags if audio_file else {}
        log.info("Metadata retreived")
        
    except Exception as e:
        log.critical("Error extracting metadata")
        return length_seconds, f"Error extracting metadata: {e}"

    # Format metadata
    metadata_str = ""
    #Check if metadata is not empty and apply format
    if metadata:
        metadata_items = [f"{key}: {', '.join(value) if isinstance(value, list) else value}" for key, value in metadata.items()]
        metadata_str = ', '.join(metadata_items)
        log.info("Metadata formatted")

    return length_seconds, metadata_str.strip()

