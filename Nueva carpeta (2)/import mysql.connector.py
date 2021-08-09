import mysql.connector
import pyobdc
print("Hola")

class ConexionBD():
    # Crear la conexion SQL
    def CreaDBConnection(self, servidor,database,user,password):         
        connection = pyodbc.connect(Driver="{ODBC Driver 17 for SQL Server}", 
                            Server=servidor, 
                            Database=database, 
                            UID=user, 
                            PWD=password) 

        return connection
  
# cerrar la conexion
    def closeDBConnection(self,connection):          
        try: 
            connection.close() 
        except pyodbc.ProgrammingError as e: 
            print(e)