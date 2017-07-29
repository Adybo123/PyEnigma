#PyEnigma
#Python Enigma Emulator
#
#By Adam Soutar

#Import sys as some OSes require us to give an exit code
import sys

#Alphabet - CONSTANT
#Do not change
global Alphabet
Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

Rotor1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
Rotor2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
Rotor3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
Rotor4 = list('ESOVPZJAYQUIRHXLNFTGKDCMWB')
Rotor5 = list('VZBRGITYUPSDNHLXAWMJQOFECK')

#Use to set your rotors and their order
global Rotors
Rotors = [Rotor1, Rotor2, Rotor3]

#Reflectors
ReflectorA = list('EJMZALYXVBWFCRQUONTSPIKHGD')
ReflectorB = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
ReflectorC = list('FVPJIAOYEDRZXWGCTKUQSBNMHL')
ReflectorBThin = list('ENKQAUYWJICOPBLMDXZVFTHRGS')
ReflectorCThin = list('RDOBJNTKVEHMLFCWZAXGYIPSUQ')

#Use this for the offset of your rotors on start
global RotorPosition
RotorPosition = [0, 0, 0]

#Use this to set your reflector
global Reflector
Reflector = ReflectorA

#Plugboard, this corresponds with the alphabet
#If you don't know what you're doing, don't change it
global Plugboard
Plugboard = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

#Collumns, this variable goes unused here,
#but it can be referenced by another script using the API
global Collumns
Collumns = [Alphabet, [Rotors], Reflector]

def correctForOffset():
    #Correct the rotors for the starting offset
    for I in range(0, len(Rotors)):
        #If bigger than 26, correct since 27 = 1, 28 = 2, et cetera
        while (RotorPosition[I]>26):
            RotorPosition[I] = RotorPosition[I] - 26
        #For range to our offset, right loop shift the array
        for x in range(0, RotorPosition[I]):
            Rotors[I].insert(0, Rotors[I][len(Rotors[I]) - 1])
            Rotors[I].pop(len(Rotors[I]) - 1)

def enigmaStatus():
    #Prints the status of the Enigma machine, such as the rotors and positions
    print("PyEnigma Status:")
    for i in range(0, len(Rotors)):
        print("Rotor " + str(i + 1) + ": " + str(Rotors[i]))
    print("Rotor offsets: " + str(RotorPosition))
    print("Plugboard: " + str(Plugboard))
    print("Reflector: " + str(Reflector))

def printHelp():
    #Print the help prompt
    print("""
=Help=
Commands:
Help - Shows this menu
Exit/Quit - Quits the script
Settings - Shows settings such as rotors and their order
Stat/Status - Shows the status of the rotors, such as their positions
Detect - Detect the Enigma machine type

To encipher a message, simply type a message which isn't a command.

Notes:
The Enigma cipher should be used for proof of concept and very-basic
message protection. Do not use this cipher to hold sensitive data!
And don't forget - You can use PyEnigma as an import library.
    """)

def enigChar(charIn):
    #Ciphers a character
    #Cache start char
    originalChar = charIn
    #Pass through plugboard
    charIn = Plugboard[Alphabet.index(charIn)]
    #Rotate rotors
    doRotorTurn = 0
    for i in range(0, len(Rotors) - 1):
        if (doRotorTurn == i):
            RotorPosition[i] = RotorPosition[i] + 1
            Rotors[i].insert(0, Rotors[i][len(Rotors[i]) - 1])
            Rotors[i].pop(len(Rotors[i]) - 1)
            if (RotorPosition[i]>26):
                if (i!=len(Rotors) - 1):
                    RotorPosition[i] = 0
                    doRotorTurn = i + 1
                else:
                    for p in RotorPosition:
                        p = 0
    #Pass through the rotors in order
    for R in Rotors:
        charIn = R[Alphabet.index(charIn)]
    #Reflect using reflector
    charIn = Reflector[Alphabet.index(charIn)]
    #Build reverse order rotor array
    reverseRotors = []
    for R in Rotors:
        reverseRotors.insert(0,R)
    #Pass through rotors in reverse order
    for R in reverseRotors:
        charIn = Alphabet[R.index(charIn)]
    #Pass through alphabet again
    charIn = Plugboard[Alphabet.index(charIn)]
    return charIn

def enigAskString():
    #Ask for a string then enigma it unless it is 'EXIT' or 'QUIT'
    global enigRun
    inEnig = input("Enigma >")
    inEnig = inEnig.upper()
    endStr = ""
    for i in inEnig:
        if (inEnig=="QUIT") or (inEnig=="EXIT"):
            enigRun = False
        elif (inEnig=="HELP"):
            printHelp()
            break;
        elif (inEnig=="DETECT"):
            print(detectEnigma())
            break;
        elif (inEnig=="STAT") or (inEnig=="STATUS"):
            enigmaStatus()
            break;
        else:
            if (i.upper()!=i.lower()):
                endStr = endStr + str(enigChar(i))
            else:
                endStr = endStr + i
    print(endStr)

def detectEnigma():
    #Detect the type of enimga machine based on settings
    enigType = ""
    if (len(Rotors)==3):
        if (Plugboard!=Alphabet):
            enigType = "Luftwaffe/Wehrmacht - Drei Walzenlage"
        else:
            enigType = "Commercial Enigma I"
    elif (len(Rotors)==4):
        enigType = "Kriegsmarine - Vier Walzenlage"
    else:
        enigType = "None - Custom setup"
    return enigType

if __name__ == "__main__":
    #Unnessesary extravagance
    print("""
======================
PyEnigma

Python Enimga Emulator
Written by Adam Soutar
======================

Defaulting to settings in script
Type 'Help' for commands
    """)

    print("Detected enigma type: " + detectEnigma())
    print("")
    #Main progam loop and exit code
    global enigRun
    enigRun = True
    correctForOffset()
    while (enigRun==True):
        enigAskString()
    print("End of Enigma program...")
    sys.exit(0)
