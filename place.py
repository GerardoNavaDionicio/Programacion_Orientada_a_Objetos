from tkinter import *
from tkinter import font,messagebox

class Promedio():
    def __init__(self):
        self.principal = Tk()
        self.poo = DoubleVar()
        self.so = DoubleVar()
        self.prom = DoubleVar()

        self.principal.title('Calificaciones')
        self.lbPOO = Label(self.principal,text="POO")
        self.lbPOO.place(x = 10,y = 10)
        self.entryPOO = Entry(self.principal,textvariable=self.poo,bd=5)
        self.entryPOO.place(x = 60,y = 10)

        self.lbSO = Label(self.principal,text= "SO")
        self.lbSO.place(x = 10,y = 50)
        self.entrySO = Entry(self.principal,textvariable=self.so,bd=5)
        self.entrySO.place(x = 60,y = 50)

        self.lbPromedio = Label(self.principal,text="Promedio")
        self.lbPromedio.place(x = 10,y = 150)
        self.entryPromedio = Entry(self.principal,textvariable=self.prom,bd=5)
        self.entryPromedio.place(x = 80,y = 150)
        self.btCalcular = Button(self.principal,text="Obtener promedio",bg='pink',command=self.promedio)
        self.btCalcular.place(x = 80,y = 100)
        self.principal.geometry("250x250+10+10")
        fuente = font.Font(family="Helvetica",size=12,weight="bold")

        self.entryPOO.bind('<FocusIn>',self.borrar1)
        self.entrySO.bind('<FocusIn>',self.borrar2)
        self.principal.mainloop()

    def promedio(self):
        p = (self.poo.get()+self.so.get())/2
        self.prom.set(p)
        print("El promedio es: ",p)
        if p > 9.0:
            messagebox.showinfo('Becas','Tienes beca')
        else:
            messagebox.showinfo('Becas','Lo sentimos no tienes beca')
    
    def borrar1(self,evento):
        self.entryPOO.delete(0,END)
    
    def borrar2(self,evento):
        self.entrySO.delete(0,END)
def main():
    mi_prom = Promedio()
    return 0
if __name__=="__main__":
    main()
