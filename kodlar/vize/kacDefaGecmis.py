kelimeler={}
try:
    file = open("deneme.txt","r")
    readDosyaSplit = file.read().split()
    for kelime in readDosyaSplit:

        if kelime in kelimeler:
            kelimeler[kelime] += 1 
        else:
            kelimeler[kelime] = 1

except FileNotFoundError:
    print("Dosya bulunamadı!!!")
finally:
    file.close()

file2 = open("yazi.txt","w")
for kelime,deger in kelimeler.items():
    file2.write(f"{kelime}:{deger}\n")

file2.close()

