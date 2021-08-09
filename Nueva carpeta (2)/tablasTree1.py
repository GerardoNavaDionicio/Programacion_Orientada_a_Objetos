from tkinter import ttk
from tkinter import *
from tkinter import font,messagebox

class AppTree():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Celdas editable para BD")
        fuente = font.Font(size=10,weight='bold')

        self.columnas = ("Usuario","Contraseña","Correo")

        self.treeview = ttk.Treeview(self.principal,height=10,show = 'headings',column = self.columnas)
        self.treeview.column("Usuario",width=100,anchor='center')
        self.treeview.column("Contraseña",width=100,anchor='center')
        self.treeview.column("Correo",width=100,anchor='center')

        self.treeview.heading('Usuario',text='user')
        self.treeview.heading('Contraseña',text='password')
        self.treeview.heading('Correo',text='Email')
        self.treeview.pack(side=LEFT,fill=BOTH)

        self.usuarios = []
        for n in range(1,10):
            self.usuarios.append((f'Usuario {n}',f'Contraseña{n}',f'email{n}@example.com'))
        for usuario in self.usuarios:
            self.treeview.insert('',END,values=usuario)

        self.treeview.bind('<<TreeviewSelect>>',self.item_selected)
        self.treeview.grid(row=0,column=0,sticky='nsew')

        self.scrollbarV = ttk.Scrollbar(self.principal,orient='vertical',command=self.treeview.yview)
        self.treeview.configure(yscroll=self.scrollbarV.set)
        self.scrollbarV.grid(row=0,column=1,sticky='ns')

        self.nuevaF = Button(self.principal, text='Nuevo usuario',width=20,bg='blue',command=self.nuevaFila)
        self.nuevaF.grid(row=2,column=0,sticky='ns')

        self.treeview.bind('<Button-3>',self.eliminar)
        self.treeview.bind('<Button-2>',self.editar)
        

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        self.principal.mainloop()

    def item_selected(self,event):
        for selected_item in self.treeview.selection():
            item = self.treeview.item(selected_item)
            print(item)
            record = item['values']
            messagebox.showinfo('Datos',','.join(record))
    
    def nuevaFila(self):
        print('Ingresa aqui')
        nuevo = [('user','pass','email')]
        self.usuarios.append(nuevo)
        for usuario in nuevo:
            self.treeview.insert('',END,values=usuario)
        self.treeview.update()
        self.nuevaF.update()
    
    def eliminar(self,event):
        selected_item = self.treeview.selection()[0]
        item = self.treeview.item(selected_item)
        res = messagebox.askokcancel("Confirmacion","Deseas eliminar")
        if res == True:
            self.treeview.delete(selected_item)
            messagebox.showinfo('Confirmacion','Elemento eliminado')
            self.treeview.update()
    def editar(self,event):
        print('Editar')
        columna=''
        fila=''
        for item in self.treeview.selection():
            texto_item = self.treeview.item(item,"values")
            columna = self.treeview.identify_column(event.x)
            fila = self.treeview.identify_row(event.y)
            print(columna,fila)
        nColumna = int(str(columna).replace('#',''))
        nFila = int(str(fila).replace('I',''))
        print(nFila,nColumna)
        textEditar = Text(self.principal,width=10 + (nColumna -1) * 16,height=1)
        textEditar.place(x=16 + (nColumna - 1) * 130, y=6 + nFila * 20)

        def guardar():
            self.treeview.set(item,column=columna,value=textEditar.get(0.0,"end"))
            textEditar.destroy()
            self.btConfirmar.destroy()
        self.btConfirmar = ttk.Button(self.principal,text='OK',width=4,command=guardar)
        self.btConfirmar.place(x=90 + (nColumna - 1) * 242,y=2 + nFila * 20)
        
def main():
    app = AppTree()
    return 0

if __name__=='__main__':
    main()
