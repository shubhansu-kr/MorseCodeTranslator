# File Handling for morse code translation 

# Take input from english txt
def readEnglish(): 
    f = open('english.txt', 'r')
    eng = f.read()
    f.close()
    return eng


# Write in english txt 
def writeEnglish(decodedMorse): 
    # Let decodedMorse be the required code 
    f = open('english.txt', 'w')
    f.write(decodedMorse)
    f.close()


# Take input from morse txt
def readMorse(): 
    f = open('morse.txt', 'r')
    morse = f.read()
    f.close()
    return morse


# Write in morse txt 
def writeMorse(encodedMorse):
    # Let encodedMorse be the required code 
    f = open('morse.txt', 'w')
    f.write(encodedMorse)
    f.close()

# Write in output txt 
def writeOutput(s):
    # Let encodedMorse be the required code 
    f = open('output.txt', 'w')
    f.write(s)
    f.close()
