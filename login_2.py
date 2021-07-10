import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from Login2 import Ui_MainWindow

class MyLogin(QMainWindow):
    def __init__(self):
        super(MyLogin,self).__init__
        super.ui = Ui_MainWindow
        self.ui.setup(self)


app = QApplication([])
ventana = MyLogin()
ventana.show
sys.exit(app.exec())