def division(dividendo,divisor):
    res = dividendo/divisor
    return res

try:
    #el codifo se va ejecutar
    div = division (23,0)
    print ("El resultado es:",div)

except ArithmeticError   as err:
    #el codigo que se va ejecutar si hay error
    print("Eres pendejo o k?",err)





