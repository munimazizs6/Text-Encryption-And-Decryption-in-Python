# Encryption and Decryption
# By Munim Aziz Shaikh

def encryption(text):
    text_code = [" " for i in range(len(text))]

    for x in range(len(text)):
        if(text[x] == "A" or text[x] == "a"):
            text_code[x] = "0"
        elif(text[x] == "B" or text[x] == "b"):
            text_code[x] = "1"
        elif(text[x] == "C" or text[x] == "c"):
            text_code[x] = "2"
        elif(text[x] == "D" or text[x] == "d"):
            text_code[x] = "3"
        elif(text[x] == "E" or text[x] == "e"):
            text_code[x] = "4"
        elif(text[x] == "F" or text[x] == "f"):
            text_code[x] = "5"
        elif(text[x] == "G" or text[x] == "g"):
            text_code[x] = "6"
        elif(text[x] == "H" or text[x] == "h"):
            text_code[x] = "7"
        elif(text[x] == "I" or text[x] == "i"):
            text_code[x] = "8"
        elif(text[x] == "J" or text[x] == "j"):
            text_code[x] = "9"
        elif(text[x] == "K" or text[x] == "k"):
            text_code[x] = "10"
        elif(text[x] == "L" or text[x] == "l"):
            text_code[x] = "11"
        elif(text[x] == "M" or text[x] == "m"):
            text_code[x] = "12"
        elif(text[x] == "N" or text[x] == "n"):
            text_code[x] = "13"
        elif(text[x] == "O" or text[x] == "o"):
            text_code[x] = "14"
        elif(text[x] == "P" or text[x] == "p"):
            text_code[x] = "15"
        elif(text[x] == "Q" or text[x] == "q"):
            text_code[x] = "16"
        elif(text[x] == "R" or text[x] == "r"):
            text_code[x] = "17"
        elif(text[x] == "S" or text[x] == "s"):
            text_code[x] = "18"
        elif(text[x] == "T" or text[x] == "t"):
            text_code[x] = "19"
        elif(text[x] == "U" or text[x] == "u"):
            text_code[x] = "20"
        elif(text[x] == "V" or text[x] == "v"):
            text_code[x] = "21"
        elif(text[x] == "W" or text[x] == "w"):
            text_code[x] = "22"
        elif(text[x] == "X" or text[x] == "x"):
            text_code[x] = "23"
        elif(text[x] == "Y" or text[x] == "y"):
            text_code[x] = "24"
        elif(text[x] == "Z" or text[x] == "z"):
            text_code[x] = "25"
        else:
            text_code[x] = " "
    
    for y in range(len(text)):
        if(text_code[y] != " "):
            text_code[y] = str((7* int(text_code[y]) +3) % 26)
    
    for z in range(len(text_code)):
        if(text_code[z] == "0"):
            text_code[z] = "A"
        elif(text_code[z] == "1"):
            text_code[z] = "B"
        elif(text_code[z] == "2"):
            text_code[z] = "C"
        elif(text_code[z] == "3"):
            text_code[z] = "D"
        elif(text_code[z] == "4"):
            text_code[z] = "E"
        elif(text_code[z] == "5"):
            text_code[z] = "F"
        elif(text_code[z] == "6"):
            text_code[z] = "G"
        elif(text_code[z] == "7"):
            text_code[z] = "H"
        elif(text_code[z] == "8"):
            text_code[z] = "I"
        elif(text_code[z] == "9"):
            text_code[z] = "J"
        elif(text_code[z] == "10"):
            text_code[z] = "K"
        elif(text_code[z] == "11"):
            text_code[z] = "L"
        elif(text_code[z] == "12"):
            text_code[z] = "M"
        elif(text_code[z] == "13"):
            text_code[z] = "N"
        elif(text_code[z] == "14"):
            text_code[z] = "O"
        elif(text_code[z] == "15"):
            text_code[z] = "P"
        elif(text_code[z] == "16"):
            text_code[z] = "Q"
        elif(text_code[z] == "17"):
            text_code[z] = "R"
        elif(text_code[z] == "18"):
            text_code[z] = "S"
        elif(text_code[z] == "19"):
            text_code[z] = "T"
        elif(text_code[z] == "20"):
            text_code[z] = "U"
        elif(text_code[z] == "21"):
            text_code[z] = "V"
        elif(text_code[z] == "22"):
            text_code[z] = "W"
        elif(text_code[z] == "23"):
            text_code[z] = "X"
        elif(text_code[z] == "24"):
            text_code[z] = "Y"
        elif(text_code[z] == "25"):
            text_code[z] = "Z"
        else:
            text_code[z] = " "
    return text_code

def decryption(text):
    text_code = [" " for i in range(len(text))]

    for x in range(len(text)):
        if(text[x] == "A" or text[x] == "a"):
            text_code[x] = "0"
        elif(text[x] == "B" or text[x] == "b"):
            text_code[x] = "1"
        elif(text[x] == "C" or text[x] == "c"):
            text_code[x] = "2"
        elif(text[x] == "D" or text[x] == "d"):
            text_code[x] = "3"
        elif(text[x] == "E" or text[x] == "e"):
            text_code[x] = "4"
        elif(text[x] == "F" or text[x] == "f"):
            text_code[x] = "5"
        elif(text[x] == "G" or text[x] == "g"):
            text_code[x] = "6"
        elif(text[x] == "H" or text[x] == "h"):
            text_code[x] = "7"
        elif(text[x] == "I" or text[x] == "i"):
            text_code[x] = "8"
        elif(text[x] == "J" or text[x] == "j"):
            text_code[x] = "9"
        elif(text[x] == "K" or text[x] == "k"):
            text_code[x] = "10"
        elif(text[x] == "L" or text[x] == "l"):
            text_code[x] = "11"
        elif(text[x] == "M" or text[x] == "m"):
            text_code[x] = "12"
        elif(text[x] == "N" or text[x] == "n"):
            text_code[x] = "13"
        elif(text[x] == "O" or text[x] == "o"):
            text_code[x] = "14"
        elif(text[x] == "P" or text[x] == "p"):
            text_code[x] = "15"
        elif(text[x] == "Q" or text[x] == "q"):
            text_code[x] = "16"
        elif(text[x] == "R" or text[x] == "r"):
            text_code[x] = "17"
        elif(text[x] == "S" or text[x] == "s"):
            text_code[x] = "18"
        elif(text[x] == "T" or text[x] == "t"):
            text_code[x] = "19"
        elif(text[x] == "U" or text[x] == "u"):
            text_code[x] = "20"
        elif(text[x] == "V" or text[x] == "v"):
            text_code[x] = "21"
        elif(text[x] == "W" or text[x] == "w"):
            text_code[x] = "22"
        elif(text[x] == "X" or text[x] == "x"):
            text_code[x] = "23"
        elif(text[x] == "Y" or text[x] == "y"):
            text_code[x] = "24"
        elif(text[x] == "Z" or text[x] == "z"):
            text_code[x] = "25"
        else:
            text_code[x] = " "
    
    for y in range(len(text)):
        if(text_code[y] != " "):
            text_code[y] = str((15* (int(text_code[y]) -3)) % 26)
    
    for z in range(len(text_code)):
        if(text_code[z] == "0"):
            text_code[z] = "A"
        elif(text_code[z] == "1"):
            text_code[z] = "B"
        elif(text_code[z] == "2"):
            text_code[z] = "C"
        elif(text_code[z] == "3"):
            text_code[z] = "D"
        elif(text_code[z] == "4"):
            text_code[z] = "E"
        elif(text_code[z] == "5"):
            text_code[z] = "F"
        elif(text_code[z] == "6"):
            text_code[z] = "G"
        elif(text_code[z] == "7"):
            text_code[z] = "H"
        elif(text_code[z] == "8"):
            text_code[z] = "I"
        elif(text_code[z] == "9"):
            text_code[z] = "J"
        elif(text_code[z] == "10"):
            text_code[z] = "K"
        elif(text_code[z] == "11"):
            text_code[z] = "L"
        elif(text_code[z] == "12"):
            text_code[z] = "M"
        elif(text_code[z] == "13"):
            text_code[z] = "N"
        elif(text_code[z] == "14"):
            text_code[z] = "O"
        elif(text_code[z] == "15"):
            text_code[z] = "P"
        elif(text_code[z] == "16"):
            text_code[z] = "Q"
        elif(text_code[z] == "17"):
            text_code[z] = "R"
        elif(text_code[z] == "18"):
            text_code[z] = "S"
        elif(text_code[z] == "19"):
            text_code[z] = "T"
        elif(text_code[z] == "20"):
            text_code[z] = "U"
        elif(text_code[z] == "21"):
            text_code[z] = "V"
        elif(text_code[z] == "22"):
            text_code[z] = "W"
        elif(text_code[z] == "23"):
            text_code[z] = "X"
        elif(text_code[z] == "24"):
            text_code[z] = "Y"
        elif(text_code[z] == "25"):
            text_code[z] = "Z"
        else:
            text_code[z] = " "
    return text_code

def main():
    print("\n**************************************** SIMPLE FILE ENCRYPTION AND DECRYPTION ****************************************")
    print("\n***************************************************** WELCOME *********************************************************")
    ead2()

def ead2():
    print("\nPress 1: if you want to do encryption or Press 2: if you want to do decryption or Press 3: if you want to do encryption and decryption")
    n = int(input("Enter an Option: "))
    if(n == 1):
        text = input("Enter your Text: ")
        encryptedtext = encryption(text)
        print(f"Encrypted Text: {encryptedtext}")
        print("Encryption Done!")
        main()
    elif(n == 2):
        text = input("Enter your Text: ")
        decryptedtext = decryption(text)
        print(f"Decrypted Text: {decryptedtext}")
        print("Decryption Done!")
        main()
    elif(n == 3):
        text = input("Enter your Text: ")
        encryptedtext = encryption(text)
        print(f"Encrypted Text: {encryptedtext}")
        decryptedtext = decryption(encryptedtext)
        print(f"Decrypted Text: {decryptedtext}")
        print("Encryption and Decryption Done!")
        main()
    else:
        print("Please enter a correct option!")
        ead2()

main()