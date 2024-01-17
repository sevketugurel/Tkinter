from tkinter import *

class Oscars:
    def __init__(self) -> None:
        window = Tk()
        window.title("Yıllara Göre Oscarlar")

        caption = "Yıl [1928-2013]"
        Label(window, text=caption).grid(row=0, column=0)

        self.yılGirisi = StringVar()
        self.entYıl = Entry(window, width=5, textvariable=self.yılGirisi).grid(row=0, column=1, sticky=W)

        caption = "En iyi Film"
        bulBtn = Button(window, text=caption, command=self.DisplayFilm)
        bulBtn.grid(row=1, column=1)

        Label(window, text="Film").grid(row=2, column=0, sticky=E)
        Label(window, text="Tür").grid(row=3, column=0, sticky=E)

        self.filmEnt = StringVar()
        self.ReadFilmEnt = Entry(window, state="readonly", textvariable=self.filmEnt).grid(row=2, column=1, padx=5, sticky=W)
        self.TürEnt = StringVar()
        self.ReadTurEnt = Entry(window, textvariable=self.TürEnt, state="readonly")
        self.ReadTurEnt.grid(row=3, column=1, sticky=W, padx=5)

        self.data = self.read_data_from_file("Oscars_cleaned.txt")

    def DisplayFilm(self):
        year = int(self.yılGirisi.get())
        if 1928 <= year <= 2013:
            film, tur = self.data[year - 1928]
            self.filmEnt.set(film)
            self.TürEnt.set(tur)
        else:
            self.filmEnt.set("Geçersiz Yıl")
            self.TürEnt.set("Geçersiz Yıl")

    def read_data_from_file(self, filename):
        data = []
        with open(filename, "r") as infile:
            lines = infile.readlines()
            for i in range(0, len(lines), 3):
                if i + 2 < len(lines):  # Kontrol eklendi
                    year = int(lines[i].strip())
                    film = lines[i + 1].strip()
                    tur = lines[i + 2].strip()
                    data.append((film, tur))
        return data

# Boş satırları temizle
with open("/Volumes/SSDsandisk/Masaüstü/Ders Notları/2.Sınıf(çoğusu driveda)/Nesne çalışma soruları/kodlar/Final/Oscars.txt", "r") as infile:
    lines = infile.readlines()

cleaned_lines = [line.strip() for line in lines if line.strip()]
with open("Oscars_cleaned.txt", "w") as outfile:
    outfile.write("\n".join(cleaned_lines))

if __name__ == "__main__":
    app = Oscars()
    mainloop()
