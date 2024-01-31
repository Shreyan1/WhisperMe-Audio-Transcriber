'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe
WhisperMe
'''

import tkinter as tk
import audiorecorder

from tkinter import filedialog, messagebox
from transcriber import transcribe_audio

def start_recording():
    audiorecorder.start_recording()
    messagebox.showinfo("Recording", "Recording started")

def stop_and_handle_recording():
    audiorecorder.stop_recording()
    handle_recording_save()

def handle_recording_save():
    choice = messagebox.askyesno("Recording Stopped", "Do you want to save the recording?")
    if choice:
        save_recording()
    else:
        messagebox.showinfo("Recording Discarded", "The recording has been discarded.")

def save_recording():
    filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if filename:
        audiorecorder.save_recording(filename)
        messagebox.showinfo("Recording Saved", f"Recording has been saved as {filename}")

def transcribe():
    audio_file = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.wav *.mp3")])
    if audio_file:
        save_filename = filedialog.asksaveasfilename(title="Save Transcription As", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_filename:
            result = transcribe_audio(audio_file, save_filename)
            messagebox.showinfo("Transcription Result", result)

root = tk.Tk()
root.title("Transcription Service")

# Adjust the recording buttons to use the new stop and handle function
record_start_button = tk.Button(root, text="Start Recording", command=start_recording)
record_start_button.pack(pady=5)

# Removed the stop button as the stopping will now be handled via console input
record_stop_button = tk.Button(root, text="Stop Recording", command=stop_and_handle_recording)
record_stop_button.pack(pady=5)

# Transcription button
transcribe_button = tk.Button(root, text="Transcribe Audio", command=transcribe)
transcribe_button.pack(pady=5)

root.mainloop()
