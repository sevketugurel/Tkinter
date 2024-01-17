from tkinter import *


class Oscars:
    def __init__(self):
        window = Tk()
        window.title("Kıtalar-Ülkeler")
        Label(window, text="KITA").grid(row=0, column=0)
        Label(window, text="Ülkeler").grid(row=0, column=1)
        infile = open("veriler/dunya.txt", 'r')
        self.kıtaKume = {line.split(',')[1].rstrip() for line in infile}
        infile.close()
        self._L = list(self.kıtaKume)
        self._L.sort()
        
        self.KitaListesi = StringVar()
        self.Kitalar = Listbox(window, width=20, height=len(self._L), listvariable=self.KitaListesi)
        self.Kitalar.grid(row=1, column=0, padx=10,pady=10, sticky=N)
        self.KitaListesi.set(tuple(self._L))
        self.Kitalar.bind("<<ListboxSelect>>", self.ulkeler)

        yscroll = Scrollbar(window, orient=VERTICAL)
        yscroll.grid(row=1, column=2, sticky=NS)

        self.ulkeler = Listbox(window, width=25,height=len(self._L), yscrollcommand=yscroll.set)
        self.ulkeler.grid(row=1, column=1, padx=10,pady=10,sticky=NSEW)

        yscroll["command"] = self.ulkeler.yview

        window.mainloop()

    def ulkeler(self, e):
        self.ulkeler.delete(0, END)  # Önceki içeriği temizle

        kita = self.Kitalar.get(self.Kitalar.curselection())
        ulkeler_listesi = [line.split(",")[0] for line in open("veriler/dunya.txt", "r")
                           if line.split(",")[1].rstrip() == kita]

        for ulke in ulkeler_listesi:
            self.ulkeler.insert(END, ulke)


if __name__ == "__main__":
    app = Oscars()
