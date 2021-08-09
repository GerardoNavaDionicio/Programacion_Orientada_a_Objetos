class NumPrimoError(Exception):
    def __init__(self,valor,mensaje = 'No es numero primo'):
        self.valor= valor
        self.mensaje=mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.valor} -> {self.mensaje}'

def es_primo(num):
    for i in range(2,num):
        if num%i == 0:
            print(num,'->No es primo, es divisor')
            return False
    print('Es primo')
    return True

try:
    x=int(input('Ingresa un numero: '))
    primo= es_primo(x)
    if not(primo):
        raise NumPrimoError(x)
except NumPrimoError as err:
    print(err)
'''class MiPrimerExcepcion(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

try:
    raise MiPrimerExcepcion('Mi excepcion')
except MiPrimerExcepcion as err:
    print(err.mensaje)
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

def func():
    raise IOError

try:
    func()

except IOError as exc:
    raise RuntimeError('No se puede abrir la BD') from exc'''
