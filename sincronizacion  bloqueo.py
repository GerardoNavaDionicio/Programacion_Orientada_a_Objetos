import threading
import time
suma = 0 
def ingresaDatos():
    cant = (int) (input('Ingresa una cantidad'))
    return cant
    def ingresaDato():
        global suma
        contador = 0
        time.sleep(2)
        hiloActual = threading.currentthread().getName()
        while contador < 10:
            print('Esperando a ser bloqueado:',hiloActual)
            bloqueo.acquire()
            try:
                contador - contador + 1
                cantidad = ingresaDatos()
                print('bloqueado por',hiloActual,contador )
                print('total',suma)
            finally:
                print('liberado bloqueo por',hiloActual)
                bloqueo.release
                
bloqueo = threading.Lock()