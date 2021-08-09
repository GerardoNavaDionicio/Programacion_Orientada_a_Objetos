
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QLineEdit

from IMCUI import Ui_MainWindow

class IMC(QMainWindow):
    def __init__(self):
        super(IMC,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btCalcular.clicked.connect(self.btCalcular_clicked)
        self.ui.btBorrar.clicked.connect(self.btBorrar_clicked)
        self.ui.rbMujer.toggled.connect(self.onClicked)
        self.ui.rbHombre.toggled.connect(self.onClicked)
        self.ui.rbNA.toggled.connect(self.onClicked)
        
    def btCalcular_clicked(self):
        estatura = float(self.ui.lineEditEstatura.text())
        peso = float(self.ui.lineEditPeso.text())
        res=peso/estatura**2
        self.ui.resultado.setText(str(res))

    def btBorrar_clicked(self):
        self.ui.lineEditEstatura.setText('')
        self.ui.lineEditPeso.setText('')
        self.ui.resultado.setText('')

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            msj=radioBtn.text()+'Cuida tu salud'
            print("eres %s" % (radioBtn.text()))
            QMessageBox.information(self,"aviso",msj,QMessageBox.Ok)
if __name__ == '__main__':
    app = QApplication([])
    MyWindow = IMC()
    MyWindow.show()
        #app.exec_()ejecuta con o sin errores
    sys.exit(app.exec())