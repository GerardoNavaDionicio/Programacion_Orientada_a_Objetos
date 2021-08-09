from tkinter import *
from tkinter import font ,messagebox

""" class ScrolbarVertical():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Scrollbar V")
        self.scrollbar = Scrollbar(self.principal)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.principal, yscrollcommand=self.scrollbar.set)

        for i in range(100):
            self.listbox.insert("end", str(i))
        self.listbox.pack(side="left", fill="both")
        self.scrollbar.config(command=self.listbox.yview)
        self.principal.mainloop()

if __name__=='__main__':
    app = ScrolbarVertical() """

class ScrolbarHorizontal():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Scrollbar VyH")
        self.principal.geometry('250x200')
        self.scrollbar = Scrollbar(self.principal, orient='horizontal')
        self.scrollbar.pack(side="bottom", fill="x")
        self.scrollbarV = Scrollbar(self.principal, orient='vertical')
        self.scrollbar.pack(side="right", fill="y")

        self.text = Text(self.principal, wrap = "none", xscrollcommand=self.scrollbar.set, yscrollcommand=self.scrollbarV.set)

        for i in range(20):
            self.text.insert(END,"Texto de ejemplo para el scrollbar horizontal\n")
        self.text.pack(side="top", fill="x")

        self.scrollbar.config(command=self.text.xview)
        self.scrollbarV.config(command=self.text.yview)
        
        self.principal.mainloop()

if __name__=='__main__':
    app = ScrolbarHorizontal()