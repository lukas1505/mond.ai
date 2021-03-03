import speech_recognition as sr
from talk import speak
import time

def mondai():
    r = sr.Recognizer()
    speech = sr.Microphone()

    with speech as source:
        print("Wie kann ich dir helfen")
        audio = r.listen(source)
        
    try:
        recog = r.recognize_google(audio, language = 'de-DE')
        print(recog)
        print("processing...")
        speak(recog)
        time.sleep(2)
        mondai()

    except sr.UnknownValueError:
        print("Das habe ich leider nicht verstanden")
