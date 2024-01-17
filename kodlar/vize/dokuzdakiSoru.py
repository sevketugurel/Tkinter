
def satırSatırOkuma(dosya):
    dictWord = {}
    bulunduguSatır = 1

    line = dosya.readline()

    while line:
        lineSplit = line.split()

        for word in lineSplit:
            # dictte varsa ve key değerinde bulunduğu satır numarası yoksa
            if word in dictWord and (f"{bulunduguSatır}" not in dictWord[word] ): 
                dictWord[word] += f"{bulunduguSatır} "
            else:
                dictWord[word] = f"{bulunduguSatır} "
        
        bulunduguSatır += 1
        line = dosya.readline()  

    return dictWord

def txtYazmak(dictWord):
    file = open("index.txt", "w")
    for key, value in dictWord.items():
        yazı = f"{key}:{value}\n"
        file.write(yazı)

dosya = open("metin.txt", 'r')
dictWord = satırSatırOkuma(dosya)
txtYazmak(dictWord)

dosya.close()  
