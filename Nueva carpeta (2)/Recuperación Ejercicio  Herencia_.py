from abc import ABC, abstractmethod
class Mascota(ABC):
    def _init_(self, nombre, color,genero ):
        self.nombre = nombre
        self.color = color
        self.genero = genero
    @property
    def nombre(self):
        return self.__nombre
    @property
    def color(self):
        return self.__color
    @property
    def genero(self):
        return self.__genero
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @color.setter
    def color(self,color):
        self.__color = color
    @genero.setter
    def genero(self,genero):
        self.__genero = genero
    @abstractmethod
    def comida(self):
        pass
    @abstractmethod
    def vacunas(self):
        pass
    def _str_(self):
        cadena = "\n Nombre: {0}".format(self.nombre)
        cadena = cadena + "\n Color: {0}".format(self.color)
        cadena = cadena + "\n Genero: {0}".format(self.genero)
        return cadena
class Mamifero():
    def descripcion(self):
        return print("Nace del Vientre")
    def habitat(self):
        return print("Toda clase de hábitat.")
class Vertebrado():
    def extremidades(self):
        return print("Permiten desplazarse.")
    def reproduccion(self):
        return print(" Sexual.")
class Conejo(Mascota, Mamifero, Vertebrado):
    def comida(self):
        return print("Come zanahorias.")
    def vacunas(self):
        return print("Vacuna contra la rabia.")
class Huron(Mascota, Mamifero, Vertebrado):
    def comida(self):
        return print("Dezconosco que come.")
    def vacunas(self):
        return print("Debe vacunarse.")
class Perro(Mascota, Mamifero, Vertebrado):
    def comida(self):
        return print("Come croquetas.")
    def vacunas(self):
        return print("Vacuna contra la rabia.")
class Gato(Mascota, Mamifero, Vertebrado):
    def comida(self):
        return print("Come whiskas.")
    def vacunas(self):
        return print("Vacuna contra la rabia.")

if __name__=="__main__":
    conejo1 = Conejo("Rabito", "Blanco", "Macho")
    conejo2 = Conejo("Rabittt", "Blanco", "Macho")
    conejo3 = Conejo("Conejito", "Blanco", "Hembra")
    huron = Huron("H", "Cafe", "Macho")
    perro1 = Perro("Pinone", "Cafe", "Macho")
    perro2 = Perro("Ruffus", "Blaco", "Hembra")
    gato = Gato("Chaneke", "Gris", "Hembra")
    listaMascotas = []
    listaMascotas.append(conejo1)
    listaMascotas.append(conejo2)
    listaMascotas.append(conejo3)
    listaMascotas.append(huron)
    listaMascotas.append(perro1)
    listaMascotas.append(perro2)
    listaMascotas.append(gato)
    listaOrdenada = sorted(listaMascotas, key = lambda x : x.nombre)
    for mascota in listaOrdenada:
        print(mascota)