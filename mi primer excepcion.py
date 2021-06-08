class MiPrimeraExcepcion(Exception):
    def __init__(self,mensaje):
        self.mensaje=mensaje
        super().__init__(self.mensaje)
        
try:
    raise MiPrimeraExcepcion('Mi excepcion')
except MiPrimeraExcepcion as err:
    print(err.mensaje)