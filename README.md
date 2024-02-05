# WhisperMe - The Ultimate OpenSource Audio Transcriber 🎙️

Welcome to the WhisperMe Audio Transcriber, the ultimate audio transcription tool powered by OpenAI's Whisper API. Designed with simplicity and efficiency in mind, WhisperMe aims to revolutionize the way we transcribe audio by offering high-quality, accessible, and user-friendly transcription services, that can be integrated by anyone with the Use-in-Code Version or be used directly with the GUI Version.

If you like the project and the mission, do leave a Star ⭐ on this repository. And if you want to further support the cause, this is where you can truly do by donating any amount you wish at this [Github Sponsors Link](https://github.com/sponsors/Shreyan1/).

![WhisperMe Banner](https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/blob/f976336968e9f968d2201065b3911ba8cb7f4558/WhisperMe%20Banner.png)

## Features :

- **High-Quality Transcription**: Leverages the cutting-edge Whisper API for accurate transcriptions. File formats supported are - *.flac *.wav *.mp3 *.ogg *.webm *.mpeg *.mpga *.mp4
- **Live Recording Feature**: Includes a live recording feature with timer and saves the audio file as an uncompressed .wav file for the highest quality recording.
- **Large File Handling**: Smartly splits large audio files into manageable chunks for transcription , ensuring efficient processing.
- **User-Friendly GUI**: Offers a straightforward interface for hassle-free operation.
- **Real-Time Logging**: Provides immediate feedback and status updates during transcription with logs for each operation.
- **Flexible Export Options**: Easily save your transcripts in various formats.

## Getting Started :

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

   ```
   git clone https://github.com/Shreyan1/WhisperMe.git
   cd WhisperMe
   ```

2. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Launch WhisperMe [on Linux and MacOS]**

   ```
   cd GUI Version
   ./run_GUI.sh
   ```

## Things to Know before your take-off :

This repository contains 2 versions of the same code logic - 
- **USE-in-CODE** : This version contains the code logic with all functionalities in a manner that can be re-used in your code by just basic integration and calling.
- **GUI Version** :  This packs a graphical user interface designed using Tkinter library to use it across all platforms. This GUI version has 2 pairs of special .sh/.bat files namely - clear_logs.sh/.bat and run_GUI.sh/.bat.

Let's understand what they do - 
- **clear_logs.sh/.bat** : This handles the automatic deletion of all the log files inside the log folder in a second, which could otherwise take a long time when multiple logs have been generated and have caused an overpopulation inside the folder resulting into a disk space issue.
- **run_GUI.sh/.bat** : This performs the direct execution of the GUI.py file without manually opening it and executing it through an editor/terminal, thus giving a software like UX while interacting with the GUI.

There is also a folder with Example Transcripts generated using this repo code by transcribing multilingual audio files for - 
- Chinese, English, French, German, Hindi, Italian, Japanese, Korean, Russian, Spanish, Tamil

Check it out to view the power of the Whisper Model.

## Usage :

1. **Start WhisperMe**: Run the `run_GUI.sh` script to launch the application.
2. **Record Live/ Select Audio File**: Click on `Start Recording` to record live and save it as a .wav file or `Transcribe Now` to select the audio file you wish to transcribe.
3. **Transcription**: Wait for the transcription to complete. A "Please wait" message will display during this process.
4. **Save Transcript**: Once transcription is complete, choose where to save your transcript file.


## Contributing :

We warmly welcome contributions from the community. Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated. Please check out our [Contributing Guide](CONTRIBUTING.md) for more details on submitting pull requests to the project.

## Support :

Encounter a bug or need support? Open an [issue](https://github.com/Shreyan1/WhisperMe/issues) or start a [discussion](https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/discussions) here now to engage and help the community to understand more.

## Acknowledgments :

- [Wikimedia](https://commons.wikimedia.org/wiki/Category:Audio_files_by_language) Audio Library
- OpenAI Team for the Whisper API
- All you contributors who will help the community by shaping WhisperMe

## License :

WhisperMe is released under the GPL-3.0 License. See the [LICENSE](https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/blob/main/LICENSE) file for more details.

## About the Author :

WhisperMe is created by Shreyan Basu Ray, a passionate advocate for the mission - "Accessible AI Education and Technology for all".

Let us connect together at - 
<h2 align="center">
  Check out more of this at - 
  <a href="https://www.linkedin.com/in/shreyanbasuray/">
    <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/LinkedIn.svg" alt="LinkedIn" width="35" height="35"/>
  </a>
  <a href="https://github.com/Shreyan1/WhisperMe-Audio-Transcriber" style="margin: 0 15px;">
    <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/af89bcc5e478013caaa514c31a3789f25e818193/icons/Github-Dark.svg" alt="GitHub" width="35" height="35"/>
  </a>
  <a href="https://twitter.com/theengineerboy1">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/X_logo_2023_%28white%29.png/600px-X_logo_2023_%28white%29.png" alt="Twitter" width="35" height="35"/>
  </a>
</h2>
<br>
