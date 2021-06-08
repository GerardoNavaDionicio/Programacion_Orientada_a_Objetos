class Mascota:
    _classInfo = 'animales de casa'
    @classmethod
    def acerca(clase):
        print ('Esta clase es acerca de  '+ clase._classInfo)
class Perro (Mascota):
    _classInfo = 'Son los mejores'
class Gato(Mascota):
    _classInfo='Si son agradables '

if __name__=="__main__":
    m = Mascota()
    Mascota.acerca()
    p = Perro()
    Perro.acerca()
    g= Gato()
    Gato.acerca()
