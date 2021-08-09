import pymysql
class Conexion():
    def CrearConexion(self):
        connection = pymysql.connect(host="localhost",port=3306,user="root", password="1234567890", db="POO")
        return connection

    def CerrarConexion(self,connection):
        try:
            connection.close()
        except pymysql.ProgrammingError as e:
            print(e)

