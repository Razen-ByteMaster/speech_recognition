import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_filename = "test.wav"
FILENAME_FROMMIC = "RECORDING.wav"
VOICE_TEXT_FILENAME = "VOICE_TEXT.txt"

r = sr.Recognizer()


def recognize_from_file(filename):
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text


def recognize_from_mic(file_to_write):
    SAMPLE_RATE = 16000
    duration = 5  # seconds
    audio_recording = sd.rec(
        int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1
    )
    print("Recording...")
    sd.wait()
    print("Audio recording complete, Playing back...")
    sd.play(audio_recording, SAMPLE_RATE)
    sd.wait()
    print("Play audio complete")
    wav.write(file_to_write, SAMPLE_RATE, audio_recording)


def save_text_to_file(text, filename):
    with open(filename, "w") as f:
        f.write(text)


if __name__ == "__main__":
    # Check if test_filename exists
    try:
        print(recognize_from_file(test_filename))
    except FileNotFoundError:
        print(f"File '{test_filename}' not found.")

    # Record from microphone and save it
    recognize_from_mic(FILENAME_FROMMIC)

    # Now process the saved file and extract text
    text_from_voice = recognize_from_file(FILENAME_FROMMIC)
    save_text_to_file(text_from_voice, VOICE_TEXT_FILENAME)
