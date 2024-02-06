<h1 align="center">
   WhisperMe - The Ultimate OpenSource Audio Transcriber 🎙️
</h1>

Welcome to the WhisperMe Audio Transcriber, the ultimate audio transcription tool powered by OpenAI's Whisper API. 

Designed with simplicity and efficiency in mind, WhisperMe aims to revolutionize the way we transcribe audio by offering high-quality, accessible, and user-friendly transcription services, that can be integrated by anyone with the **Use-in-Code** Version or be used directly with the **GUI Version**.

If you like the project and the mission, do leave a Star ⭐ on this repository. And if you want to further support the cause, this is where you can truly do by donating any amount you wish, here - [Github Sponsors Link](https://github.com/sponsors/Shreyan1/).

<p align="center">
   <img src="https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/blob/67386668364c966fcb98ef2a4ba670e5176d608a/WhisperMe%20Banner.png" width="700">
</p>


## Features :

- **High-Quality Transcription**: Leverages the cutting-edge Whisper API for accurate transcriptions. File formats supported are - `*.flac *.wav *.mp3 *.ogg *.webm *.mpeg *.mpga *.mp4`
- **Live Recording Feature**: Includes a live recording feature with timer and saves the audio file as an uncompressed .wav file for the highest quality recording.
- **Large File Handling**: Smartly splits large audio files into manageable chunks for transcription , ensuring efficient processing.
- **User-Friendly GUI**: Offers a straightforward and the most simple interface for hassle-free operation.
- **Real-Time Logging**: Provides immediate feedback and status updates during transcription with logs for each operation.
- **Simplest Export Option**: Easily save your transcripts in the most simplest and easy-to-use option with `.txt`

## Getting Started : 🏁

### Installation 👨‍💻

1. **Clone the Repository** : ` git clone https://github.com/Shreyan1/WhisperMe.git ` ; `cd WhisperMe`

2. **Install Dependencies** : ` pip install -r requirements.txt `

3. **Launch WhisperMe [on Linux and MacOS]** : `cd GUI Version` ; `./run_GUI.sh` on Linux or MacOS ; `.\myScript.bat` on Windows using Powershell


## Things to Know before your take-off : 🛫

The ideal max audio file size is 25MB, so anything less than that will be completely fine, although larger file handling has been integrated in this code but still.

This repository contains **2 versions** of the same code logic - 
- **USE-in-CODE** : This version contains the code logic with all functionalities in a manner that can be re-used in your code by just basic integration and calling.
- **GUI Version** :  This packs a graphical user interface designed using Tkinter library to use it across all platforms. This GUI version has 2 pairs of special .sh/.bat files namely - `clear_logs.sh/.bat` and `run_GUI.sh/.bat`.

Let's understand what they do - 
- **clear_logs.sh/.bat** : This handles the automatic deletion of all the log files inside the log folder in a second, which could otherwise take a long time when multiple logs have been generated and have caused an overpopulation inside the folder resulting into a disk space issue.
- **run_GUI.sh/.bat** : This performs the direct execution of the GUI.py file without manually opening it and executing it through an editor/terminal, thus giving a software like UX while interacting with the GUI.

There is also a folder with Example Transcripts generated using this repo code by transcribing multilingual audio files for - `Chinese, English, French, German, Hindi, Italian, Japanese, Korean, Russian, Spanish, Tamil`

Check out the folder to view the power of the Whisper Model.

## Usage : 💽

1. **Start WhisperMe**: Run the `run_GUI.sh` script to launch the application.
2. **Record Live/ Select Audio File**: Click on `Start Recording` to record live and save it as a .wav file or `Transcribe Now` to select the audio file you wish to transcribe.
3. **Transcription**: Wait for the transcription to complete. A "Please wait" message will display during this process.
4. **Save Transcript**: Once transcription is complete, choose where to save your transcript file.

## Service Usage : 🛎️
You can access and use it all you want but there are 3 options to access the core service - 
1. **The Flash way** : If you already have an OpenAI API Subscription, then just include your api inside the apikey.py file inside the variable `APIKEY=` or,
   
2. **The Quicksilver Way** : Mail in the audio file directly at my mailing address - [shreyan.github@gmail.com](shreyan.github@gmail.com) and let me know if you need _any thing specific_ and _by how many days_. I'll mail you the price depending on the length of the audio. It'll typically be starting from $0.50 / ₹29.00 for any audio file less than 20 minutes.
   
3. **The Sonic-the-Hedgehog Way**: Subscription for one time usage-
   - $0.99 /₹49.00 for 3 hours of WhisperMe Usage.
   - $1.95 /₹95.00 for 6 hours of usage.
   - $2.90 /₹125.00 for 9 hours of usage.

### How to subscribe and get the service - 
You can directly pay through the Github Sponsors link for this repo by clicking on the Sponsors button or by clicking on the link here- [Pay via Github Sponsors](https://github.com/sponsors/Shreyan1/) and then drop a mail at [shreyan.github@gmail.com](shreyan.github@gmail.com)

We'll send you a private API key within a few hours for the subscribed hours at your email address. The API key will automatically get de-activated after the susbscribed hours of usage. To extend it you can either subscribe again or pre-subscribe with more hours for as long as you want and the price will be calculated as : $(0.99+(n−1)×0.95) or ₹(-2.5n^2 + 57.5n - 6) for n hours.

## Contributing : 🫶

We warmly welcome contributions from the community. Whether you're fixing bugs, adding new features, or improving documentation, your help is appreciated. Please check out our [Contributing Guide](CONTRIBUTING.md) for more details on submitting pull requests to the project.

## Support : 🤝

Encounter a bug or need support? Open an [issue](https://github.com/Shreyan1/WhisperMe/issues) or start a [discussion](https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/discussions)🗣️ here now to engage and help the community to understand more.

## Acknowledgments : 🙏

- [Wikimedia](https://commons.wikimedia.org/wiki/Category:Audio_files_by_language) Audio Library
- OpenAI Team for the Whisper API
- All you contributors who will help the community by shaping WhisperMe

## License : 🪪

WhisperMe is released under the GPL-3.0 License. See the [LICENSE](https://github.com/Shreyan1/WhisperMe-Audio-Transcriber/blob/main/LICENSE) file for more details.

## About the Author : ✍️

WhisperMe is created by Shreyan Basu Ray, a passionate advocate for the mission - "Accessible AI Education and Technology for all".

Let us connect together at - 
<h2 align="left">
  <a href="shreyan.github@gmail.com" style="margin: 0 15px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" alt="LinkedIn" width="35" height="35"/>
  </a>
  <a href="https://www.linkedin.com/in/shreyanbasuray/" style="margin: 0 15px;">
    <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/LinkedIn.svg" alt="LinkedIn" width="35" height="35"/>
  </a>
  <a href="https://twitter.com/theengineerboy1">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg" alt="Twitter" width="35" height="35"/>
  </a>
</h2>
<br>
