import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MyWindowClass(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(".\Interfacez\IMC.ui",self)
        self.setWindowTitle("Calcula tu IMC" )
        self.btCalcular.clicked.connect(self.btCalcular_clicked)
        self.btBorrar.clicked.connect(self.btBorrar_clicked)
        self.rbMujer.toggled.connect(self.onClicked)
        self.rbHombre.toggled.connect(self.onClicked)
        self.rbNA.toggled.connect(self.onClicked)
    def btCalcular_clicked(self):
        estatura = float(self.lineEditEstatura.text())
        peso = float(self.lineEditPeso.text())
        res=peso/estatura**2
        self.resultado.setText(str(res))
    def btBorrar_clicked(self):
        self.lineEditEstatura.setText('')
        self.lineEditPeso.setText('')
        self.resultado.setText('')

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            msj=radioBtn.text()+'Cuida tu salud'
            print("eres %s" % (radioBtn.text()))
            QMessageBox.information(self,"aviso",msj,QMessageBox.Ok)
            
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = MyWindowClass()
    MyWindow.show()
        #app.exec_()ejecuta con o sin errores
    sys.exit(app.exec())