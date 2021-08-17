import sys
import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QButtonGroup, QMainWindow, QMessageBox, QLineEdit
from pymysql.cursors import Cursor
from int import Ui_MainWindow
from ConexionBD import Conexion
import webbrowser
pedidos={}
class proyecto_int(QMainWindow):
    def __init__(self):
        super(proyecto_int, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nombre_cliente
        self.ui.telefono_cliente
        self.ui.direccion_cliente
        self.ui.numero_cliente
        self.ui.distancia_datos
        self.ui.vehiculo_datos
        #self.ui.ayuda_text.triggered.connect(self.chems)
        self.ui.helpBT.triggered.connect(self.chems)
#        self.ui.enviar_botton.clicked.connect(self.Insertar)
        self.ui.guardar_botton.clicked.connect(self.Guardar)

        self.c = Conexion()
        self.conn = self.c.CrearConexion()
        self.cursor = self.conn.cursor()
        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.ui.rb1)  
        self.RadioGroup.addButton(self.ui.rb2)
        self.RadioGroup.addButton(self.ui.rb3)
        self.RadioGroup.addButton(self.ui.rb4)
        self.RadioGroup.addButton(self.ui.rb5)
        self.RadioGroup.addButton(self.ui.rb6)
        self.RadioGroup.addButton(self.ui.rb7)
        self.RadioGroup.addButton(self.ui.rb8)
        self.RadioGroup.addButton(self.ui.rb9)
        self.RadioGroup.addButton(self.ui.rb10) 
    def Guardar(self):
        km = self.ui.distancia_datos.text()
        car =  self.ui.vehiculo_datos.text()
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
        pedidos[km]
        





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
        self.ui.distancia_datos.setText('')
        self.ui.vehiculo_datos.setText('')
        self.RadioGroup.setExclusive(False)
        self.ui.rb1.setChecked(False)
        self.ui.rb2.setChecked(False)
        self.ui.rb3.setChecked(False)
        self.ui.rb4.setChecked(False)
        self.ui.rb5.setChecked(False)
        self.ui.rb6.setChecked(False)
        self.ui.rb7.setChecked(False)
        self.ui.rb8.setChecked(False)
        self.ui.rb9.setChecked(False)
        self.ui.rb10.setChecked(False)
        self.RadioGroup.setExclusive(True)
    def chems(self):
        webbrowser.open("https://m.facebook.com/permalink.php?story_fbid=105737101284775&id=105736124618206&substory_index=0")

if __name__ == '__main__':
    app = QApplication([])
    ventana = proyecto_int()
    ventana.show()
    sys.exit(app.exec())
    
