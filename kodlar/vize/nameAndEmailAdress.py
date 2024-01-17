def menu():
    print()
    print("1- isim ve email ekle")
    print("2- isim ve email düzenle")
    print("3- isim ve email sil")
    print()

    secim = int(input("Yukarıdaki seçeneklerden birisini seçiniz: "))
    dataDict={}

    if secim == 1:
        nameAndEmailAdd(dataDict)
    elif secim == 2:
        displayData("emailNameData.txt")
        print()
        editNameEmail(dataDict)
    elif secim == 3:
        displayData("emailNameData.txt")
        print()
        delNameEmail(dataDict)

    # en sonda dosyaya ekleyim
    inputFile = open("emailNameData.txt","a")
    dosyayaYaz(inputFile,dataDict)

def dosyayaYaz(inputfile,dataDict):
    try:
        for key,value in dataDict.items():
            inputfile.write(f"{key} : {value}")
        print("verileriniz yazıldı")
    except Exception as err:
        print(err)
    finally:
        inputfile.close()

def nameAndEmailAdd(dictNameEmail, input_file):
    isim = input("İsim: ")
    email = input("Email: ")
    dictNameEmail[isim] = email
    input_file.write(f"isim:{isim}: {email}\n")


def editNameEmail(dataDict):
    isim = input("Değiştireceğiniz yeni email adresinin sahibini yazınız: ")
    if isim in dataDict:
        dataDict[isim] = input("Değiştireceğiniz yeni email adresini yazınız : ")
    else:
        print(f"{isim} adında bir kayıt bulunamadı.")


def delNameEmail(dictNameEmail):
    delIsim = input("bilglerini silmek istediğiniz ismi yazınız")
    if delIsim in dictNameEmail:
        del dictNameEmail[delIsim]
    else:
        print(f"{delIsim} adında bir kayıt bulunamadı.")
def displayData(inputFile):
    outputData = open(inputFile,"r")
    datalar = outputData.readlines()
    print(datalar)
# Programı çalıştırmak için
menu()
