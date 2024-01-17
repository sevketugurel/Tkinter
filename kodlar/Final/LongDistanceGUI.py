import tkinter
import tkinter.messagebox

class LongDistanceGUI:
    def __init__(self) -> None:
        self.main_window = tkinter.Tk()
        
        self.topFrame = tkinter.Frame(self.main_window)
        self.midFrame = tkinter.Frame(self.main_window)
        self.bottomFrame = tkinter.Frame(self.main_window)

        self.rbvar = tkinter.IntVar()

        self.rbvar.set(1)

        self.radiobutton1 = tkinter.Radiobutton(self.topFrame,text="Gündüz (06.00-17.59)",variable=self.rbvar,value=1)
        self.radioButton2 = tkinter.Radiobutton(self.midFrame,text="Akşam (18.00-23-59)",variable = self.rbvar,value=2)
        self.raidoButton3 = tkinter.Radiobutton(self.bottomFrame,variable = self.rbvar,text="Gece(00.00-5.59)",value=3)
        self.radiobutton1.pack()
        self.radioButton2.pack()
        self.raidoButton3.pack()

        self.minutesFrame = tkinter.Label(self.bottomFrame,text="Kaç dakika konuştunuz:")
        self.minutesEntry = tkinter.Entry(self.bottomFrame,width=10)

        self.minutesFrame.pack(side="left")
        self.minutesEntry.pack(side="left")

        self.displayButton = tkinter.Button(self.bottomFrame,text="Ücreti Göster",command=self.calculate)
        self.quitButton = tkinter.Button(self.bottomFrame,text="ÇIKIŞ",command=self.main_window.destroy)

        self.displayButton.pack(side="left")
        self.quitButton.pack(side="left")

        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        tkinter.mainloop()
    def calculate(self):
        minutes = float(self.minutesEntry.get())

        if self.rbvar.get() == 1:
            rate = 0.07
        elif self.rbvar.get() == 2:
            rate = 0.12
        elif self.rbvar.get() == 3:
            rate = 0.05
        
        charges = minutes * rate

        tkinter.messagebox.showinfo("Toplam Ücret", "Ödeyeceğiniz Ücret = TL " + format(charges, ".2f"))


longDist = LongDistanceGUI()