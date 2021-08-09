from  abc import ABC, abstractclassmethod, abstractmethod
class Conferencia(ABC):
    def __init__(self, nombre, inicioConferencia, finConferencia, ciudad, pais, envioArticulos, revisionArticulos,envioFinalArticulos):
        self.__nombre = nombre
        self.__inicioConferencia = inicioConferencia
        self.__finConferencia = finConferencia
        self.__ciudad = ciudad
        self.__pais = pais
        self.__envioArticulos = envioArticulos
        self.__revisionArticulos = revisionArticulos
        self.__envioFinalArticulos = envioFinalArticulos
        super().__init__()
    @property
    def nombre(self):
        return  self.__nombre
    @property
    def inicioConferencia(self):
        return self.__inicioConferencia
    @property
    def finConferencia(self):
        return self.__fincioConferencia
    @property
    def ciudad(self):
        return self.__ciudad
    @property
    def pais(self):
        return self.__pais
    @property
    def revisionArticulos(self):
        return
    @property
    def envioArticulos(self):
        return self.__envioArticulos
    @property
    def envioFinalArticulos(self):
        return self.envioFinalArticulos
    #----
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @inicioConferencia.setter
    def inicioConferencia(self,inicioConferencia):
        self.__inicioConferencia = inicioConferencia
    @finConferencia.setter
    def finConferencia(self,finConferencia):
        self.__fincioConferencia=finConferencia	
    @ciudad.setter
    def ciudad(self,ciudad):
        self.__ciudad=ciudad
    @pais.setter
    def pais(self,pais):
        self.__pais=pais
    @revisionArticulos.setter
    def revisionArticulos(self,revisionArticulos):
        self.revisionArticulos =revisionArticulos
    @envioArticulos.setter
    def envioArticulos(self,envioArticulos):
        self.__envioArticulos=envioArticulos
    @envioFinalArticulos.setter
    def envioFinalArticulos(self,envioFinalArticulos):
        self.__envioArticulos=envioFinalArticulos
    @abstractclassmethod
    def chairmen(self):
        pass
class ConferenciaCientifica(Conferencia):
    def chairmen(self,presidente):
        print('EL chairmen de esta conferencia es: ',presidente)	
class Persona(ABC):
    def __init__(self, nombre, institucion, correo):
        self.__nombre = nombre
        self.__institucion = institucion
        self.__correo = correo
        property
    @property
    def nombre(self):
        return self.__nombre
    @property
    def institucion(self):
        return self.__institucion
    @property
    def correo(self):
        return self.__correo
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @institucion.setter
    def institucion(self,institucion):
        self.__institucion = institucion
    @correo.setter
    def correo(self,correo):
        self.__correo = correo

class Presidente(Persona):
    def __init__(self, nombre, institucion, correo,gradoAcademico,roll):
        super().__init__(nombre, institucion, correo)
        self.__gradoAcademico = gradoAcademico
        self.__roll = roll
    @property
    def gradoAcadeico(self):
        return self.__gradoAcademico
    @property
    def roll(self):
        return self.__roll
    @gradoAcademico.setter
    def correo(self,gradoAcademico):
        self.__gradoAcademico = gradoAcademico
    @roll.setter
    def roll(self,roll):
        self.roll=roll
class Autores(Persona):
    def __init__(self, nombre, institucion, correo,departamento,pais,autoCorrespondecia):
        super().__init__(nombre, institucion, correo)
    @property
    def departamento(self):
        return self.departamento
    @property
    def pais(self):
        return self.pais
    @property
    def autorCorrespondencia(self):
        return self.autorCorrespondencia
    @departamento.setter
    def departamenti(self,departamento):
        self.departamento=departamento
    @pais.setter
    def pais(self,pais):
        self.pais=pais
    @autoCorrespondencia.setter
    def autoCorrespondencia(self,autoCorrespondencia):
        self.autoCorrespondencia=autoCorrespondencia

class Revisor(Persona):
    def __init__(self, nombre, institucion, correo,topico):
        super().__init__(nombre, institucion, correo)
        self.__topico=topico
    @property
    def topico(self):
        return self.__topico
    @topico.setter
    def tipoco(self,topico):
        self.__topico=topico
