import speech_recognition as sr
from mark01 import mondai

def start():
    print("Wenn du mich brauchst sag einfach meinen Namen")
    print("Ich heiße Mondi")
    r = sr.Recognizer()
    speech = sr.Microphone()
    while True:
        with speech as source:
            audio = r.listen(source)
            print("Ich analysiere meinen Namen...")
            try:
                recog = r.recognize_google(audio, language = 'de-DE')
                print(recog)
                if (recog == "Mondi"):
                    print("starting...")
                    assistant()
                    start()
            except sr.UnknownValueError:
                print("Das habe ich leider nicht verstanden")
start()
            

