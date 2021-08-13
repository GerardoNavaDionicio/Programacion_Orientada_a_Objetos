import sys
import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from int import Ui_MainWindow
from ConexionBD import Conexion

class proyecto_int(QMainWindow):
    def __init__(self):
        super(proyecto_int, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nombre_cliente
        self.ui.telefono_cliente
        self.ui.direccion_cliente
        self.ui.numero_cliente
        self.ui.repartidor_datos
        self.ui.enviar_botton.clicked.connect(self.Insertar)
        self.c = Conexion()
        self.conn = self.c.CrearConexion()
        self.cursor = self.conn.cursor()
    def Insertar(self):
        rep = self.ui.repartidor_datos.text()
        num = self.ui.numero_cliente.text()
        tel = self.ui.telefono_cliente.text()
        nom = self.ui.nombre_cliente.text() 
        dire =self.ui.direccion_cliente.text()
        ped = self.pedido()
        sentencia=  "insert into cliente (numero,telefono,nombre,direccion,pedido) values('{}','{}','{}','{}','{}')".format(num,tel,nom,dire,ped)
        self.cursor.execute(sentencia)
        row = self.cursor.fetchone()
        self.conn.commit()
        self.limpiar()
    def pedido(self):
        if self.ui.rb1.isChecked():
            return 1
        if self.ui.rb2.isChecked():
            return 2
        if self.ui.rb3.isChecked():
            return 3
        if self.ui.rb4.isChecked():
            return 4
        if self.ui.rb5.isChecked():
            return 5
        if self.ui.rb6.isChecked():
            return 6
        if self.ui.rb7.isChecked():
            return 7
        if self.ui.rb8.isChecked():
            return 8
        if self.ui.rb9.isChecked():
            return 9
        if self.ui.rb10.isChecked():
            return 10
    def limpiar (self):
        self.ui.numero_cliente.setText('')
        self.ui.telefono_cliente.setText('')
        self.ui.nombre_cliente.setText('')
        self.ui.direccion_cliente.setText('')
        self.ui.repartidor_datos.setText('')
        self.ui.rb1.setChecked(True)
        self.ui.rb2.setChecked(True)
        self.ui.rb3.setChecked(True)
        self.ui.rb4.setChecked(True)
        self.ui.rb5.setChecked(True)
        self.ui.rb6.setChecked(True)
        self.ui.rb7.setChecked(True)
        self.ui.rb8.setChecked(True)
        self.ui.rb9.setChecked(True)
        self.ui.rb10.setChecked(True)
        self.ui.rb11.setChecked(True)
       
if __name__ == '__main__':
    app = QApplication([])
    ventana = proyecto_int()
    ventana.show()
    sys.exit(app.exec())

