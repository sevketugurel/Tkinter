from tkinter import *
import pickle

class Nations:
    def __init__(self) -> None:
        window = Tk()
        window.title("Nations")  # Pencere başlığı eklendi.

        # with open("/Veriler/UNdict.dat", "rb") as file:
        #     self._dictVeri = pickle.load("/Veriler/UNdict.dat","rb")  # Eski hatalı kod
        with open("/Users/sevketugurel/Desktop/Ders Notları/Ders Notları 2.Sınıf(çoğusu driveda)/Nesne çalışma soruları/kodlar/Final/UNdict2.dat", "rb") as file:
            self._dictVeri = pickle.load(file)  # Dosya nesnesi eklenerek pickle.load düzeltildi.
        
        # self._listVeri = list((self._dictVeri).keys())
        self._listVeri = list(self._dictVeri.keys())
        # self._nationSort = self._listVeri.sort()  # Eski hatalı kod
        self._listVeri.sort()  # _nationSort yerine _listVeri kullanıldı.

        self._conOFlstNotions = StringVar()

        yscroll = Scrollbar(window, orient=VERTICAL)
        yscroll.grid(row=0, column=1, rowspan=7, sticky=NS)

        # self._lstNotions = Listbox(window, listvariable=self._nationSort, yscrollcommand=yscroll)  # Eski hatalı kod
        self._lstNotions = Listbox(window, listvariable=self._conOFlstNotions, yscrollcommand=yscroll.set)
        self._lstNotions.grid(row=0, column=0, rowspan=7, sticky=NS)

        # self._conOFlstNotions.set(tuple(self._nationSort))  # Eski hatalı kod
        self._conOFlstNotions.set(tuple(self._listVeri))  # _nationSort yerine _listVeri kullanıldı.
        # self._lstNotions.bind("<<ListboxSelecet", self.displayData)  # Eski hatalı kod
        self._lstNotions.bind("<<ListboxSelect>>", self.displayData)  # Komut adı düzeltildi.
        # yscroll["command"] = YView  # Eski hatalı kod
        yscroll["command"] = self._lstNotions.yview  # YView yerine self._lstNotions.yview düzeltildi.

        Label(window, text="Continent").grid(row=0, column=2, sticky=E, padx=4)
        Label(window, text="Population").grid(row=1, column=2, sticky=E, padx=4)
        Label(window, text="Area (sq.mt)").grid(row=2, column=2, sticky=E, padx=4)

        self._conOFentContinent = StringVar()
        entContinent = Entry(window, width=15, state="readonly", textvariable=self._conOFentContinent)
        entContinent.grid(row=0, column=3, sticky=W)

        self._conOFPopulation = StringVar()
        populasyonEntry = Entry(window, state="readonly", width=15, textvariable=self._conOFPopulation)
        populasyonEntry.grid(row=1, column=3, sticky=W)

        self.alanStringi = StringVar()
        alanEntry = Entry(window, width=15, state="readonly", textvariable=self.alanStringi)
        alanEntry.grid(row=2, column=3, sticky=W)

        window.mainloop()

    def displayData(self, e):
        nation = self._lstNotions.get(self._lstNotions.curselection())
        self._conOFentContinent.set(self._dictVeri[nation]["cont"])
        self._conOFPopulation.set("{0:,.0f}".format(1000000 * float(self._dictVeri[nation]["popl"])))
        self.alanStringi.set("{0:,.2f}".format(self._dictVeri[nation]["area"]))

app = Nations()

if __name__ == "__main__":
    app