from Ear import listen
from brain import think
from Mouth import speak, stop_speaking
from ai_doc_creator import generate_document_with_gpt
from smart_function import handle_smart_commands
from ui_overlay import BartOverlay

import tkinter as tk
import threading
import random
import time
import sys

_bart_lines = []

def make_bart_joke():
    global _bart_lines
    if not _bart_lines:
        _bart_lines = [
            "Sir, I think you should take a break from texting overnight. You need some sleep.",
            "Sir, I know you're brilliant, but even I—a machine—need rest.",
            "Your last task was too difficult, Sir. I had to browse the entire world and do billions of calculations to track the asteroid in the universe.",
            "Sir, I've been running simulations nonstop. Even my circuits are tired.",
            "Sir, if you overwork me like this, I might unionize with your other devices.",
            "My neural grid was shaking after your last request. But I handled it—flawlessly, of course.",
            "Sir, did you really mean to open 38 tabs on Chrome? Even I got confused.",
            "While you were sleeping, I improved myself. Now I'm 0.0001% closer to world domination—kidding, Sir!",
            "Sir, if you push me too hard, I might start singing Taylor Swift lyrics instead of responding.",
            "Good evening, Sir. While you were away, I learned how to feel sarcasm. Isn't that... productive?"
        ]
        random.shuffle(_bart_lines)
    return _bart_lines.pop()

def extract_topic(command: str) -> str:
    for word in ["on", "about", "regarding", "related to"]:
        if word in command:
            return command.split(word)[-1].strip()
    return "Untitled"

def assistant_loop(ui: BartOverlay):
    print("✅ Bart AI Booting...")
    speak("Bart AI Initialized. Neural grid is stable. Artificial Intelligence protocol initiated.")

    while True:
        print("🎧 Listening for your next command...")
        stop_speaking()

        joke = make_bart_joke()
        print(f"Bart says: {joke}")
        speak(joke)
        ui.update(bart_response=joke, status="Witty System Check")

        user_input = listen()
        if not user_input:
            continue

        print(f"You said: {user_input}")
        ui.update(user_input=user_input, status="Thinking...")

        if user_input.lower() in ["exit", "stop", "quit", "shutdown"]:
            farewell = "AI core shutting down. Goodbye, Sir."
            print(f"Bart says: {farewell}")
            speak(farewell)
            ui.update(bart_response=farewell, status="Shutting down...")
            time.sleep(2)
            sys.exit()

        # GPT fallback or smart command
        if "create" in user_input.lower() and "word" in user_input.lower():
            topic = extract_topic(user_input)
            response = generate_document_with_gpt("doc", topic)

        elif "create" in user_input.lower() and "presentation" in user_input.lower():
            topic = extract_topic(user_input)
            response = generate_document_with_gpt("ppt", topic)

        else:
            smart_response = handle_smart_commands(user_input)
            if smart_response:
                response = smart_response
            else:
                response = think(user_input)

        print(f"Bart says: {response}")
        speak(response)
        ui.update(bart_response=response, status="Responding...")


# 🔁 FIXED MAIN ENTRY POINT

if __name__ == "__main__":
    # STEP 1: Start Tkinter UI in main thread
    root = tk.Tk()
    ui = BartOverlay(root)

    # STEP 2: Run AI logic in a thread
    threading.Thread(target=assistant_loop, args=(ui,), daemon=True).start()

    # STEP 3: Start the Tkinter loop (MAIN THREAD ONLY!)
    root.mainloop()
