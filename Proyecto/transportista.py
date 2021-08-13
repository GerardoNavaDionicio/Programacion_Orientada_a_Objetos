from ConexionBD import Conexion
import sys
import pymysql
import os
class App:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',user='root',passwd='1234567890',db='proyecto')
        self.cursor = self.conn.cursor()
    def Insertar(self):
        numero1 = input('ingrese el numero de cliente:\n')
        telefono1 = input('ingresa tu telefono\n')
        cliente1 = input ('ingresa tu nombre\n')
        direccion1 =  input ('ingresa tu direccion\n')
        pedido1 = input('ingresa numero de pedido\n')
        sql = "insert into cliente (numero,telefono,nombre,direccion,pedido) values('{}','{}','{}','{}','{}')".format(numero1,telefono1,cliente1,direccion1,pedido1)
        self.cursor.execute(sql)
        print('Datos ingresador correctos');
        self.conn.commit()
        os.system('pause')
aplication =  App()
aplication.Insertar()