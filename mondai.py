import speech_recognition as sr
import time
import subprocess
import webbrowser
from gtts import gTTS
import os

def mondai():
    r = sr.Recognizer()
    speech = sr.Microphone()

    with speech as source:
        print("how can i help you")
        audio = r.listen(source)
        
    try:
        recog = r.recognize_google(audio, language='en-US')
        print(recog)
        print("processing...")
        speak(recog)
        time.sleep(2)
        mondai()

    except sr.UnknownValueError:
        print("sorry i didnt understand this")

def speak(recog):
    if (recog == "hello"):
        print("hello how can i help you")
        # testsay()
    elif (recog == "are you here"):
        print("I am always on your side")
    elif (recog == "how are you"):
        print("i am fine")
    elif (recog == "what are you doing today"):
        print("i am staying in your computer i think")
    elif (recog == "do you sing"):
        print("no")
    elif (recog == "shut up"):
        print("ok")
    elif (recog == "can you cook"):
        print("i can help you with that probably")
    elif (recog == "do you like me"):
        print("probably")
    elif (recog == "what's on"):
        print("right now nothing")
    elif (recog == "mistake"):
        print("alright")
    elif (recog == "what is now"):
        print("what do you mean by that")
    elif (recog == "what are you doing"):
        print("i am doing nothing right now")
    elif (recog == "could you help me"):
        print("i would like to help you")
        print("how can i help you")
    elif (recog == "you can do nothing for me"):
        print("i understood")
    elif (recog == "are you helping me now"):
        print("how can i help you")
    elif (recog == "do something"):
        print("what should i do")
    elif (recog == "who created you"):
        print("i am created by LP")
    elif (recog == "thanks"):
        print("i understand")
        start()
    else:
        functions(recog)

def functions(recog):
    print("functions processing")
    if (recog == "what's the weather like"):
        print("this is the Weather")
        webbrowser.open("https://www.wetter.com/deutschland/EUDE.html")
    elif (recog == "open Instagram"):
        print("open instagram")
        webbrowser.open_new_tab("https://instagram.com")
    elif (recog == "open YouTube"):
        print("open youtube")
        webbrowser.open_new_tab("https://youtube.com")
    elif (recog == "open Facebook"):
        print("open Facebook")
        webbrowser.open_new_tab("https://facebook.com")
    elif (recog == "I want to print something"):
        print("here are a few ideas")   
        webbrowser.open_new_tab("https://www.thingiverse.com")
    elif (recog == "open Google"):
        print("open Google")
        webbrowser.open_new_tab("https://google.com")
    elif (recog == "open stackoverflow"):
        print("open stackoverflow")
        webbrowser.open_new_tabl("https://stackoverflow.com")
    elif (recog == "open wikipedia"):
        print("open wikipedia")
        webbrowser.open("https://wikipedia.org")
    else:
        print("I didnt understand this")


def start():
    print("If you need my only say my Name")
    print("I am called Mondi")
    r = sr.Recognizer()
    speech = sr.Microphone()
    while True:
        with speech as source:
            audio = r.listen(source)
            print("Analysing name...")
            try:
                recog = r.recognize_google(audio, language = 'en-US')
                print(recog)
                if (recog == "Mondi"):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Monti"):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Modi"):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Monty" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Monday" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "mondi" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Mondeo" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "bungie" ):
                    print("starting...")
                    mondai()
                    start()
            except sr.UnknownValueError:
                print("I didnt understand this")
                start()
start()