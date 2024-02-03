'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

#Sample usage in .py file- 
# from audiorecorder import record_audio
# record_audio()

import pyaudio
import wave
import threading

class AudioRecorder:
    def __init__(self, format=pyaudio.paInt16, channels=2, rate=44100, chunk=1024):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format, channels=self.channels,
                                      rate=self.rate, input=True,
                                      frames_per_buffer=self.chunk)
        self.frames = []
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        print("Recording live... (Type 'stop' and press Enter to stop)")
        while self.is_recording:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            self.frames.append(data)

    def stop_recording(self):
        self.is_recording = False
        print("Finished recording!")

    def save_recording(self, filename):
        wave_file = wave.open(filename, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(self.format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()
        print(f"Recording saved as {filename}")

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

def record_audio():
    recorder = AudioRecorder()

    recording_thread = threading.Thread(target=recorder.start_recording)
    recording_thread.start()

    while recorder.is_recording:
        if input() == 'stop':
            recorder.stop_recording()

    recording_thread.join()

    filename = None  # Initialize filename to None
    save = input("Do you want to save the recording? (yes/no): ").lower()
    if save == 'yes':
        filename = input("Save your audio file as: ") + ".wav"
        recorder.save_recording(filename)
        print(f"Recording saved as {filename}")
    else:
        print("Recording discarded.")

    recorder.close()
    return filename

