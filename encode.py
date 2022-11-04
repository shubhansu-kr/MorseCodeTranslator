# s -> string to be encoded into morse code

morseDictionary = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
             "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
             "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", " ": "  "}


def encodeMorse(s):
    print(s)
    s = s.lower()
    print(s)
    encodedString = ''
    for c in s: 
        encodedString += morseDictionary[c]
    return encodedString


# CheckPoint: TestFunction
# s = 'Shubhansu Kumar Singh'
# print(encodeMorse(s))