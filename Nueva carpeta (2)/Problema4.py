dicc={}
salir=1
while(salir):
    print("Que deseas hacer?")
    print("1.-Añadir cliente ")
    print("2.-Eliminar cliente")
    print("3.-Mostrar cliente")
    print("4.-Listar todos los clientes")
    print("5.-Listar clientes preferenciales")
    print("6.-Terminar")
    opcion=int(input("     :"))
    if(opcion is 1):
        nombre= str(input("Ingresa el nombre del cliente  "))
        direccion = str(input("Ingresa la direccion del cliente  "))
        correo = str(input("Ingresa el correo del cliente  "))
        NIF = str(input("Ingresa el NIF del cliente  "))
        preferente = str(input("Ingresa 'si' en caso de que el cliente sea preferente y 'no' si no lo es "))
        if(preferente.upper()=="SI"):
            pre=True
        else:
            pre=False
        diccaux={'nombre':nombre,'direccion':direccion,'preferencia':pre}
        dicc[NIF]=diccaux
    elif (opcion is 2):
        NIF = str(input("Ingresa el NIF del cliente "))
        if (NIF in dicc):
            del dicc[NIF]
        else:
            print("NIF de cliente no existente")
    elif (opcion is 3):
        for i in dicc:
           mostrar=str(input("Ingresa el NIF del cliente a mostrar "))
           if (NIF in dicc):
               print(dicc[NIF])
           else:
               print("NIF de cliente no existente")
        print("-----------------------------------")
    elif (opcion is 4):
        for i in dicc:
            print("-----------------------------------")
            print("clave: {}  costo: {} ".format(i, dicc[i]))
        print("-----------------------------------")
    elif (opcion is 5):
        for i in dicc:
            dicc2=dicc[i]
            if(dicc2['preferencia']==True):
                print("clave: {}  costo: {} ".format(i, dicc[i]))
    elif (opcion is 6):
        salir = 0
        print("ADIOS :D")
    else:
        print("Opcion invalida")
