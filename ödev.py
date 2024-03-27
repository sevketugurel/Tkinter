from tkinter import *
import math
import sympy as sp

pencere = Tk()
pencere.title("Nümerik Analiz Hesaplama Arayüzü")

Label(pencere, text="Fonksiyonunuzu giriniz:").grid(row=0, column=0, pady=1, sticky=SE)
Label(pencere, text="Epsilon Değeri:").grid(row=1, column=0, pady=1, sticky=SE)
Label(pencere, text="Başlangıç Değeri 1:").grid(row=2, column=0, pady=1, sticky=SE)
Label(pencere, text="Başlangıç Değeri 2:").grid(row=3, column=0, pady=1, sticky=SE)
Label(pencere, text="Max İterasyon Sayısı:").grid(row=4, column=0, pady=1, sticky=SE)

fonksiyonVar = StringVar()
epsilonVar = StringVar()
baslangic1Var = StringVar()
baslangic2Var = StringVar()
iterasyonVar = StringVar()

Entry(pencere, textvariable=fonksiyonVar).grid(row=0, column=1)
Entry(pencere, textvariable=epsilonVar).grid(row=1, column=1)
Entry(pencere, textvariable=baslangic1Var).grid(row=2, column=1)
Entry(pencere, textvariable=baslangic2Var).grid(row=3, column=1)
Entry(pencere, textvariable=iterasyonVar).grid(row=4, column=1)

# RadioButton'lar
fonksiyonSecimi = StringVar()
fonksiyonSecimi.set(None)

def secim():
    print(fonksiyonSecimi.get())

Label(pencere, text="Metodu seçiniz:").grid(row=5, column=0)
Radiobutton(pencere, text="Newton", variable=fonksiyonSecimi, value="Newton", command=secim).grid(row=5, column=1)
Radiobutton(pencere, text="Kiriş", variable=fonksiyonSecimi, value="Kiriş", command=secim).grid(row=5, column=2)
Radiobutton(pencere, text="Sekant", variable=fonksiyonSecimi, value="Sekant", command=secim).grid(row=5, column=3)

# Çıktı text widget'ı
Label(pencere, text="Çıktı:").grid(row=6, column=1, pady=1, sticky=E)
cikti_text = Text(pencere, height=10, width=40)
cikti_text.grid(row=6, column=2, padx=5, pady=5)

def hesapla():
    if fonksiyonSecimi.get() == "Newton":
        # Newton yöntemi hesaplama
        newtonYontemi()
        
    elif fonksiyonSecimi.get() == "Kiriş":
        # Kiriş yöntemi hesaplama
        kirisYontemi()
        
    # Sekant yöntemi hesaplama
    elif fonksiyonSecimi.get() == "Sekant":
        sekantYontemi()

def newtonYontemi():
    baslangic = float(baslangic1Var.get())
    epsilon = float(epsilonVar.get())
    maks_iterasyon = int(iterasyonVar.get())

    x = sp.symbols('x')
    fonksiyon = sp.sympify(fonksiyonVar.get())
    fonksiyon_turev = sp.diff(fonksiyon, x)

    def f(x_degeri):
        return float(fonksiyon.subs(x, x_degeri))

    def f_turev(x_degeri):
        return float(fonksiyon_turev.subs(x, x_degeri))

    def newton_raphson_yontemi(baslangic, epsilon=0.001, maksIterasyon=2):
        x0 = baslangic
        iterasyon = 0
        cikti_text.delete(1.0, END)  # Önceki çıktıyı temizle
        while iterasyon < maksIterasyon:
            x1 = x0 - f(x0) / f_turev(x0)
            cikti_text.insert(END, f"{iterasyon + 1}. iterasyon değeri = {x1}\n")
            if abs(f(x1)) < epsilon:
                return x1
            x0 = x1
            iterasyon += 1
        return float('NaN')

    kok = newton_raphson_yontemi(baslangic, epsilon, maks_iterasyon)
    if not math.isnan(kok):
        cikti_text.insert(END, f"Kök: {kok}\n")
    else:
        cikti_text.insert(END, f"Kök: {kok}\n")
        cikti_text.insert(END, "Yöntem belirlenen tolerans değerine ulaşmadı veya maksimum iterasyon sayısına erişti.\n")

def kirisYontemi():
    baslangic1 = float(baslangic1Var.get())
    baslangic2 = float(baslangic2Var.get())
    epsilon = float(epsilonVar.get())
    maks_iterasyon = int(iterasyonVar.get())

    x = sp.symbols('x')
    fonksiyon = sp.sympify(fonksiyonVar.get())
    fonksiyon_turev = sp.diff(fonksiyon, x)
    
    def f(x_degeri):
        return float(fonksiyon.subs(x, x_degeri))

    def kiris_yontemi(x0, x1, epsilon=0.001, maksIterasyon=100):
        cikti_text.delete(1.0, END)  
        iterasyon = 0
        hata = float("inf")
        x2 = float("nan")

        while iterasyon < maksIterasyon and hata > epsilon:
            if abs(f(x1) - f(x0)) < epsilon:
                print("Yöntem uygun bir sonuç üretmedi.")
                return float("nan")

            if f(x1) - f(x0) == 0:  # Kontrol eklendi
                print("Bölme hatası: sıfıra bölme hatası!")
                return float("nan")
            cikti_text.insert(END, f"{iterasyon + 1}. iterasyon değeri = {x1}\n")
            x2 = x1 - ((x1 - x0) * f(x0)) / (f(x1) - f(x0))
            hata = abs(f(x2))

            # Hata hesaplamasında x2 değeri kullanılıyor
            x0 = x1
            x1 = x2

            iterasyon += 1

        if iterasyon == maksIterasyon:
            print("Maksimum iterasyon sayısına ulaşıldı.")
            return float("nan")

        # Kok değeri x2 olarak
        return x2

    kok = kiris_yontemi(baslangic1, baslangic2, epsilon, maks_iterasyon)
    if not math.isnan(kok):
        cikti_text.insert(END, f"Kök: {kok}\n")
    else:
        cikti_text.insert(END, f"Kök: {kok}\n")
        cikti_text.insert(END, "Yöntem belirlenen tolerans değerine ulaşmadı veya maksimum iterasyon sayısına erişti.\n")
            
def sekantYontemi():
    cikti_text.delete(1.0, END)  
    baslangic1 = float(baslangic1Var.get())
    baslangic2 = float(baslangic2Var.get())
    epsilon = float(epsilonVar.get())
    maks_iterasyon = int(iterasyonVar.get())

    x = sp.symbols('x')
    fonksiyon = sp.sympify(fonksiyonVar.get())

    def f(x_degeri):
        return float(fonksiyon.subs(x, x_degeri))

    def sekant_yontemi(x0, x1, epsilon, maksIterasyon):
        iterasyon = 0
        x2 = 0
        f_x0 = f(x0)
        f_x1 = f(x1)

        while iterasyon < maksIterasyon:
            x2 = x1 - (f_x1 * (x0 - x1)) / (f_x0 - f_x1)
            if abs(f(x2)) < epsilon:
                return x2
            x0 = x1
            x1 = x2
            f_x0 = f_x1
            f_x1 = f(x1)
            cikti_text.insert(END, f"{iterasyon + 1}. iterasyon değeri = {x1}\n")
            iterasyon += 1

        return math.nan

    def sekant():
        kok = sekant_yontemi(baslangic1, baslangic2, epsilon, maks_iterasyon)
        if not math.isnan(kok):
            cikti_text.insert(END, f"Kök: {kok}\n")
        else:
            cikti_text.insert(END, f"Kök: {kok}\n")
            cikti_text.insert(END, "Yöntem belirlenen tolerans değerine ulaşmadı veya maksimum iterasyon sayısına erişti.\n")

    sekant()

Button(pencere, text="Hesapla", command=hesapla).grid(row=6, column=0, pady=5)
pencere.mainloop()


