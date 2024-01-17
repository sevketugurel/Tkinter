from tkinter import *

class Oscars:
    def __init__(self) -> None:
        window = Tk()
        window.title("Kıtalar-Ülkeler")

        Label(window, text="KITALAR", borderwidth=2, relief=SOLID).grid(row=0, column=0, sticky=N)
        Label(window, text="ULKELER", borderwidth=2, relief=SOLID).grid(row=0, column=1, sticky=N)

        infile = open("Veriler/dunya.txt", "r")  # "/Veriler/dunya.txt" yerine "veriler/dunya.txt" kullanıldı
        self.kıtalar = {line.split(",")[1].rstrip() for line in infile}
        infile.close()

        self._Liste = list(self.kıtalar)
        self._Liste.sort()  # Sıralı listeyi elde etmek için sort() fonksiyonu kullanılmalıdır

        self.kıtaKümesi = StringVar()
        self.Kitalar = Listbox(window, width=10, height=len(self._Liste), listvariable=self.kıtaKümesi)
        self.Kitalar.grid(row=1, column=0, sticky=N)
        self.kıtaKümesi.set(tuple(self._Liste))
        self.Kitalar.bind("<<ListboxSelect>>", self.ulkeler)

        self.yscroll = Scrollbar(window, orient=VERTICAL)
        self.yscroll.grid(row=1, column=1, sticky=W)

        self.ulkelerListesi = Listbox(window, width=10, height=len(self._Liste), yscrollcommand=self.yscroll.set)
        self.ulkelerListesi.grid(row=1, column=1, sticky=E)

        self.yscroll["command"] = self.ulkelerListesi.yview
        window.mainloop()

    def ulkeler(self, e):
        self.ulkelerListesi.delete(0, END)

        kita = self.Kitalar.get(self.Kitalar.curselection())

        ulkelerListesi = [line.split(',')[0].rstrip() for line in open("veriler/dunya.txt", 'r')
                          if kita == line.split(",")[1].rstrip()]

        for ulke in ulkelerListesi:
            self.ulkelerListesi.insert(END, ulke)


if __name__ == "__main__":
    app = Oscars()
