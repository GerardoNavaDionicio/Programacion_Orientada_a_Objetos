import threading, time 
def trabajador():
    print(threading.currentThread().getName(),'lanzando')
    #segundos
    time.sleep(2)
    print(threading.currentThread().getName(),'Detenido')

def servicio():
    print(threading.currentThread().getName(),'lanzando')
    #segundos
    time.sleep(2)
    print(threading.currentThread().getName(),'Detenido')

h1=threading.Thread(target=servicio,name='Servicio')
h2=threading.Thread(target=trabajador,name='Trabajador')
h3=threading.Thread(target=trabajador)
h2.start
h3.start
h1.start
