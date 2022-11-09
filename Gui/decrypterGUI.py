from tkinter import *
# master = Tk()

# Import decode modules from decode.py
import Algo.decode as decode 
# Import files modules from files.py
import File.files as files

def openDecrypter(master):
    decryptorWindow = Toplevel(master)
    decryptorWindow.geometry("600x600")
    decryptorWindow.title("Decrypter")
    decryptorWindow.configure(background="orange")

    TextEntryLabel = Label(decryptorWindow, text="Enter Text to Decrypt", font=("Arial", 13), bg="orange", fg="black")
    TextEntryLabel.grid(row=0, column=1, pady = 8)

    TextEntry = Entry(decryptorWindow, width=50, borderwidth=5)
    TextEntry.grid(row=2, column=1, padx=120, pady=15)

    # Event listener: Click Button trigger
    def trigger(): 
        s = TextEntry.get()
        decodedString = decode.decodeMorse(s)

        # Console log the string and write in the output file.
        print('The String is :', decodedString)
        files.writeOutput(decodedString)
        
        # Write the decrypted text in the text file. 
        files.writeEnglish(decode.decodeMorse(files.readMorse()))
        
        return decodedString

    def showDecryptedText():
        decryptedText = trigger()
        DecryptedTextLabel = Label(decryptorWindow, text=decryptedText, font=("Arial", 25), bg="white", fg="black")
        DecryptedTextLabel.place(height=174, relwidth=0.304, relx=0.348, rely=0.4)

    DecryptButton = Button(decryptorWindow, text="Decrypt",command=showDecryptedText)
    DecryptButton.place(relx=0.45, rely=0.15)

    outputLabel = Label(decryptorWindow, text="Decrypted Text",font=("Arial", 20), bg="orange", fg="black")
    outputLabel.place(height=174, relwidth=0.304, relx=0.348, rely=0.2)

    OutputMessage = Message(decryptorWindow, text="", bg="white", fg="black")
    OutputMessage.place(height=174, relwidth=0.6, relx=0.2, rely=0.4)
