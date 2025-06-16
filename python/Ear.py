import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True) 

def print_loop():
    while True:
        print(Fore.GREEN + "I am Listning...",end="",flush=True)
        print(Style.RESET_ALL, end="", flush=True)
        print("",end="", flush=True)


def Trans_hindi_to_english(txt):
    english_txt = translate(txt, to_language="en-in")
    return english_txt
        
def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold=False
    recognizer.energy_threshold=35000
    recognizer.dynamic_energy_adjustment_damping=0.03  #less more active
    recognizer.dynamic_energy_ratio=1.9  #less more active
    recognizer.pause_threshold=0.5  
    recognizer.operation_timeout=None
    recognizer.pause_threshold=0.2
    recognizer.non_speaking_duration=0.1


    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "I am Listening...", end="", flush=True  )
            try:
                audio=recognizer.listen(source, timeout=None)
                print("\r"+Fore.CYAN + "Got it, Recognizing...",end="", flush=True)
                recognizer_txt= recognizer.recognize_google(audio).lower()
                if recognizer_txt:
                    translate_txt=Trans_hindi_to_english(recognizer_txt)
                    print("\r" + Fore.CYAN + "Mr U S T: " + translate_txt)
                    return translate_txt
                
                else:
                    return ""
                
            except sr.UnknownValueError:
                recognizer_txt = ""
            finally:
                print("\r", end="", flush=True)

            os.system('cls' if os.name == 'nt' else 'clear')
            # threading part 
            listning_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=print_loop)
            listning_thread.start()
            print_thread.start()
            listning_thread.join()
            print_thread.join()

listen()