'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

import pyaudio
import wave
import threading

#setup log level
import logconfig
import logging as log
logconfig.logsetup()

# Define is_recording at the module level
is_recording = False

class AudioRecorder:
    
    log.info("audiorecorder.py > class AudioRecorder")
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

    def start_recording(self):
        log.info("audiorecorder.py > class AudioRecorder > start_recording")
        global is_recording
        is_recording = True
        while is_recording:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            self.frames.append(data)

    def stop_recording(self):
        log.info("audiorecorder.py > class AudioRecorder > stop_recording")
        global is_recording
        is_recording = False

    def save_recording(self, filename):
        log.info("audiorecorder.py > class AudioRecorder > save_recording")
        wave_file = wave.open(filename, 'wb')
        wave_file.setnchannels(self.channels)
        wave_file.setsampwidth(self.audio.get_sample_size(self.format))
        wave_file.setframerate(self.rate)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

recorder = AudioRecorder()

def start_recording():
    log.info("audiorecorder.py > start_recording")
    global recorder
    recording_thread = threading.Thread(target=recorder.start_recording)
    recording_thread.start()

def stop_recording():
    log.info("audiorecorder.py > stop_recording")
    global recorder
    recorder.stop_recording()

def save_recording(filename):
    log.info("audiorecorder.py > save_recording")
    global recorder
    recorder.save_recording(filename)
    recorder.close()

def recording_active():
    log.info("audiorecorder.py > recording_active")
    global is_recording
    return is_recording
