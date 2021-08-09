import sys
import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit

from Login2 import Ui_MainWindow
from ConexionBD import Conexion

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pass_datos.setEchoMode(QLineEdit.Password)
        self.ui.registrar.clicked.connect(self.Ingresar)
        self.c = Conexion()
        self.conn = self.c.CrearConexion()
        self.cursor = self.conn.cursor()

    def Ingresar(self):
        pw = self.Consultar(self.ui.pass_datos.text(), self.ui.usuario_datos.text())

        if pw:
            QMessageBox.information(self, "Información", "Acceso permitido", QMessageBox.Ok)
            print("Acceso correcto")
            print("Usuario:", self.ui.usuario_datos.text())
            print("Contraseña:", self.ui.pass_datos.text())
            self.Borrar()
        else:
            QMessageBox.information(self, "Alerta", "Acceso denegado", QMessageBox.Ok)
            print("Acceso Incorrecto")
            self.ui.usuario_datos.setText('')
            self.ui.pass_datos.setText('')

    def Consultar(self, passw, user):
        sentencia = "SELECT * FROM usuarios WHERE usuario = '%s'" % user
        self.cursor.execute(sentencia)
        row = self.cursor.fetchone()
        if row != None:
            if row[2]== passw:
                return True
            else:
                return False
        else:
            print("Acceso Incorrecto")
        self.c.CerrarConexion(self.conn)

    def Borrar(self):
        self.ui.usuario_datos.setText('')
        self.ui.pass_datos.setText('')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Login()
    ventana.show()
    sys.exit(app.exec())
