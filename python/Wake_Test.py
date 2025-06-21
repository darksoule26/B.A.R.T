from vosk import Model, KaldiRecognizer
import pyaudio
import json

model_path = r"D:\PROJECTS\JARVIS\vosk-model-small-en-in-0.4"
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("🎤 Say 'Bart' to test wake-word recognition")

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print("Heard:", result.get("text"))
        if "hat" in result.get("text", "").lower():
            print("✅ Wake word 'Bart' detected!")
            break
