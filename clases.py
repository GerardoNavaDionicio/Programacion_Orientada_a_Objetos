class Persona:
    codigo_postal = '72800'
    def __init__(self, nombre, matricula, edad):
        self.nombre=nombre
        self.matricula=matricula
        self.edad=edad
        
    def __str__(self):
        cadena = 'Nombre: {0}\n'.format(self.nombre)
        cadena = cadena + 'Matricula: {0}\n'.format(self.matricula)
        cadena = cadena +'edad: {0}\n'.format(self.edad)
        cadena = cadena + 'codigo postal: {0}'.format(self.codigo_postal)
        return cadena
    def copia(self):
        nueva = Persona(self.nombre[:], self.matricula[:],self.edad)
        return nueva
def probando_esto(persona1,persona2):
    persona1.edad +=1
    persona3=persona2
    persona4=persona2.copia()
    persona3.edad -= 1 
    persona4.edad -= 2
    return persona4
    

if __name__=="__main__":
    #print(Persona.__dict__)
    gerardo = Persona('Gerardo','191801029',23)
    gerardo.codigo_postal = '52100'
    #print(gerardo.__dict__)
    print(gerardo)
    p2=gerardo.copia()
    p2.edad=33
    print (gerardo is p2)
    bere = Persona('Bere','191801009',20)
    otra = probando_esto(gerardo,bere)
    bere = Persona('Bere','191801009',20)
    print(gerardo)
    print(bere)
    print(otra)
##    luis = Persona('Luis','182801023',25)
##    luis.codigo_postal = '72765'
##    print(luis)























































    

