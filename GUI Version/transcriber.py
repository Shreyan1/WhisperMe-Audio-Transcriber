'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

import os
import openai

#setup log level
import logconfig
import logging as log
logconfig.logsetup()

from pydub import AudioSegment
from apikey import APIKEY
from getmetadata import get_audio_metadata

def transcribe_audio(audio_input, transcribed_file_name):
    openai.api_key = APIKEY

    # Calculate the file size
    file_size = os.path.getsize(audio_input)
    log.info("File size of the audio is %s", file_size)
    max_file_size = 25 * 1024 * 1024  # 25 MB in bytes

    try:
        audio = AudioSegment.from_file(audio_input)
        length, metadata = get_audio_metadata(audio_input)
        audiometa = f"Audio Length: {length} seconds\nMetadata: "
        audiometa += metadata.replace("\n", " ") if metadata else "No metadata available."

        transcripts = []

        if file_size <= max_file_size:
            log.info("File size is within 25MB limit")
            with open(audio_input, "rb") as audio_file:
                transcript_response = openai.Audio.transcribe(
                    model="whisper-1", 
                    file=audio_file, 
                    response_format="text"
                )
                transcript = transcript_response if isinstance(transcript_response, str) else transcript_response.get('text', 'Transcription unavailable.')
                transcripts.append(transcript)
        else:
            log.info("File size is more than the 25MB limit, moving to split and transcribe")
            
            # Split and transcribe the audio
            segment_length_ms = 10 * 60 * 1000
            for i in range(0, len(audio), segment_length_ms):
                segment = audio[i:i+segment_length_ms]
                segment_file = "temp_segment.mp3"
                segment.export(segment_file, format="mp3")

                with open(segment_file, "rb") as segment_audio_file:
                    transcript_response = openai.Audio.transcribe(
                        model="whisper-1", 
                        file=segment_audio_file, 
                        response_format="text"
                    )
                    transcript = transcript_response if isinstance(transcript_response, str) else transcript_response.get('text', 'Transcription unavailable.')
                    transcripts.append(transcript)
                os.remove(segment_file)

        transcribed_fn = transcribed_file_name if transcribed_file_name.endswith('.txt') else transcribed_file_name + ".txt"

        if transcripts:
            if os.path.exists(transcribed_fn):
                log.warn(f"File {transcribed_fn} already exists. Choose a different name or move the existing file.")
                return f"File {transcribed_fn} already exists. Choose a different name or move the existing file."
            else:
                with open(transcribed_fn, 'w') as f:
                    f.write(audiometa)
                    f.write("\n\nTranscript:\n")
                    for transcript in transcripts:
                        f.write(transcript + "\n")
                log.info("Transcription saved to %s", transcribed_fn)
                return f"Transcription saved to {transcribed_fn}"
        else:
            log.critical("Error in Transcription. No text returned")
            return "Error in Transcription! No text returned."
        
    except FileNotFoundError:
        log.error(f"File {audio_input} not found.")
        return f"File {audio_input} not found."
    
    except Exception as e:
        log.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"
