ilkDosya = input("Birinci Dosyanın tam adını giriniz: ")
ikinciDosyaAdı = input("İkinci Dosyanın Adini giriniz: ")


def kelimelere_ayir(dosyatxt):
    try:
        dosya = open(dosyatxt, 'r')
        cumle = dosya.readline()
        dosya.close()
        kelimeler = cumle.split()
        return set(kelimeler)  # kelimeleri teke indirdik

    except FileNotFoundError:
        print("Dosya bulunamadı")
    except Exception as err:
        print("Bir hata oluştu: " + str(err))


def hangileriIceriyor(kelimeKümesi1, kelimeKümesi2):
    farkliKelimeler = kelimeKümesi1.difference(kelimeKümesi2)
    return farkliKelimeler

dosya1 = "metin.txt"
dosya2 = "metin2.txt"

kelimekümesi1 = kelimelere_ayir(ilkDosya)
kelimekümesi2 = kelimelere_ayir(ikinciDosyaAdı)

yalnızBirdeOlanlar = hangileriIceriyor(kelimekümesi1,kelimekümesi2)
yalnızIkideOlanlar = hangileriIceriyor(kelimekümesi2,kelimekümesi1)

herİkisindeOlanlar = kelimekümesi1.intersection(kelimekümesi2)
print()
print("Birinci Dosyada olup ikinci dosyada olmayanlar: ")
for i in yalnızBirdeOlanlar:
    print(i)

print
print("ikinci Dosyada olup birinci dosyada olmayanlar: ")
for i in yalnızIkideOlanlar:
    print(i)

print
print("Her ikisinde de olanlar: ")
for i in herİkisindeOlanlar:
    print(i)
