import subprocess
import webbrowser

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
    elif (recog == "öffne googel"):
        print("ich öffne Googel")
        webbrowser.open_new_tab("https://google.com")
    else:
        print("Es tut mir leid das kann ich nocht nicht aber ich lerne noch")