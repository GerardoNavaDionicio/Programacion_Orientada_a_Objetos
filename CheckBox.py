from tkinter import*
from tkinter import font, messagebox

class App():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Coffe")
        self.principal.geometry('700x400')
        fuente =  font.Font(size=12,weight='bold')
        self.principal.config(bd=15)
        self.leche = IntVar()
        self.azucar = IntVar()
        self.imagen = PhotoImage(file='.\interfaz\GIF.gif')
        Label(self.principal,image=self.imagen).pack(side='left')
        self.frame=Frame(self.principal)
        self.frame.pack(side='left')
        Label(self.frame,text='tu cafe con?',font=fuente).pack(anchor='w')
        Checkbutton(self.frame,text='Con leche',variable=self.leche,onvalue=1,offvalue=0,font=fuente,command=self.seleccionar).pack(anchor='w')
        Checkbutton(self.frame,text="Con azucar",variable=self.azucar,onvalue=1,offvalue=0,font=fuente,command=self.seleccionar).pack(anchor='w')
        self.pantalla=Label(self.frame)
        self.pantalla.pack()
        self.principal.mainloop()

    def seleccionar(self):
        cadena= ''
        if (self.leche.get()):
            cadena += 'Con leche'
        else:
            cadena =+ 'Sin leche'
        if (self.azucar.get()):
                cadena += 'y azucar'
        else:
            cadena =+ "Sin azucar"
        fuente1 = font.Font(size=10,weight='bold')
        self.pantalla.config(text=cadena,font=fuente1,fg='blue')

def main():
    app= App()
    return 0
if __name__=='__main__':
    main()

        