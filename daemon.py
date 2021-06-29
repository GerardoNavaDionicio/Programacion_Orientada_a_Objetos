import threading
import time
from random import random

class Mensaje():
    __msj=''
    __numMsj=0
    __disponible = False

    def almacenar(self,nmsj,condicion):
        global __msj
        global __numMsj
        global __disponible

        while self.__disponible == True:
            try:
                condicion.wait()
            except InterruptedError as err:
                print(err)

        self.__msj = 'Mensaje'
        self.__numMsj=nmsj
        self.__disponible = True
        condicion.notifyAll()

    def obtener(self,condicion):
        global __msj
        global __numMsj
        global __disponible

        while self.__disponible == False:
            try:
                condicion.wait()
            except InterruptedError as err:
                print(err)

        self.__disponible = False
        condicion.notifyAll()
        
        mensaje = self.__msj +'#'+str(self.__numMsj)
        return mensaje

class Productor(threading.Thread):
    __mensaje = Mensaje()
    __continuar = True

    def __init__(self,mensaje,condicion):
        global __mensaje
        super().__init__()
        self.__mensaje = mensaje
        self.condicion = condicion

    def run(self):
        global __continuar
        while self.__continuar:
            self.condicion.acquire()
            numM=(int(random()*100))
            self.__mensaje.almacenar(numM,self.condicion)
            print('Productor ',threading.currentThread().getName(),'almacena el mensaje #: ',numM)
            try:
                mseg = (int(random()*5))
                time.sleep(mseg)
            except InterruptedError as err:
                print(err)
            self.condicion.release()

    def terminar(self):
        global __continuar
        self.__continuar = False

class Consumidor(threading.Thread):
    __mensaje = Mensaje()
    __continuar = True

    def __init__(self,mensaje,condicion):
        global __mensaje
        super().__init__()
        self.__mensaje = mensaje
        self.condicion = condicion

    def run(self):
        global __continuar
        while self.__continuar:
            self.condicion.acquire()
            mnsj = self.__mensaje.obtener(self.condicion)
            print('consumidor ',threading.currentThread().getName(),' obtuvo: ',mnsj)
            self.condicion.release()

    def terminar(self):
        global __continuar
        self.__continuar = False

class SincronizacionHilos():
    if __name__=="__main__":
        condicion = threading.Condition()
        mensaje = Mensaje()
        productor = Productor(mensaje,condicion)
        productor2 = Productor(mensaje,condicion)
        consumidor1= Consumidor(mensaje,condicion)
        consumidor2= Consumidor(mensaje,condicion)

        productor.start()
        productor2.start()
        consumidor1.start()
        consumidor2.start()
        productor.join(3)
        productor2.join(3)
        consumidor1.join(3)
        consumidor2.join(3)
        productor.terminar()
        productor2.terminar()
        consumidor1.terminar()
        consumidor2.terminar()
                
    
    
