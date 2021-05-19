
mes = input("Da el numero de Mes")
mes=int(mes)
while mes > 12 or mes < 1:
    print ("Error de Mes")
    mes = int(input("Da el numero de Mes"))
print("Has elegido el mes", mes)

edad=0
while edad<18:
    edad = edad +1
    if edad % 2 ==0:
        continue
    print "Tu edad es" + str (edad)