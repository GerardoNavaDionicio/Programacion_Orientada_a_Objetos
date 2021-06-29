'''Elabore un hilo que con 5 nombres de personas viendo una seria con palomitas (100grs), quien
termine consuma los primeros 50gras deberá enviar un mensaje y finalmente indicar cuando hayan
terminado los 100grs).
Se deberá crear el constructor correspondiente y pasar como parámetro el nombre y sabor de las
palomitas.
Salida:
Juan1: ha consumido 50grs de palomitas de mantequilla.
......
....
...
Juan1 ha terminado sus palomitas de mantequilla.
->Gerardo Nava Dionicio 191801029 '''
import threading

class Palomitas(threading.Thread):
    def __init__(self, nombre, sabor):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.sabor = sabor
    def run(self):
        i=0
        for i in range(50,100):
            print(self.nombre, 'ha comido ',i,'grs de palomitas de ', self.sabor)
        print(self.nombre,'termino los 100 grs de palomitas de ', self.sabor)     

if __name__=="__main__":
    nombres = ['Bere UwU','Gee','Kota','Pinole','Ruffus','Dollar']
    for nom in nombres:
        mantequilla = Palomitas(nom,'Mantequilla')
        mantequilla.start()
        mantequilla.join()

