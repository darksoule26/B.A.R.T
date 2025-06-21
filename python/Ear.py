import speech_recognition as sr
from mtranslate import translate

def Trans_hindi_to_english(txt):
    return translate(txt, to_language="en-in")

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.6  # allows a short pause in speech
    recognizer.non_speaking_duration = 0.2  # sensitivity to speech start

    with sr.Microphone() as source:
        print("🎤 Auto Listening... Speak when ready.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("🧠 Recognizing...")
            text = recognizer.recognize_google(audio, language="hi-IN").lower()
            return Trans_hindi_to_english(text)
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            print(f"Error in listening: {e}")
            return ""
