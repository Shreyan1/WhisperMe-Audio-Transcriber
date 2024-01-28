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

openai.api_key = APIKEY

audio_in= input("Type the audio file name here including .extension: ")
audio_file = open(audio_in, "rb")
length, metadata = get_audio_metadata(audio_in)
audiometa = f"Audio Length: {length} seconds\nMetadata: "
audiometa += metadata.replace("\n", " ") if metadata else "No metadata available."

try:
  transcript = openai.Audio.transcribe(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
  )

  transcribed_fn = input("Save your transcription file as: ") + ".txt"

  if transcript:
    if os.path.exists(transcribed_fn):
        print(f"File {transcribed_fn} already exists. Choose a different name or move the existing file.")
    else:
        with open(transcribed_fn, 'w') as f:
            f.write(audiometa)
            f.write("\n\nTranscript:\n")
            f.write(transcript)
  else:
      print("Error in Transcription! No text returned.")
          
except Exception as e:
  print(f"An error occurred: {e}")

audio_file.close()
