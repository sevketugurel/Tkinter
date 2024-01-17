from tkinter import *
import os

class Fakulteler:
    def __init__(self) -> None:
        pencere = Tk()
        pencere.title("Fakülte-Bölüm-Öğretim Elemanları")

        Label(text="Fakülte", borderwidth=2, relief=SOLID).grid(row=0, column=0, sticky=N)
        Label(text="Bölüm", borderwidth=2, relief=SOLID).grid(row=0, column=1, sticky=N)
        Label(text="Öğretim Elemanı", borderwidth=2, relief=SOLID).grid(row=0, column=2, sticky=N)

        dosya_yolu = "/Volumes/SSDsandisk/Masaüstü/Ders Notları/2.Sınıf(çoğusu driveda)/Nesne çalışma soruları/kodlar/Final/fakültelerVeri.txt"
        with open(dosya_yolu, "r") as dosya:
            self.data = [satır.split(",") for satır in dosya]

        self.FakülteListesi = sorted(list(set([line[0].rstrip() for line in self.data])))

        self.fakülteListbox = Listbox(pencere, width=15, height=len(self.FakülteListesi))
        self.fakülteListbox.grid(row=1, column=0, sticky=N)
        self.fakülteListbox.bind("<<ListboxSelect>>", self.bölümler)

        for fakulte in self.FakülteListesi:
            self.fakülteListbox.insert(END, fakulte)

        yscroll = Scrollbar(pencere, orient=VERTICAL)
        yscroll.grid(row=1, column=2, sticky=NSEW)

        self.bölümKümesiListbox = Listbox(pencere, width=10, height=len(self.FakülteListesi), yscrollcommand=yscroll.set)
        self.bölümKümesiListbox.grid(row=1, column=1, sticky=N)
        self.bölümKümesiListbox.bind("<<ListboxSelect>>", self.ögrtEleman)
        yscroll["command"] = self.bölümKümesiListbox.yview

        self.ElemanlarKümesiListbox = Listbox(pencere, width=15, height=len(self.FakülteListesi), yscrollcommand=yscroll.set)
        self.ElemanlarKümesiListbox.grid(row=1, column=2, sticky=NE) 
        yscroll["command"] = self.ElemanlarKümesiListbox.yview

        pencere.mainloop()

    def bölümler(self, e):
        # Bölüm listesini temizle
        self.bölümKümesiListbox.delete(0, END)

        Fakulte = self.fakülteListbox.get(self.fakülteListbox.curselection())
        bölüm = [line[1].rstrip() for line in self.data if Fakulte == line[0].rstrip()]

        for b in bölüm:
            self.bölümKümesiListbox.insert(END, b)

        # Öğretim elemanları listesini temizle
        self.ElemanlarKümesiListbox.delete(0, END)

    def ögrtEleman(self, e):

        bölüm = self.bölümKümesiListbox.get(self.bölümKümesiListbox.curselection())
        bölümdekElemanlar = [line[2].rstrip() for line in self.data if bölüm == line[1].rstrip()]

        for el in bölümdekElemanlar:
            self.ElemanlarKümesiListbox.insert(END, el)

if __name__ == "__main__":
    app = Fakulteler()
