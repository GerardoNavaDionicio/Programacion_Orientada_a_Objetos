import threading
class Mithead1(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num

    def run(self):
        print('soy el hilo',self.num)
    
if __name__=="__main__":
    for i in range(0,10):
        t=Mithead1(i)
        t.setName('hola prro-'+str(i))
        t.start()
        print(t.getName())
        t.join()
        print(t.is_alive())

