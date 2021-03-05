import speech_recognition as sr
import time
import subprocess
import webbrowser
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

def mondai():
    r = sr.Recognizer()
    speech = sr.Microphone()

    with speech as source:
        print("how can i help you")
        speaker.Speak("how can i help you")
        audio = r.listen(source)
        
    try:
        recog = r.recognize_google(audio, language='en-US')
        print(recog)
        print("processing...")
        speaker.Speak("processing")
        speak(recog)
        time.sleep(2)
        mondai()

    except sr.UnknownValueError:
        print("sorry i didnt understand this")
        speaker.Speak("sorry i didnt understand this")

def speak(recog):
    if (recog == "hello"):
        print("hello how can i help you")
        speaker.Speak("hello how can i help you")
        # testsay()
    elif (recog == "are you here"):
        print("I am always on your side")
        speaker.Speak("I am always on your side")
    elif (recog == "how are you"):
        print("i am fine")
        speaker.Speak("i am fine")
    elif (recog == "what are you doing today"):
        print("i am staying in your computer i think")
        speaker.Speak("i am staying in your computer i think")
    elif (recog == "do you sing"):
        print("no")
        speaker.Speak("no")
    elif (recog == "shut up"):
        print("ok")
        speaker.Speak("shut up")
    elif (recog == "can you cook"):
        print("i can help you with that probably")
        speaker.Speak("i can help you with that probably")
    elif (recog == "do you like me"):
        print("probably")
        speaker.Speak("probably")
    elif (recog == "what's on"):
        print("right now nothing")
        speaker.Speak("right now nothing")
    elif (recog == "mistake"):
        print("alright")
        speaker.Speak("alright")
    elif (recog == "what is now"):
        print("what do you mean by that")
        speaker.Speak("what is now")
    elif (recog == "what are you doing"):
        print("i am doing nothing right now")
        speaker.Speak("i am doing nothing right now")
    elif (recog == "could you help me"):
        print("i would like to help you")
        print("how can i help you")
        speaker.Speak("i would like to help you")
        speaker.Speak("how can i help you")
    elif (recog == "you can do nothing for me"):
        print("i understood")
        speaker.Speak("i understood")
    elif (recog == "are you helping me now"):
        print("how can i help you")
        speaker.Speak("how can i help you")
    elif (recog == "do something"):
        print("what should i do")
        speaker.Speak("what should i do")
    elif (recog == "who created you"):
        print("i am created by LP")
        speaker.Speak("i am created by LP")
    elif (recog == "thanks"):
        print("i understand")
        speaker.Speak("i unterstand")
        start()
    else:
        functions(recog)

def functions(recog):
    print("functions processing")
    if (recog == "what's the weather like"):
        print("this is the Weather")
        speaker.Speak("this is the Weather")
        webbrowser.open("https://www.wetter.com/deutschland/EUDE.html")
    elif (recog == "open Instagram"):
        print("open instagram")
        speaker.Speak("open instagram")
        webbrowser.open_new_tab("https://instagram.com")
    elif (recog == "open YouTube"):
        print("open youtube")
        speaker.Speak("open Youtube")
        webbrowser.open_new_tab("https://youtube.com")
    elif (recog == "open Facebook"):
        print("open Facebook")
        speaker.Speak("open Facebook")
        webbrowser.open_new_tab("https://facebook.com")
    elif (recog == "I want to print something"):
        print("here are a few ideas")
        speaker.Speak("here are a few ideas")   
        webbrowser.open_new_tab("https://www.thingiverse.com")
    elif (recog == "open Google"):
        print("open Google")
        speaker.Speak("open Google")
        webbrowser.open_new_tab("https://google.com")
    elif (recog == "open stackoverflow"):
        print("open stackoverflow")
        speaker.Speak("open stack overflow")
        webbrowser.open_new_tabl("https://stackoverflow.com")
    elif (recog == "open wikipedia"):
        print("open Wikipedia")
        speaker.Speak("open wikipedia")
        webbrowser.open("https://wikipedia.org")
    else:
        print("I didnt understand this")
        speaker.Speak("i didnt understand this")


def start():
    print("If you need me only say my Name")
    speaker.Speak("if you need me only say my Name")
    print("I am called Mondi")
    speaker.Speak("I am called Mondi")
    r = sr.Recognizer()
    speech = sr.Microphone()
    while True:
        with speech as source:
            audio = r.listen(source)
            try:
                recog = r.recognize_google(audio, language = 'en-US')
                print(recog)
                if (recog == "Mondi"):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "Monti"):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "Modi"):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "Monty" ):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "Monday" ):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "mondi" ):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "Mondeo" ):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
                if (recog == "bungie" ):
                    print("starting...")
                    speaker.Speak("starting")
                    mondai()
                    start()
            except sr.UnknownValueError:
                print("try again")
                speaker.Speak("try again")
                start()
start()