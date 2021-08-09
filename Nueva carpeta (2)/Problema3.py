ciclo=1
dicc={}
while(ciclo):
    print("Que deseas hacer? ")
    print("1.-Añadir factura ")
    print("2.-Pagar factura ")
    print("3.-Mostrar facturas por pagar ")
    print("4.-Salir")
    opcion=int(input("   :"))
    if(opcion==1):
        codigo=str(input("Ingresa el codigo de la factura "))
        precio=str(input("Ingresa el precio de la factura "))
        if(not(codigo in dicc)):
            dicc[codigo]=precio
        else:
            print("Ese codigo ya existe, factura no agregada ")
    elif(opcion==2):
        codigo = str(input("Ingresa el codigo de la factura "))
        if(codigo in dicc):
            del dicc[codigo]
        else:
            print("Codigo de factura no existente")
    elif(opcion==4):
        ciclo=0
        print("ADIOS :D")
    elif(opcion==3):
       for i in dicc:
           print("-----------------------------------")
           print("clave: {}  costo: {} ".format(i,dicc[i]))
       print("-----------------------------------")
    else:
        print("Opcion no valida")
