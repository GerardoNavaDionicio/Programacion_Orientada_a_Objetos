# Ejercicio_1: Generados aleatoriamente números en un rango del 0-100, con un retardo de tiempo de 5 segundos,
#una vez generados, se deben almacenar en una lista, ordenarlos de menor a mayo y mostrarlos.
#Gerardo Nava Dionicio 191801029
import random
import time
import threading
class Numeros_Aleatorios(threading.Thread):
    def run(self):
        print("Cuantos numeros Aleatorios quieres?")
        a=int(input())
        numeros=[0]*a
        for i in range(a):
            numeros[i] = random.randint(0, 100)
            time.sleep(1)
            print(numeros[i])
        numeros.sort()
        print('Numeros Ordenados de Mayor a menor',numeros,'\n')
if __name__=="__main__":
    numeros_aleatorios=Numeros_Aleatorios()
    numeros_aleatorios.start()
    numeros_aleatorios.join()