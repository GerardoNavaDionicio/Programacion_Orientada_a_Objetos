import sys
from PyQt5.QtGui import qAlpha
import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit

from Login2 import Ui_MainWindow
from ConexionBD import Conexion
from proyecto_final import proyecto_int

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
        self.proy = proyecto_int()

    def Ingresar(self):
        pw = self.Consultar(self.ui.pass_datos.text(), self.ui.usuario_datos.text())

        if pw:
            QMessageBox.information(self, "Información", "Acceso permitido", QMessageBox.Ok)
            print("Acceso correcto")
            print("Usuario:", self.ui.usuario_datos.text())
            print("Contraseña:", self.ui.pass_datos.text())
            self.Borrar()
            QApplication.quit()
            #proy = proyecto_int()
            #proy.show()
            #self.abrir_ventana()
            self.proy.show()
        else:
            QMessageBox.information(self, "Alerta", "Acceso denegado", QMessageBox.Ok)
            print("Acceso Incorrecto")
            self.ui.usuario_datos.setText('')
            self.ui.pass_datos.setText('')

    def abrir_ventana(self):
        
        '''app_proy = QApplication([])
        ventana_proy = proyecto_int()
        ventana_proy.show()
        sys.exit(app_proy.exec())''' 
        

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
    
    


