from tkinter import *
principal = Tk()
contador = 0
for r in range(6):
    for c in range(6):
        contador=contador + 1
        Button(principal,text=str(contador),borderwidth=1).grid(row=r,column=c)

principal.mainloop()