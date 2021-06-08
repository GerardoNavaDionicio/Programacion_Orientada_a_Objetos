class Persona():
    def __init__ (self,nombre,edad,genero):
        self.__nombre=nombre
        self.__edad=edad
        self.__genero=genero
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def genero(self):
        return self.__genero
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    @edad.setter
    def edad(self,edad):
        self.__edad=edad
    @genero.setter
    def genero(self,genero):
        self.__genero=genero
           
if __name__=="__main__":
    tere = Persona('Tere',22,'Mujer')
    print (tere.nombre)
    print (tere.edad)
    print (tere.genero)
    tere.nombre='Teresa'
    tere.edad = 45
    tere.genero='inclusive xd'
    print (tere.nombre)
    print (tere.edad)
    print (tere.genero)
        



            
