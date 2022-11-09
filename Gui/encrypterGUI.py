from tkinter import *
# master = Tk()

# Import encode module and files module
import Algo.encode as encode 
import File.files as files

def openEncrypter(master):

    encryptorWindow = Toplevel(master)
    encryptorWindow.geometry("600x600")
    encryptorWindow.title("Encrypter")
    encryptorWindow.configure(background="orange")

    TextEntryLabel = Label(encryptorWindow, text="Enter Text to Encrypt",font=("Arial", 13), bg="orange", fg="black")
    TextEntryLabel.grid(row=0, column=1, pady = 8)

    TextEntry = Entry(encryptorWindow, width=50, borderwidth=5)
    TextEntry.grid(row=2, column=1, padx=120, pady=15)


    def trigger(): 
        s = TextEntry.get()
        encodedString = encode.encodeMorse(s)

        # Console log the string and write in the output file.
        print('The Morse Code is :', encodedString)
        files.writeOutput(encodedString)
        
        # Write the decrypted text in the text file. 
        files.writeEnglish(encode.encodeMorse(files.readMorse()))
        
        return encodedString

    def showEncryptedText():
        encryptedText = trigger()
        EncryptedTextLabel = Label(encryptorWindow, text=encryptedText,font=("Arial", 25) , bg="white", fg="black")
        EncryptedTextLabel.place(height=174, relwidth=0.304, relx=0.348, rely=0.4)

    EncryptButton = Button(encryptorWindow, text="Encrypt",command=showEncryptedText)
    EncryptButton.place(relx=0.45, rely=0.15)

    outputLabel = Label(encryptorWindow, text="Encrypted Text",font=("Arial", 20), bg="orange", fg="black")
    outputLabel.place(height=174, relwidth=0.304, relx=0.348, rely=0.2)
    OutputMessage = Message(encryptorWindow, text="",bg="white", fg="black")
    OutputMessage.place(height=174, relwidth=0.6, relx=0.2, rely=0.4)
