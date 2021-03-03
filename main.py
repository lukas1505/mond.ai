import speech_recognition as sr
from talk import speak

def assistant():
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
        assistant()


    except sr.UnknownValueError:
        print("Das habe ich leider nicht verstanden")