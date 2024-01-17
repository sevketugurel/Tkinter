codes = {'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '&', 'D': '*', 'd': '^', 'E': '!',
         'e': '+', 'F': '?', 'f': '~', 'G': '>', 'g': '<', 'H': '|', 'h': '=', 'I': '(', 'i': ')',
         'J': '{', 'j': '}', 'K': '[', 'k': ']', 'L': ':', 'l': ';', 'M': ',', 'm': '.', 'N': '/',
         'n': '_', 'O': '-', 'o': '1', 'P': '2', 'p': '3', 'Q': '4', 'q': '5', 'R': '6', 'r': '7',
         'S': '8', 's': '0', 'T': 'a', 't': 'b', 'U': 'c', 'u': 'd', 'V': 'e', 'v': 'f', 'W': 'g',
         'w': 'h', 'X': 'i', 'x': 'j', 'Y': 'k', 'y': 'l', 'Z': 'm', 'z': 'n'}

def encrypted(dosya):
    encryptStr = ""
    try:
        file  = open(dosya,"r")
        fileReadSplit = file.readlines()
        for kelime in fileReadSplit:
            for harf in kelime:
                encryptStr += codes.get(harf,f"{harf}")
            encryptStr += " " # boşluk ekledim ki kelimeler birbirine karışmasın
    except FileNotFoundError:
        print("Dosya bulunamadı !!!")
    finally:
        file.close()     
    # yazma İşlemi
    yazma("encyrptedFile.txt",encryptStr)

def decrypted(dosya):
    
    decryptedStr =""

    try:
        file = open(dosya,'r')
        fileReadLines = file.readlines()
        for kelime in fileReadLines:

            for harf in kelime:
                
                for key,value in codes.items():
                    if value == harf:
                         decryptedStr += key
                         break
            decryptedStr += " "
    except FileNotFoundError:
        print("Dosya bulunmadı !")
    finally:
        file.close
    yazma("decrypted.txt",decryptedStr)

# chatin 
def decrypt_file(input_file, codes):
    try:
        file = open(input_file, 'r')
        encrypted_content = file.read()

        decrypted_content = ''
        for char in encrypted_content:
            for key, value in codes.items():
                if char == value:
                    decrypted_content += key
                    break
            else:
                decrypted_content += char

    except FileNotFoundError:
        print(f'Error: File not found - {input_file}')
    yazma("decyrpted.txt",decrypted_content)
    




def yazma(dosya,metin):
    writeFile = open(dosya,"w")
    writeFile.write(metin)
    writeFile.close()
                    
# Usage 
decrypt_file('encyrptedFile.txt', codes)
encrypted("deneme.txt")
#decrypted("encyrptedFile.txt")