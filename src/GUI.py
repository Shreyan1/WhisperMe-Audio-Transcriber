'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe-Audio-Transcriber
WhisperMe
'''

import os
import threading
import time
import datetime
import tempfile
import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread

import audiorecorder
from transcriber import transcribe_audio
from extract_audio import download_youtube_video, extract_audio_from_video

#setup log level
import logconfig
import logging as log
logconfig.logsetup()

current_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

class RecordingPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Recording...")
        self.geometry("200x100")
        
        self.timer_label = tk.Label(self, text="00:00:00")
        self.timer_label.pack(pady=10)
        
        self.stop_button = tk.Button(self, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack(pady=10)
        
        self.start_time = time.time()
        self.update_timer()

    def stop_recording(self):
        audiorecorder.stop_recording()
        log.info("Recording Stopped")
        self.destroy()
        log.info("Recording Window Closed")
        handle_recording_save()

    def update_timer(self):
        if audiorecorder.recording_active():
            elapsed_time = time.time() - self.start_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            self.timer_label.config(text=formatted_time)
            log.info(f"Timer updated: {formatted_time}")
            self.after(1000, self.update_timer)
        else:
            log.info("Timer halted.")
            
            
           
            
class ExtractAudioPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Extract Audio")
        self.geometry("500x250")

        # Section 1: Extract from YouTube
        youtube_frame = tk.LabelFrame(self, text=" YouTube Audio Extraction ", padx=10, pady=10)
        youtube_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.youtube_url_var = tk.StringVar(value="Enter youtube link here")
        self.youtube_entry = tk.Entry(youtube_frame, textvariable=self.youtube_url_var, width=60)
        self.youtube_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.extract_youtube_button = tk.Button(youtube_frame, text="Extract from YouTube", command=self.extract_from_youtube)
        self.extract_youtube_button.grid(row=1, column=0, padx=5, pady=5)

        # Section 2: Extract from File
        file_frame = tk.LabelFrame(self, text=" Local File Audio Extraction ", padx=10, pady=10)
        file_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # "Extract from File" button
        self.extract_file_button = tk.Button(file_frame, text="Extract from File", command=self.extract_from_file)
        self.extract_file_button.grid(row=0, column=0, padx=5, pady=5)

        # Adjust column configuration for centering
        self.grid_columnconfigure(0, weight=1)
        youtube_frame.grid_columnconfigure(0, weight=1)
        file_frame.grid_columnconfigure(0, weight=1)

        self.youtube_url_var.trace_add("write", self.on_youtube_url_change)  # Corrected trace_add method

    
    def on_youtube_url_change(self, *args):
        url = self.youtube_url_var.get().strip()
        if url and url != "Enter youtube link here":
            self.extract_file_button["state"] = "disabled"
        else:
            self.extract_file_button["state"] = "normal"
    
    def extract_from_youtube(self):
        
        # Create 'extracted_audio' directory if it doesn't exist
        if not os.path.exists('extracted_audio'):
            os.makedirs('extracted_audio')
        
        self.toggle_extraction_state(True)
        url = self.youtube_url_var.get().strip()
        if url and url != "Enter youtube link here":
            audio_path = f'extracted_audio/audioextract_{current_time}.ogg'
            
            with tempfile.TemporaryDirectory() as temp_dir:
                video_path = download_youtube_video(url, temp_dir)
                extract_audio_from_video(video_path, audio_path)
                
            log.info("Extracting audio from YouTube:", url) 
            messagebox.showinfo("Success", "Audio extracted successfully from YouTube.")
            log.info("Success")
        self.toggle_extraction_state(False)

    def extract_from_file(self):
        
        # Create 'extracted_audio' directory if it doesn't exist
        if not os.path.exists('extracted_audio'):
            os.makedirs('extracted_audio')
            
        self.toggle_extraction_state(True)
        video_file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4", "*.mkv", "*.avi")])
        if video_file_path:
            audio_path = f'extracted_audio/audioextract_{current_time}.ogg'
            extract_audio_from_video(video_file_path, audio_path)
            
            log.info("Extracting audio from file:", video_file_path)
            messagebox.showinfo("Success", "Audio extracted successfully from file.")
            log.info("Success")
        self.toggle_extraction_state(False)
    
    def toggle_extraction_state(self, extracting):
        state = "disabled" if extracting else "normal"
        self.extract_youtube_button["state"] = state
        self.extract_file_button["state"] = state
        if extracting:
            self.extract_youtube_button["text"] = "Extraction In Progress..."
            self.extract_file_button["text"] = "Extraction In Progress..."
        else:
            self.extract_youtube_button["text"] = "Extract from YouTube"
            self.extract_file_button["text"] = "Extract from File"

def open_extract_audio_popup(parent):
    ExtractAudioPopup(parent)
    
    

class WaitingPopup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Transcribing...")
        self.geometry("300x75")
        self.label = tk.Label(self, text="Please wait while WhisperMe is transcribing your audio...")
        self.label.pack(padx=20, pady=20)
        self.grab_set()

def transcribe_audio_with_popup(audio_input, transcribed_file_name, parent):
    def transcribe_and_close_popup():
        transcribe_audio(audio_input, transcribed_file_name)
        popup.destroy()

    popup = WaitingPopup(parent)
    transcription_thread = Thread(target=transcribe_and_close_popup)
    transcription_thread.start()

def start_recording():
    audiorecorder.start_recording()
    log.info("Recording Started")
    RecordingPopup(root)

def handle_recording_save():
    choice = messagebox.askyesno("Recording Stopped", "Do you want to save the recording?")
    if choice:
        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio files", "*.wav")])
        if filename:
            audiorecorder.save_recording(filename)
            messagebox.showinfo("Recording Saved", f"Recording has been saved as {filename}")
            log.info("Recording saved as %s", filename)
    else:
        messagebox.showinfo("Recording Discarded", "The recording has been discarded.")
        log.warning("Recording Discarded")

def transcribe_now():
    audio_file = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*flac *.wav *.mp3 *.ogg *.webm *.mpeg *.mpga *.mp4")])
    if audio_file:
        save_filename = filedialog.asksaveasfilename(title="Save Transcription As", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_filename:
            transcribe_audio_with_popup(audio_file, save_filename, root)


root = tk.Tk()
root.title("WhisperMe Transcriber")
root.geometry("350x100")

button_frame = tk.Frame(root)
button_frame.pack(expand=True)

record_start_button = tk.Button(button_frame, text="Start Recording", command=start_recording)
record_start_button.grid(row=0, column=0, pady=5, padx=5)

extract_audio_button = tk.Button(button_frame, text="Extract Audio", command=lambda: open_extract_audio_popup(root))
extract_audio_button.grid(row=0, column=1, pady=5, padx=5)

transcribe_button = tk.Button(button_frame, text="Transcribe Now", command=transcribe_now)
transcribe_button.grid(row=0, column=2, pady=5, padx=5)

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure((0, 1), weight=1)

root.mainloop()
