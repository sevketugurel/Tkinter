from tkinter import Tk, Listbox, StringVar

window = Tk()

conOflstRates = StringVar()
lstRates = Listbox(window, height=5, width=4, exportselection=1, listvariable=conOflstRates)
lstRates.grid(row=3, column=0) 

# StringVar'ı güncelleme örneği
conOflstRates.set(["Item 1", "Item 2", "Item 3"])

window.mainloop()
