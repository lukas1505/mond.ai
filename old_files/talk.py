from websites import functions
from start_mondai import start

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