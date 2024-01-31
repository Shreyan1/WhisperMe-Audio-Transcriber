'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe
WhisperMe
'''

import os
import openai
from apikey import APIKEY
from getmetadata import get_audio_metadata

def transcribe_audio(audio_input, transcribed_file_name):
    openai.api_key = APIKEY

    try:
        with open(audio_input, "rb") as audio_file:
            length, metadata = get_audio_metadata(audio_input)
            audiometa = f"Audio Length: {length} seconds\nMetadata: "
            audiometa += metadata.replace("\n", " ") if metadata else "No metadata available."

            # Transcribe the audio
            transcript_response = openai.Audio.transcribe(
                model="whisper-1", 
                file=audio_file, 
                response_format="text"
            )

            # Assuming the transcription is directly in the response
            transcript = transcript_response if isinstance(transcript_response, str) else transcript_response.get('text', 'Transcription unavailable.')

        transcribed_fn = transcribed_file_name if transcribed_file_name.endswith('.txt') else transcribed_file_name + ".txt"

        if transcript:
            if os.path.exists(transcribed_fn):
                return f"File {transcribed_fn} already exists. Choose a different name or move the existing file."
            else:
                with open(transcribed_fn, 'w') as f:
                    f.write(audiometa)
                    f.write("\n\nTranscript:\n")
                    f.write(transcript)
                return f"Transcription saved to {transcribed_fn}"
        else:
            return "Error in Transcription! No text returned."
    except FileNotFoundError:
        return f"File {audio_input} not found."
    except Exception as e:
        return f"An error occurred: {e}"
