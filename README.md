# Voice Recognition and Recording Tool

This Python script enables audio recording from a microphone or an existing audio file, performs speech-to-text conversion, and saves the resulting text to a `.txt` file. By leveraging the `speech_recognition` library, it allows seamless transcription of speech from both recorded files and live microphone input.

## Features

- Records audio directly from the microphone and saves it as a WAV file.
- Converts recorded audio or file-based speech into text using Google's Speech-to-Text API.
- Allows playback of the recorded audio after capturing it.
- Saves the transcribed text into a `.txt` file for further use.
- Easy to use for both microphone and file-based transcription.

## Requirements

- Python 3.x
- `speech_recognition`, `sounddevice`, `numpy`, and `scipy` libraries.

## Installation

1. Install the necessary Python packages:

   ```bash
   pip install SpeechRecognition sounddevice numpy scipy
   ```

## Usage

To use the script, run it in your terminal. It will attempt to recognize speech from a file if provided. If the file is not found, it will record new audio from the microphone.

```bash
python voice_recognition.py
```

Once the script is running, it will:
1. Try to transcribe speech from the provided file (`test.wav`).
2. If the file is not found, it will record audio from the microphone, play it back, and save it as `RECORDING.wav`.
3. The script will then transcribe the saved recording and store the transcribed text in `VOICE_TEXT.txt`.
