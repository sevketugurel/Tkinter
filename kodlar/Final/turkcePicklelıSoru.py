from tkinter import *
import pickle

class Ulkeler:
    def __init__(self) -> None:
        # Tkinter penceresini oluştur
        pencere = Tk()
        pencere.title("Ülkeler")

        # Pickle kullanarak veri sözlüğünü dosyadan yükle
        with open("/Users/sevketugurel/Desktop/Ders Notları/Ders Notları 2.Sınıf(çoğusu driveda)/Nesne çalışma soruları/kodlar/Final/UNdict2.dat", "rb") as dosya:
            self._veriSozlugu = pickle.load(dosya)
        
        # Ülkeler listesini oluştur ve sırala
        self._ulkeListesi = list(self._veriSozlugu.keys())
        self._ulkeListesi.sort()

        # Tkinter StringVar kullanarak listbox içeriğini güncelle
        self._ulkeStringVar = StringVar()

        # Dikey scrollbar oluştur
        dikey_scroll = Scrollbar(pencere, orient=VERTICAL)
        dikey_scroll.grid(row=0, column=1, rowspan=7, sticky=NS)

        # Listbox oluştur ve dikey scrollbar'ı ayarla
        self._ulkeListebox = Listbox(pencere, listvariable=self._ulkeStringVar, yscrollcommand=dikey_scroll.set)
        self._ulkeListebox.grid(row=0, column=0, rowspan=7, sticky=NS)

        # Listbox içeriğini güncelle ve Listbox seçim olayını bağla
        self._ulkeStringVar.set(tuple(self._ulkeListesi))
        self._ulkeListebox.bind("<<ListboxSelect>>", self.veriGoster)

        # Dikey scrollbar'ı Listbox ile bağla
        dikey_scroll["command"] = self._ulkeListebox.yview

        # Etiketler ve giriş kutularını oluştur
        Label(pencere, text="Kıta").grid(row=0, column=2, sticky=E, padx=4)
        Label(pencere, text="Nüfus").grid(row=1, column=2, sticky=E, padx=4)
        Label(pencere, text="Alan (km²)").grid(row=2, column=2, sticky=E, padx=4)

        self._kitaStringVar = StringVar()
        entKita = Entry(pencere, width=15, state="readonly", textvariable=self._kitaStringVar)
        entKita.grid(row=0, column=3, sticky=W)

        self._nuksStringVar = StringVar()
        nuksEntry = Entry(pencere, state="readonly", width=15, textvariable=self._nuksStringVar)
        nuksEntry.grid(row=1, column=3, sticky=W)

        self.alanStringVar = StringVar()
        alanEntry = Entry(pencere, width=15, state="readonly", textvariable=self.alanStringVar)
        alanEntry.grid(row=2, column=3, sticky=W)

        # Tkinter penceresini başlat
        pencere.mainloop()

    def veriGoster(self, olay):
        # Seçilen ülkenin bilgilerini gerekli giriş kutularına yerleştir
        ulke = self._ulkeListebox.get(self._ulkeListebox.curselection())
        self._kitaStringVar.set(self._veriSozlugu[ulke]["cont"])
        self._nuksStringVar.set("{0:,.0f}".format(1000000 * float(self._veriSozlugu[ulke]["popl"])))
        self.alanStringVar.set("{0:,.2f}".format(self._veriSozlugu[ulke]["area"]))

# Ulkeler sınıfından bir örnek oluştur
uygulama = Ulkeler()

# Eğer bu dosya doğrudan çalıştırılıyorsa, uygulamayı başlat
if __name__ == "__main__":
    uygulama
