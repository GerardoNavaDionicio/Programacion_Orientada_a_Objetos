from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QLineEdit,QCalendarWidget
from PyQt5 import uic, QtCore
import sys
import webbrowser

archivo = uic.loadUiType(".\interfacez\menu.ui")[0]

class ClsPasaTiempos(QMainWindow,archivo):
    def __init__(self,parent=None):
        super(QMainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Pasatiempos")
        self.save.clicked.connect(self.guardar)

        #menu
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionSalir.triggered.connect(self.cerrar)
        self.actionAcerca.triggered.connect(self.acerca)


    def abrir(self):
        respuesta = QMessageBox.quesion(self,'Mensale','Quieres abrir un archivo?')
        if respuesta == QMessageBox.Yes:
            nombre = input('Ingresa el nombre del archivo:')
            try:
                f = open(nombre + '.txt','w')
                f.write(self.textEdit.toPlainText())
                f.close()
            except:
                informacion=QMessageBox.critical(self,"Error",'no se puede abrir',QMessageBox.Ok)
                f.closed()
    def cerrar(self):
        QApplication.quit()

    def acerca(self):
        webbrowser.open("https://www.python.org/");
#stateChanged.connect(self.item_checado)

    def item_checado(self,lista1,lista2):
        if self.viajes.isChecked():
            lista1.append(self.viajes.text())
        if self.deportes.isChecked():
            lista1.append(self.deportes.text())
        if self.games.isChecked():
            lista1.append(self.games.text())
        if self.pelis.isChecked():
            lista1.append(self.pelis.text())
        if self.libros.isChecked():
            lista1.append(self.libros.text())
        if self.mascotas.isChecked():
            lista1.append(self.mascotas.text())

        if self.leer.isChecked():
            lista2.append(self.leer.text())
        if self.dormir.isChecked():
            lista2.append(self.dormir.text())
        if self.jugar.isChecked():
            lista2.append(self.jugar.text())
        if self.series.isChecked():
            lista2.append(self.series.text())
        if self.comprar.isChecked():
            lista2.append(self.comprar.text())
        if self.musica.isChecked():
            lista2.append(self.musica.text())

        return lista1,lista2

    def guardar(self):
        listaGustos=[]
        listaPasatiempos=[]
        fecha = self.calendarWidget.selectedDate()
        frase = self.textEdit.toPlainText()
        print (frase)
        print(fecha.toString())
        gustos,pasatiempos= self.item_checado(listaGustos,listaPasatiempos)

        print ('Gustos \n',gustos)

        print ('pasatiempos \n',pasatiempos)

if __name__ == '__main__':
    app=QApplication([])
    ventana = ClsPasaTiempos(None)
    ventana.show()
    sys.exit(app.exec())  
