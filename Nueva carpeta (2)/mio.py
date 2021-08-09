class NumError(Exception):
    def __init__(self,numero,mensaje = 'Ponle mas varo pa la Coca '):
        self.numero=numero
        self.mensaje=mensaje
        super().__init__(self.mensaje)
    def __str__(self):
        return f'{self.numero} -> {self.mensaje}'
class NumeroError(ArithmeticError):
    def __init__(self,numero2,mensaje2 = 'Error :c'):
        self.valor2=numero2
        self.mensaje2=mensaje2
        super().__init__(self.mensaje2)
    def __str__(self):
        return f'-> {self.mensaje2}'

def suma(a,b):
    res=a + b
    if res < 35:
        print(res,'no alcanza pa la coca :C ')
        return False
    print('Alcanza pa la coca, lanzate!!')
    return True

try:
    x=int(input('Ingresa un numero: '))
    y=int(input('Ingresa otro numero: '))
    res2=suma(x,y)
    if not(res2):
        raise NumError(res2)
    
except NumError as err:
    print('El error es: ',err.mensaje)

except ZeroDivisionError as err:
    print('El error a mostrar: ',err.mensaje2)
    


finally:
    pass
    

