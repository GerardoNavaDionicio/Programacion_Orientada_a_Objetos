from abc import ABC, abstractmethod

class Mascota(ABC):
    @abstractmethod
    def acerca(self):
        pass
    @abstractmethod
    def pasatiempo(self):
        print("Jugar,comer,kgar")
class Dog(Mascota):
    def acerca(self):
        return print ("son animales domesticos")
    def pasatiempo(self):
        return super().pasatiempo()
    
class Cat(Mascota):
    def acerca(self):
        return print ("son Malos")
    def pasatiempo(self):
        return super().pasatiempo()
if __name__=="__main__":
    p=Dog()
    g=Cat()
    p.acerca()
    p.pasatiempo()
    print('Lindo Perrito')
    g.acerca()
    g.pasatiempo()
    print('Lindo Gatico')


