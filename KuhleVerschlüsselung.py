import os

def split(word):
    return [char for char in word] 

Zeichen = ["@","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","1","2","3","4","5","6","7","8","9","0","!","§","$","%","&","/","{","(","[","]",")","=","}","?","+","*","~","#","-","_",":",";",".","ä","ü","ö","<",">","€"," "]
lookup = {ch: i for i, ch in enumerate(Zeichen)}

def main():
    os.system("cls")
    print("[1] Load file")
    print("[2] Load from text")
    print("")
    Auswahl4 = input("[1] [2] [3]: ")

    os.system("cls")
    Password = input("Passwort: ")
    Password = split(Password)

    if Auswahl4 == "1":
        Filename = input("Filename: ")
        if not "." in Filename:
            Filename = Filename + ".txt"
        with open(Filename, "r") as file:
            Text = file.read()

    elif Auswahl4 == "2":
        Text = input("Text: ")
        Text = split(Text)

    elif Auswahl4 == "3":
        Text = os.popen("clip").read()


    Outputlist = []

    print("")
    print("[1] Verschlüsseln")
    print("[2] Entschlüsseln")
    print("")
    Auswahl = input("[1] [2]: ")
    os.system("cls")

    PwNum = 0

    for x in Text:
        wert = lookup[x]

        if Auswahl == "1":
            wert = wert + ord(Password[PwNum])
        elif Auswahl == "2":
            wert = wert - ord(Password[PwNum])

        wert = wert % len(Zeichen)

        if 0 <= wert < len(Zeichen):
            x = Zeichen[wert]

        PwNum = (PwNum + 1) % len(Password)

        Outputlist.append(x)

    Output = "".join(Outputlist)

    print("Output: " + Output )
    print("")
    print("[1] Save Output to file")
    print("[2] Run Programm again")
    print("[3] Quit")
    print("")

    Auswahl2 = input("[1] [2]: ")

    if Auswahl2 == "1":
        Filename = input("Filename: ")
        if not "." in Filename:
            Filename = Filename + ".txt"     
        with open(Filename, "w") as file:
            file.write(Output)

    elif Auswahl2 == "2":
        main()

    elif Auswahl2 == "3":
        exit()

    elif Auswahl2 == "4":
        print("Passwort:" + str(Password))
        print("Text: " + str(Text))
        print("Output: " + str(Output))
        input("")
        

    os.system("cls")


    print("")
    print("[1] Run Programm again")
    print("[2] Exit")
    print("")
    Auswahl3 = input("[1] [2]: ")
    print("")

    if Auswahl3 == "1":
        main()
    
    if Auswahl3 == "3":
        exit()

def encrypt_decrypt(text, password, encryption):
    if encryption.lower() == "encrypt":
        Auswahl = "1"
    elif encryption.lower() == "decrypt":
        Auswahl = "2"
    else:
        raise ValueError("Invalid encryption argument. Please use 'encrypt' or 'decrypt'.")

    Password = password
    Text = text
    Outputlist = []

    PwNum = 0

    for x in Text:
        wert = lookup[x]

        if Auswahl == "1":
            wert = wert + ord(Password[PwNum])
        elif Auswahl == "2":
            wert = wert - ord(Password[PwNum])

        wert = wert % len(Zeichen)

        if 0 <= wert < len(Zeichen):
            x = Zeichen[wert]

        PwNum = (PwNum + 1) % len(Password)

        Outputlist.append(x)

    Output = "".join(Outputlist)

    print(Output)

main()
# encrypt_decrypt("Hallo!","test","encrypt")
# encrypt_decrypt("5iHIL[","test","decrypt")
exit()
