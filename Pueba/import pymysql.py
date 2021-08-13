import pymysql
import os
class App:
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',user='root',passwd='1234567890',db='poo')
        self.cursor = self.conn.cursor()
    def Insertar(self):
        id_usuario = input('ingrese el id:\n')
        nombre = input('ingresa nombr\n')
        contra = input ('ingresa password\n')
        sql = "insert into usuarios (idUsuario,usuario,password) values('{}','{}','{}')".format(id_usuario,nombre,contra)
        self.cursor.execute(sql)
        print('Datos ingresador correctos');
        self.conn.commit()
        os.system('pause')
    def Mostrar(self):
        sql="select * from usuarios"
        self.cursor.execute(sql)
        personas = self.cursor.fetchall()
        for i in personas:
            print("ID:\t",i[0])
            print("usuario:",i[1])
            print("pass:\t",i[2])
            print ("--------------------------")
aplication =  App()
aplication.Insertar()
aplication.Mostrar()