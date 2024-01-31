'''
Created by Shreyan Basu Ray [Github - https://github.com/Shreyan1] @2024
Support me at - https://github.com/sponsors/Shreyan1

Built for the mission - "Accessible AI Education and Technology for all"
Project Repo = https://github.com/Shreyan1/WhisperMe
WhisperMe
'''

import time
import audiorecorder
import tkinter as tk

#setup log level
import logconfig
import logging as log
logconfig.logsetup()

from tkinter import messagebox, filedialog
from transcriber import transcribe_audio


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
        self.update_timer()  # Initial call to start the timer

    def stop_recording(self):
        audiorecorder.stop_recording()
        log.info("Recording Stopped")
        self.destroy()  # Close the popup
        log.info("Recording Window Closed")
        handle_recording_save()

    def update_timer(self):
        if audiorecorder.recording_active():
            elapsed_time = time.time() - self.start_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            self.timer_label.config(text=formatted_time)
            log.info(f"Timer updated: {formatted_time}")
            self.after(1000, self.update_timer)  # Schedule next update
        else:
            log.info("Timer halted.")


def start_recording():
    audiorecorder.start_recording()
    log.info("Recording Started")
    RecordingPopup(root)  # Open the popup for recording control


def handle_recording_save():
    choice = messagebox.askyesno("Recording Stopped", "Do you want to save the recording?")
    log.info("Recording Stopped", "Do you want to save the recording?")
    
    if choice:
        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio files", "*.wav")])
        if filename:
            audiorecorder.save_recording(filename)
            messagebox.showinfo("Recording Saved", f"Recording has been saved as {filename}")
            log.info("Recording saved as  %s", filename)
    else:
        messagebox.showinfo("Recording Discarded", "The recording has been discarded.")
        log.warning("Recording Discarded")


def transcribe_now():
    audio_file = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.wav *.mp3 *.ogg *.webm *.mpeg *.mpga *.mp4")])
    if audio_file:
        save_filename = filedialog.asksaveasfilename(title="Save Transcription As", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_filename:
            # Call the transcribe_audio function
            result = transcribe_audio(audio_file, save_filename)
            messagebox.showinfo("Transcription Result", result)
            log.info("File saved at %s", save_filename)


root = tk.Tk()
root.title("WhisperMe Transcriber")
root.geometry("350x100")

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# "Start Recording" button
record_start_button = tk.Button(button_frame, text="Start Recording", command=start_recording)
record_start_button.grid(row=0, column=0, pady=5, padx=5)

# "Transcribe Now" button
transcribe_button = tk.Button(button_frame, text="Transcribe Now", command=transcribe_now)
transcribe_button.grid(row=0, column=1, pady=5, padx=5)

# Centering in the frame
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure((0, 1), weight=1)

root.mainloop()

