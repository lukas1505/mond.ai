import speech_recognition as sr

r = sr.Recognizer()
speech = sr.Microphone()

with speech as source:
    print("say something!…")
    # audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    recog = r.recognize_google(audio, language = 'de-DE')
    print(recog)

except sr.UnknownValueError:
    print("Das habe ich leider nicht verstanden")