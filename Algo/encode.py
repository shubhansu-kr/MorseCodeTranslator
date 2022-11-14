# s -> string to be encoded into morse code

morseDictionary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
             "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
             "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}


def encodeMorse(s):
    s = s.lower()
    encodedString = ''
    for c in s: 
        if (c in morseDictionary.keys()): 
            encodedString += (morseDictionary[c] + ' ')
        else: 
            encodedString += c            
    return encodedString


# CheckPoint: TestFunction
# s = 'Shubhansu Kumar Singh'
# print(encodeMorse(s))