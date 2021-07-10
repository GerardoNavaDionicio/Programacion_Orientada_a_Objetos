from tkinter import*
from tkinter import font
from tkinter import messagebox
import time 
class App():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("estaciones del Year")
        self.principal.geometry('700x400')
        fuente =  font.Font(size=10,weight='bold')
        self.opcion = IntVar()
        Label(self.principal,text='Estacion mas gustada?',font=fuente).pack(anchor='w')
        Radiobutton(self.principal,text='Primavera',variable=self.opcion,value=1,command=self.seleccionar).pack()
        Radiobutton(self.principal,text='Verano',variable=self.opcion,value=2,command=self.seleccionar).pack()
        Radiobutton(self.principal,text='Otoño',variable=self.opcion,value=3,command=self.seleccionar).pack()
        Radiobutton(self.principal,text='Invierno',variable=self.opcion,value=4,command=self.seleccionar).pack()

        self.pantalla=Label(self.principal)
        self.pantalla.pack()
        Button(self.principal,text="Reiniciar",command=self.reiniciar).pack()
        self.principal.mainloop()
    def seleccionar(self):
        if self.opcion.get()==1:
            res = messagebox.showinfo('Estachien favorita','Buena eleccion')
        else :
            messagebox.showinfo('No es tan agradable')
        if self.opcion.get()==2:
            res = messagebox.askyesno('Estachien favorita','Are you Sure?')
            time.sleep(1)
            if res==True: 
                messagebox.showinfo('Estacion favorita','Te gusta el sol')
            else:
                messagebox.showinfo('Estachien favorita','Hace mucho calor')
        if self.opcion.get()==3:
            res = messagebox.askyesno('Estachien favorita','Are you Sure?')
            time.sleep(1)
            if res==True: 
                messagebox.showinfo('Estacion favorita','Bonito Atardecer')
            else:
                messagebox.showinfo('Estachien favorita','Mucho viento')
        else:
            res = messagebox.askyesno('Estachien favorita','Are you Sure?')
            time.sleep(1)
            if res==True: 
                messagebox.showinfo('Estacion favorita','Navidad')
            else:
                messagebox.showinfo('Estachien favorita','Mucho Frio')
    def reiniciar(self):
        self.opcion.set(None)
        self.pantalla.config(text='')
def main():
    app=App()
    return 0
if __name__=='__main__':
    main()