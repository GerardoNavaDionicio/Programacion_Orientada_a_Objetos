def division(dividendo,divisor):
    res=dividendo/divisor
    return res
def suma(numero1,numero2):
    r=numero1+numero2
    return r
try:
    s=suma(34,21)
    print('El resultado de la suma es:',s )
    res=division(23,21)
    print('El resultado de la division es:',res)
    print('Leeremos un archivo')
    f = open ('holaMundo.txt','r')
    for linea in f:
        print(linea,end='')
except  IOError as err:
    print ('Este error corresponde al archivo:',err)
except ZeroDivisionError as err:
    print ('No se puede dividir entre cero')
except Exception as err:
    print ('Error Desnonocido',err)
finally:
    if not f.closed:
        f.closed()