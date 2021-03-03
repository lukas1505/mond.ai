import speech_recognition as sr
import time
import subprocess
import webbrowser

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

def speak(recog):
    if (recog == "Hallo"):
        print("Hallo Sir wie kann ich Ihnen helfen")
    elif (recog == "bist du da"):
        print("Ich bin immer hier an deiner Seite")
    elif (recog == "wie geht es dir"):
        print("Mir geht immer gut")
    elif (recog == "bist du gut gelaunt"):
        print("Das bin ich doch immer")
    elif (recog == "was machst du heute noch"):
        print("Ich bleibe immer hier in deinem Rechner")
    elif (recog == "kannst du singen"):
        print("Nein das kann ich leider nicht")
    elif (recog == "halt's Maul"):
        print("Alles klar wie Sie wünschen")
    elif (recog == "kannst du kochen"):
        print("Nein das kann ich leider auch nicht, aber ich kann dir gerne dabei helfen")
    elif (recog == "magst du mich"):
        print("Natürlich")
    elif (recog == "was geht"):
        print("Wenn du willst kann ich dir gerne sagen was du heute noch unternhemen könntest")
    elif (recog == "nein doch nicht"):
        print("Alles klar verstanden")
    elif (recog == "was jetzt"):
        print("Jetzt können wir zwei uns unterhalten")
    elif (recog == "was treibst du"):
        print("ich mache immer nur das was du mir sagst")
    elif (recog == "kannst du mir helfen"):
        print("Wenn du mir sagst wobei helfe ich doch gerne")
    elif (recog == "du kannst einfach nichts"):
        print("ich habe verstanden")
    elif (recog == "hilfst du mir jetzt"):
        print("wobei kann ich dir denn helfen")
    elif (recog == "mach mal irgendwas"):
        print("was denn")
    elif (recog == "wer hat dich gemacht"):
        print("ich wurde von LP erschaffen")
    elif (recog == "danke"):
        print("ich habe verstanden")
        start()
    else:
        functions(recog)

def functions(recog):
    print("functions processing")
    if (recog == "wie ist das Wetter"):
        print("hier ist das Wetter")
        webbrowser.open("https://www.wetter.com/deutschland/EUDE.html")
    elif (recog == "öffne instagram"):
        print("hier ist instagram")
        webbrowser.open_new_tab("https://instagram.com")
    elif (recog == "öffne youtube"):
        print("ich öffne youtube")
        webbrowser.open_new_tab("https://youtube.com")
    elif (recog == "öffne facebook"):
        print("ich öffne facebook")
        webbrowser.open_new_tab("https://facebook.com")
    elif (recog == "was kann ich drucken"):
        print("hier ein paar Ideen")   
        webbrowser.open_new_tab("https://www.thingiverse.com")
    elif (recog == "öffne google"):
        print("ich öffne Google")
        webbrowser.open_new_tab("https://google.com")
    else:
        print("Es tut mir leid das kann ich nocht nicht aber ich lerne noch")


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
                    mondai()
                    start()
            except sr.UnknownValueError:
                print("Das habe ich leider nicht verstanden")
                start()
start()