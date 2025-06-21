from Ear import listen
from brain import think
from Mouth import speak, stop_speaking
import threading
import random

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

def response_thread_function(response):
    speak(response)

def intro():
    startup_message = (
        "Bart AI Initialized. "
        "Welcome Sir, Good day, AI core activated. "
        "Neural grid is stable. Artificial Intelligence protocol initiated. "
        "Listening automatically, Sir."
    )
    speak(startup_message)

def main():
    print("✅ Bart AI Booting...")
    intro()

    while True:
        print("🎧 Listening for your next command...")
        stop_speaking()

        joke = make_bart_joke()
        print(f"Bart says: {joke}")
        speak(joke)

        user_input = listen()
        if not user_input:
            continue

        print(f"You said: {user_input}")
        if user_input.lower() in ["exit", "stop", "quit"]:
            speak("AI core, Shutting down. Artificial Intelligence protocol Off. Goodbye, Sir.")
            break

        response = think(user_input)
        print(f"Bart says: {response}")

        t = threading.Thread(target=response_thread_function, args=(response,))
        t.start()
        t.join()

if __name__ == "__main__":
    main()


