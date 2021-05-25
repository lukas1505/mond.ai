import tkinter as tk

root = tk.Tk()
root.geometry("640x480")
root.resizable(0, 0)
root.config(background = "whitesmoke")

def click(): 
    print("Function Executed")
    input = firstinput.get()
    print(input)
    file1 = open("pathtospotify.txt", "a")
    file1.write(str(input))


headline = tk.Label(root, text="Mondi Startprogramm")
headline.config(bg = "#861205", height = "2", width = "100", font = ("Arial", "20"))
headline.pack()

firstlabel = tk.Label(root,font=('Arial', 14), text="Path to Spotify")
firstlabel.pack()
firstinput = tk.Entry(root,font=('Arial', 14), width="40")
firstinput.pack()

firstbutton = tk.Button(root, font=('Arial', 14), text='submit', command = click)
firstbutton.pack()

footer = tk.Label(root, font=('Arial', 14), text="by Lukas Paul")
footer.config(bg = "#861205", height = "1", width = "100", font= ("Arial", "15"))
footer.pack( side = "bottom")

root.mainloop()