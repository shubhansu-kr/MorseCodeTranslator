from tkinter import *

import Gui.decrypterGUI as decrypterGUI
import Gui.encrypterGUI as encrypterGUI

master = Tk()
master.geometry("600x600")
master.title("Morse Code Translator")
master.configure(background="orange")

def trigger1(): 
    encrypterGUI.openEncrypter(master)

def trigger2():
    decrypterGUI.openDecrypter(master)

TitleLabel = Label(master, text="Morse Code Translator", font=("Arial", 20), bg="orange")
TitleLabel.place(relx=0.28, rely=0.2)

Encodebtn = Button(master, text="Encrypt", font=("Arial", 20), bg="white", command=trigger1)
Encodebtn.place(relx=0.25, rely=0.4)

Decodebtn = Button(master, text="Decrypt", font=("Arial", 20), bg="white", command=trigger2)
Decodebtn.place(relx=0.60, rely=0.4)

mainloop()
