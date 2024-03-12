import os
import string

def split(word):
    return [char for char in word]

Zeichen = ["@","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","1","2","3","4","5","6","7","8","9","0","!","§","$","%","&","/","{","(","[","]",")","=","}","?","+","*","~","#","-","_",":",";",".","ä","ü","ö","<",">","€"," "]
lookup = {ch: i for i, ch in enumerate(Zeichen)}

def main():
    Eingabetext = input("Der Text: ")
    Eingabepassword = input("Das Passwort: ")
    Eingabeoption = input("[1] Encrypt \n[2] Decrypt\n")
    
    encrypt_decrypt(Eingabetext, Eingabepassword, Eingabeoption)
    
def encrypt_decrypt(text, password, option):
   
    Password = password
    Text = text
    Outputlist = []

    PwNum = 0

    for x in Text:
        wert = lookup[x]
        print(wert)

        if option == "1":
            wert = wert + ord(Password[PwNum])
        elif option == "2":
            wert = wert - ord(Password[PwNum])

        wert = wert % len(Zeichen)

        if 0 <= wert < len(Zeichen):
            x = Zeichen[wert]

        PwNum = (PwNum + 1) % len(Password)

        Outputlist.append(x)

    Output = "".join(Outputlist)

    print(Output)

main()
exit()

