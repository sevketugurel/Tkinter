from tkinter import *

def checkAnswer():
    s = sehir.index(SehirListbox.get(SehirListbox.curselection()))
    p = plaka.index(plakaListbox.get(plakaListbox.curselection()))

    if s == p:
        entCevap.set("Doğru Cevap")
    else:
        entCevap.set("Yanlış Cevap")

window = Tk()
window.title("ŞEHİR-PLAKA")

Label(window, text="Şehir").grid(row=0, column=0, sticky=NSEW)
Label(window, text="Plaka").grid(row=0, column=1, sticky=NSEW)

sehir = ["Kırıkkale", "Ankara", "Trabzon", "İzmir", "İstanbul"]
plaka = ["71", "06", "61", "35", "34", "01"]
sıralıPlaka = list(plaka)
sıralıPlaka.sort()

SehirlerSV = StringVar()
SehirListbox = Listbox(window, listvariable=SehirlerSV, width=14, height=6, exportselection=0)
SehirListbox.grid(row=1, column=0, padx=10)
SehirlerSV.set(tuple(sehir))

PlakaSV = StringVar()
plakaListbox = Listbox(window, listvariable=PlakaSV, height=6, width=5)
plakaListbox.grid(row=1, column=1, padx=10)
PlakaSV.set(tuple(sıralıPlaka))

kontrolButton = Button(window, text="Sonuç Göster", command=checkAnswer)
kontrolButton.grid(row=2, column=2, columnspan=2, sticky=E)

Label(window, text="CEVAP: ").grid(row=3, column=0, sticky=E)

entCevap = StringVar()
cevapsonuc = Entry(window, state="readonly", width=10, textvariable=entCevap)  # "readonly" yerine "normal"
cevapsonuc.grid(row=3, column=1, sticky=W)

window.mainloop()
