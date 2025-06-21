import asyncio
import os
import edge_tts
import pygame
import tempfile
import threading

VOICE = "en-AU-WilliamNeural"
stop_flag = threading.Event()

async def generate_audio(text):
    tts = edge_tts.Communicate(text, VOICE)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    await tts.save(temp_file.name)
    return temp_file.name

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if stop_flag.is_set():
            pygame.mixer.music.stop()
            break
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove(file_path)

def speak(text):
    stop_flag.clear()
    try:
        audio_path = asyncio.run(generate_audio(text))
        play_audio(audio_path)
    except Exception as e:
        print("Error speaking:", e)

def stop_speaking():
    stop_flag.set()
