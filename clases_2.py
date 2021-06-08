class Persona():
    def __init__(self):
        self.__materia='materia'#atributo privado
        self.__calif = 'Calif'
        self._profesor='profesor atributo protegido'# atributo protegido
        self.grupo = 'grupo atributo publico'# atributo publico
    def __del__(self):
        print("Destruyendo el objeto")

if __name__=="__main__":
    #aldo=Persona()
##    print('Revisando los tipos de atributos\n')
##    aldo._Persona__materia+='ya se pued emodificar\n'
##    aldo._Persona__calif += 'ya se pued emodificar\n'
##    aldo._profesor += 'ya se pued emodificar\n'
##    aldo.grupo += 'ya se pued emodificar\n'
##    print(aldo._Persona__materia)
##    print(aldo._Persona__calif)
##    print(aldo._profesor)
##    print(aldo.grupo)
##    print(aldo.__dict__)
##    tere = Persona()
##    luis = Persona()
##    luis=aldo
##    del (tere)
##    del (luis)


