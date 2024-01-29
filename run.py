'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe
WhisperMe
'''

from transcriber import transcribe_audio
from audiorecorder import record_audio

ask = input("Press 'N' to make a new recording, press 'T' to transcribe an existing one: ")
if ask.lower() == "n":
    filename = record_audio()
    
    asktranscribe = input("Do you want to transcribe the file now? (Y/N): ")
    
    if asktranscribe.lower() == "y" and filename:
        transcribe_audio(filename)
    elif asktranscribe.lower() == "n":
        print("Your recording is saved. Feel free to transcribe it later.")
        
elif ask.lower() == "t":
    audio_in = input("Type the audio file name here including .extension: ")
    transcribe_audio(audio_in)
