try:
    a = int(input('Ingrese un primer numero: '))
    b = int(input('Ingrese un segundo numero: '))
    c = a*b
except ArithmeticError as err:
    print('Error, no ingresaste un numero ',err)
except Exception as err:
    print('Error, no ingresaste un numero',err)
else:
    print('El Resultado es \t: ',c)
finally:
    print('finalizado')
