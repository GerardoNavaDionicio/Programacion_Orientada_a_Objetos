#Ejercicio_2: Implemente un programa que use hilos independientes. Un hilo imprime deberá imprimir números
#pares del 1-30, y otro hilo imprime números impares del 1-30. Cree dos instancias (hilos) de cada uno y muestre la salida.
#Gerardo Nava Dionicio 191801029

import threading
class NumerosPares(threading.Thread):
    def run(self):
        a=0
        for a in range(1,31):
            if a%2==0:
                print('Numero Par:\t','<',a,'>')
class NumerosImpares(threading.Thread):
    def run(self):
        a=0
        for a in range(1,31):
            if  a%2!=0:
                print('NUMERO IMPAR:\t',a)
class SincronizacionHilos():
    if __name__=="__main__":
        pares = NumerosPares()
        impares = NumerosImpares()
        pares.start()     
        impares.start()
