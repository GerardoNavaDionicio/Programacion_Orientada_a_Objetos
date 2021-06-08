from abc import ABC,abstractmethod

class Mascota (ABC):
    @abstractmethod
    def comida(self):
        pass
    @abstractmethod
    def vacunas(self):
        pass
class Conejo(Mascota):
    def comida(self):
        return print('Se ven bonitos')
    def vacunas(self):
        return print("Vacunalo o te da Rabia")

class Huron(Mascota):
    def comida(self):
        return print('Se ven bonitos')
    def vacunas(self):
        return print("Vacunalo o te da Rabia")

if __name__=="__main__":
    c=Conejo
    h=Huron
    c.comida()
    c.vacunas()
    print("Es un huron")
    h.comida()
    h.vacunas()
