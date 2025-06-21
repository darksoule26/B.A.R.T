from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

model_path = r"D:\PROJECTS\JARVIS\vosk-model-small-en-in-0.4"
if not os.path.exists(model_path):
    raise Exception(f"Model not found at {model_path}")

model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

def detect_bart():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            heard = result.get("text", "")
            print(f"Heard: {heard}")
            if "fat" in heard.lower():
                print("✅ Wake word 'Bart' detected!")
                return True
