import pickle

def yazma(dosya):
    devamMı = "y"
    
    while devamMı.lower() == "y":
        veriler = {}  # Her öğrenci için yeni bir sözlük oluşturuluyor.
        veriler["isim"] = input("Lütfen İsminizi Giriniz: ")
        veriler["ogrenciNo"] = int(input("Lütfen öğrenci no giriniz: "))
        veriler["notOrtalaması"] = float(input("Lütfen not ortalaması giriniz: "))
        pickle.dump(veriler, dosya)
        print("Verileriniz yazıldı...")
        devamMı = input("Devam etmek istiyor musunuz ? [y/n]: ").lower()

def display_data(inputfile):
    dosya_sonu = False
    while not dosya_sonu:
        try:
            person = pickle.load(inputfile)
            print("isim: ", person["isim"])
            print("ogrenciNo : ", person["ogrenciNo"])
            print("notOrtalaması : ", person["notOrtalaması"])
            print()
        except EOFError:
            dosya_sonu = True

dosya = open("veriler.dat", "wb")
yazma(dosya)
dosya.close()

dosya = open("veriler.dat", "rb")
display_data(dosya)
dosya.close()
