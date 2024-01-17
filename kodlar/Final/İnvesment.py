from tkinter import *

def calculate():
    # Listbox'tan seçilen faiz oranını al
    rate = lstRates.get(lstRates.curselection())
    
    # Karşılık gelen faiz oranını ondalık olarak atayın
    if rate == "2%":
        intRate = 0.02
    elif rate == "2.5%":
        intRate = 0.025
    elif rate == "3%":
        intRate = 0.03
    elif rate == "3.5%":
        intRate = 0.035
    elif rate == "4%":
        intRate = 0.04

    # Listbox'tan seçilen bileşik dönemleri al
    periods = lstPeriods.get(lstPeriods.curselection())
    
    # Yılda kaç bileşik dönem olduğunu belirlemek için karşılık gelen sayıyı atayın
    if periods == "yılda bir":
        n = 1 
    elif periods == "yarı yılda bir":
        n = 2
    elif periods == "üç aylık":
        n = 4
    elif periods == "aylık":
        n = 12
    elif periods == "haftalık":
        n = 52

    # Bileşik faiz formülünü kullanarak 5 yıl sonra yatırım miktarını hesaplayın
    amount = 10000 * (1 + intRate/n)**(5*n)

    # Hesaplanan miktarı görüntülemek için Entry widget'ında ayarlayın
    conOFentAmount.set("${0:,.3f}".format(amount))

# Ana pencereyi oluşturun
window = Tk() 
window.title("Yatırım")

# Daha iyi bir kullanıcı arayüzü için etiketler oluşturun ve yerleştirin
# Label(window, text="10.000$ Yatırım Yap").grid(row=0, column=1, pady=5)
Label(window, text="10.000$ Yatırım Yap", borderwidth=2, relief="solid").grid(row=0, column=1, pady=1)
Label(window, text="Faiz\nDönemleri:").grid(row=1, column=0, pady=5)
Label(window, text="Bileşik\nDönemleri:").grid(row=1, column=1, padx=10, pady=5)

# "Hesapla" düğmesini oluşturun ve calculate fonksiyonu ile ilişkilendirin
btnCalculate = Button(window, text="5 Yıl Sonraki\nMiktarı Hesapla", command=calculate)
btnCalculate.grid(row=3, column=2, padx=5, sticky=SE)

# Faiz oranları ve bileşik dönemleri için listeler oluşturun
conOflstRates = StringVar()
lstRates = Listbox(window, height=5, width=4, exportselection=0, listvariable=conOflstRates)
lstRates.grid(row=3, column=0)

conOflstPeriods = StringVar()
lstPeriods = Listbox(window, height=5, width=10, exportselection=0, listvariable=conOflstPeriods)
lstPeriods.grid(row=3, column=1)

# Hesaplanan miktarı görüntülemek için etiket ve giriş oluşturun
Label(window, text="5 yıl sonra miktar:").grid(row=4, column=0, pady=5, columnspan=2, sticky=E)

conOFentAmount = StringVar()
entAmount = Entry(window, textvariable=conOFentAmount, width=9, state="readonly")
entAmount.grid(row=4, column=2, padx=3, pady=5, )

# Listbox'lar için başlangıç değerlerini ayarlayın
conOflstRates.set(["2%", "2.5%", "3%", "3.5%", "4%","4.5%"])
conOflstPeriods.set(["yılda bir", "yarı yılda bir", "üç aylık", "aylık", "haftalık"])

# Ana olay döngüsünü başlatın
window.mainloop()
