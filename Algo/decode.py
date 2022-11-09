# Decoding

morseDictionary = {".-": "a", "-...": "b",  "-.-.": "c", "-..": "d",  ".": "e",  "..-.": "f",  "--.": "g",  "....": "h", "..": "i", ".---": "j",
                   "-.-": "k", ".-..": "l", "--": "m",  "-.": "n",  "---": "o",  ".--.": "p",  "--.-": "q",  ".-.": "r",  "...": "s",  "-": "t",
                   "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", " ": ""}

def decodeMorse(s): 
    words = s.split('  ')
    decodedString = ''
    for i in words: 
        letters = i.split() 
        temp = ''
        for j in letters: 
            if (j in morseDictionary.keys()):
                temp += morseDictionary[j]
        decodedString += (temp + ' ')
    return decodedString


# CheckPoint: TestFunction
# s = '.--. -.-- - .... --- -.  -.-. .-.. .- ... ...'
# print(decodeMorse(s))