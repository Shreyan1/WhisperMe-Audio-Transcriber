'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

from pytube import YouTube
from moviepy.editor import VideoFileClip

# Setup log level
import logconfig
import logging as log
logconfig.logsetup()

def download_youtube_video(url, temp_dir):
    yt = YouTube(url)
    log.info(f"Downloading video from Youtube... Link- {url}")
    video = yt.streams.filter(progressive=True, file_extension='mp4').first()
    filepath = video.download(output_path=temp_dir)
    log.info("Downloading complete to temporary folder")
    return filepath

def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    log.info("Audio Extracting...")
    audio.write_audiofile(audio_path)
    log.info(f"Audio Extracted and Saved at- {audio_path}")
    video.close()
    audio.close()
    
