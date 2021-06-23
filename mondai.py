import speech_recognition as sr
import time
import subprocess
import webbrowser
import gtts
from playsound import playsound
import os
import sys

def getvars():
    file1 = open("pathtospotify.txt", "r")
    global spotifypath
    spotifypath=file1.read()
    print(spotifypath)
getvars()

def mondai():
    r = sr.Recognizer()
    speech = sr.Microphone()

    with speech as source:
        print("how can i help you")
        tts = gtts.gTTS("hello master")
        try:
            tts.save("hello.mp3")
        except OSError:
                pass
        playsound("hello.mp3")
        audio = r.listen(source)
        
    try:
        recog = r.recognize_google(audio, language='en-US')
        print(recog)
        print("processing...")
        speak(recog)
        time.sleep(2)
        mondai()

    except sr.UnknownValueError:
        print("sorry i dont understand this")
        tts = gtts.gTTS("sorry i dont understand this")
        try:
            tts.save("dontunderstand.mp3")
        except OSError:
            pass
        playsound("dontunderstand.mp3")
        os.remove("dontunderstand.mp3 ")

def speak(recog):
    if (recog == "hello"):
        print("hello how can i help you")
        tts = gtts.gTTS("hello how can i help you")
        tts.save("howcanihelp.mp3")
        playsound("howcanihelp.mp3")
        os.remove("howcanihelp.mp3")
    elif (recog == "are you here"):
        print("I am always on your side")
        tts = gtts.gTTS("I am always on your side")
        tts.save("onside.mp3")
        playsound("onside.mp3")
        os.remove("onside.mp3")
    elif (recog == "how are you"):
        print("i am fine")
        tts = gtts.gTTS("i am fine")
        tts.save("fine.mp3")
        playsound("fine.mp3")
        os.remove("fine.mp3")
    elif (recog == "what are you doing today"):
        print("i am staying in your computer i think")
        tts = gtts.gTTS("i am staying in your computer i think")
        tts.save("stayincomputer.mp3")
        playsound("stayincomputer.mp3")
        os.remove("stayincomputer.mp3")
    elif (recog == "do you sing"):
        print("no")
        tts = gtts.gTTS("no")
        tts.save("no.mp3")
        playsound("no.mp3")    
        os.remove("no.mp3")    
    elif (recog == "shut up"):
        print("ok")
        tts = gtts.gTTS("shut up")
        tts.save("shutup.mp3")
        playsound("shutup.mp3")  
        os.remove("shutup.mp3")
    elif (recog == "can you cook"):
        print("i can help you with that probably")
        tts = gtts.gTTS("i can help you with that probably")
        tts.save("help.mp3")
        playsound("help.mp3") 
        os.remove("help.mp3")
    elif (recog == "do you like me"):
        print("probably")
        tts = gtts.gTTS("probably")
        tts.save("probably.mp3")
        playsound("probably.mp3")
        os.remove("probably.mp3")
    elif (recog == "what's on"):
        print("right now nothing")
        tts = gtts.gTTS("right now nothing")
        tts.save("nothing.mp3")
        playsound("nothing.mp3")
        os.remove("nothing.mp3")
    elif (recog == "mistake"):
        print("alright")
        tts = gtts.gTTS("alright")
        tts.save("alright.mp3")
        playsound("alright.mp3")
        os.remove("alright.mp3")
    elif (recog == "what is now"):
        print("what do you mean by that")
        tts = gtts.gTTS("what do you mean by that")
        tts.save("mean.mp3")
        playsound("mean.mp3")
        os.remove("mean.mp3")
    elif (recog == "what are you doing"):
        print("i am doing nothing right now")
        tts = gtts.gTTS("i am doing nothing right now")
        tts.save("doingnothing.mp3")
        playsound("doingnothing.mp3")
        os.remove("doingnothin.mp3")
    elif (recog == "could you help me"):
        print("i would like to help you")
        tts = gtts.gTTS("i would like to help you")
        tts.save("liketohelp.mp3")
        playsound("liketohelp.mp3")
        os.remove("liketohelp.mp3")
    elif (recog == "you can do nothing for me"):
        print("i understood")
        tts = gtts.gTTS("i understood")
        tts.save("understood.mp3")
        playsound("understood.mp3")
        os.remove("understood.mp3")
    elif (recog == "are you helping me now"):
        print("how can i help you")
        tts = gtts.gTTS("how can i help you")
        tts.save("howcanihelp.mp3")
        playsound("howcanihelp.mp3")
        os.remove("howcanihelp.mp3")
    elif (recog == "do something"):
        print("what should i do")
        tts = gtts.gTTS("what should i do")
        tts.save("whatshouldido.mp3")
        playsound("whatshouldido.mp3")
        os.remove("whatshouldido.mp3")
    elif (recog == "who created you"):
        print("i am created by LP")
        tts = gtts.gTTS("i am created by LP")
        tts.save("created.mp3")
        playsound("created.mp3")
        os.remove("created.mp3")
    elif (recog == "exit"):
        print("i am exiting you world")
        tts = gtts.gTTS("i am leaving")
        tts.save("leaving.mp3")
        playsound("leaving.mp3")
        os.remove("leaving.mp3")
        sys.exit()
    elif (recog == "thanks"):
        print("i understand")
        tts = gtts.gTTS("i unterstand")
        tts.save("understand.mp3")
        playsound("understand.mp3")
        os.remove("understand.mp3")
        start()
    else:
        functions(recog)

def functions(recog):
    print("functions processing")
    if (recog == "what's the weather like"):
        print("this is the Weather")
        tts = gtts.gTTS("this is the Weather")
        tts.save("wheater.mp3")
        playsound("wheater.mp3")
        webbrowser.open("https://www.wetter.com/deutschland/EUDE.html")
        os.remove("wheater.mp3")
    elif (recog == "open Instagram"):
        print("open instagram")
        tts = gtts.gTTS("open instagram")
        tts.save("instagram.mp3")
        playsound("instagram.mp3")
        webbrowser.open_new_tab("https://instagram.com")
        os.remove("instagram.mp3")
    elif (recog == "open Spotify"):
        print("open spotify")
        tts = gtts.gTTS("open Spotify")
        tts.save("spotify.mp3")
        playsound("spotify.mp3")
        os.system(spotifypath)
        os.remove("spotify.mp3")
    elif (recog == "open YouTube"):
        print("open youtube")
        tts = gtts.gTTS("open Youtube")
        tts.save("youtube.mp3")
        playsound("youtube.mp3")
        webbrowser.open_new_tab("https://youtube.com")
        os.remove("youtube.mp3")
    elif (recog == "open Facebook"):
        print("open Facebook")
        tts = gtts.gTTS("open Facebook")
        tts.save("facebook.mp3")
        playsound("facebook.mp3")
        webbrowser.open_new_tab("https://facebook.com")
        os.remove("facebook.mp3")
    elif (recog == "I want to print something"):
        print("here are a few ideas")
        tts = gtts.gTTS("here are a few ideas")
        tts.save("ideasprint.mp3")
        playsound("ideasprint.mp3")   
        webbrowser.open_new_tab("https://www.thingiverse.com")
        os.remove("ideasprint.mp3")
    elif (recog == "open Google"):
        print("open Google")
        tts = gtts.gTTS("open Google")
        tts.save("google.mp3")
        playsound("google.mp3") 
        webbrowser.open_new_tab("https://google.com")
        os.remove("google.mp3")
    elif (recog == "open stack overflow"):
        print("open stackoverflow")
        tts = gtts.gTTS("open stack overflow")
        tts.save("overflow.mp3")
        playsound("overflow.mp3")
        webbrowser.open_new_tab("https://stackoverflow.com")
        os.remove("overflow.mp3")
    elif (recog == "open wikipedia"):
        print("open Wikipedia")
        tts = gtts.gTTS("open wikipedia")
        tts.save("wikipedia.mp3")
        playsound("wikipedia.mp3")
        webbrowser.open("https://wikipedia.org")
        os.remove("wikipedia.mp3")
    elif (recog == "new tab"):
        print("open new tab")
        tts = gtts.gTTS("open new tab")
        tts.save("tab.mp3")
        playsound("tab.mp3")
        webbrowser.open("https://google.com")
        os.remove("tab.mp3")
    elif (recog == "new tap"):
        print("open new tab")
        tts = gtts.gTTS("open new tab")
        tts.save("tab.mp3")
        playsound("tab.mp3")
        webbrowser.open("https://google.com")
        os.remove("tab.mp3")
    elif (recog == "new top"):
        print("open new tab")
        tts = gtts.gTTS("open new tab")
        tts.save("tab.mp3")
        playsound("tab.mp3")
        webbrowser.open("https://google.com")
        os.remove("tab.mp3")
    elif (recog == "open Wikipedia"):
        print("open Wikipedia")
        tts = gtts.gTTS("open wikipedia")
        tts.save("wikipedia.mp3")
        playsound("wikipedia.mp3")
        webbrowser.open("https://wikipedia.org")
        os.remove("wikipedia.mp3")
    else:
        print("I dont understand this")


def start():
    print("If you need me only say my Name")
    print("I am called Mondi")
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
                if (recog == "Monday Monday" ):
                    print("starting...")
                    mondai()
                    start()  
                if (recog == "Monday Monday Monday" ):
                    print("starting...")
                    mondai()
                    start()      
                if (recog == "1D" ):
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
                if (recog == "deep" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "one day" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "Sunday" ):
                    print("starting...")
                    mondai()
                    start()
                if (recog == "mundane" ):
                    print("starting...")
                    mondai()
                    start()
            except sr.UnknownValueError:
                print("try again")
                start()
start()