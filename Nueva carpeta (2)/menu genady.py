from tkinter import *
from tkinter import messagebox
from tkinter import ttk,font
import getpass
class App():
    def __init__(self):
        self.principal = Tk()
        self.principal.title('Login')
        self.principal.resizable(0,0)
        fuente = font.Font(weight='bold')

        self.contenerFrame = ttk.Frame(self.principal,borderwidth = 2,relief = "sunken",padding= (10,10))
        self.lbUser = ttk.Label(self.contenerFrame,text="Username: ",font=fuente,padding=(5,5))
        self.lbPass = ttk.Label(self.contenerFrame,text="Password: ",font=fuente,padding=(5,5))
        
        self.user = StringVar()
        self.passw = StringVar()
        self.user.set(getpass.getuser())

        self.tbUser = ttk.Entry(self.contenerFrame,textvariable=self.user,width=30)
        self.tbPass = ttk.Entry(self.contenerFrame,textvariable=self.passw,show='*',width=30,)
        self.separador1 = ttk.Separator(self.contenerFrame,orient=HORIZONTAL)
        self.btAceptar = ttk.Button(self.contenerFrame,text='Aceptar',padding=(5,5),command=self.aceptar)
        self.btCancelar = ttk.Button(self.contenerFrame,text='Cancelar',padding=(5,5),command=quit)

        self.contenerFrame.grid(column=0,row=0)
        self.lbUser.grid(column=0,row=0)
        self.tbUser.grid(column=1,row=0,columnspan=2)
        self.lbPass.grid(column=0,row=1)
        self.tbPass.grid(column=1,row=1,columnspan=2)
        self.separador1.grid(column=0,row=3,columnspan=3)
        self.btAceptar.grid(column=1,row=4)
        self.btCancelar.grid(column=2,row=4)
        self.tbUser.focus_set()
        self.tbPass.bind('Button-3>',self.solicitaPass)
        self.principal.mainloop()
    def solicitaPass(self,evento):
        self.passw.set("   ")
        messagebox.showwarning('Warning','Ingresa tu pass')


        

    def aceptar(self):
        if self.passw.get() == '123' and self.user.get() == 'GenaThink':
            messagebox.showinfo('Informacion','Acceso Correcto')
            print('Acceso correcto')
            print('Usuario: ',self.tbUser.get())
            print('Contraseña: ',self.tbPass.get())
        elif self.passw.get() == '123' and self.user.get() != 'GenaThink':
            messagebox.showinfo('Error','Nombre de usuario erroneo')
            print('Acceso denegado')
            print('Usuario: ',self.tbUser.get())
            print('Contraseña: ',self.tbPass.get())
        elif self.passw.get() != '123' and self.user.get() == 'GenaThink':
            messagebox.showinfo('Error','Contraseña erronea')
            print('Acceso denegado')
            print('Usuario: ',self.tbUser.get())
            print('Contraseña: ',self.tbPass.get())
        else:
            messagebox.showinfo('Error','Acceso Denegado')
            print('Acceso denegado')
            self.passw.set("")
            self.tbPass.focus_set()


def main():
    mi_App = App()
    return 0
if __name__=="__main__":
    main()