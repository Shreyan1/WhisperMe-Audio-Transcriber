#whisper api test

import openai
from apikey import APIKEY

openai.api_key = APIKEY

audio_file = open("<audiofilename>", "rb")
transcript = openai.Audio.transcribe(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

print(transcript)

audio_file.close()