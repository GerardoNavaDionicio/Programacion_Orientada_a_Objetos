##tuplas=(10,"Nava",True)
##print(tuplas)
##tuplas2=(33)
##print(tuplas2)



"""marcas=('Soni','apple','Acer','Hp','Intel','lenovo','thinkpad','Dell','Mac')
for i in range(0,len(marcas)):
    print(i,marcas[i])"""





##dicc={'Nombre':"Gerardo",'Edad':23, 'Puesto':"Ingeniero",'Feliz':"No"}
##print(dicc['Edad'])
##
##for i in dicc:
##    print("El valor de la etiqueta {} es {}".format(i,dicc[i]))
##
##dicc['Nombre']="Genady"
##dicc['Edad']=dicc['Edad']+10
##dicc['Puesto']="Vago"
##dicc['Feliz']="Simon"
##
##dicc['color']="Carton"
##dicc['estatura']=1.75
##
##for i in dicc:
##    print("El valor de la etiqueta {} es {}".format(i,dicc[i]))




##secuencia = "uno dos tres".split()
##print (secuencia)
##
##
##matriz[[1,2,3],[2,12,6],[1,0,-3],[0,-1,0]]
##for i in range (4):
##    print('\n')
##    for j in range(3):
##        print(matriz[i][j], end = ',')'''



##matriz=[]
##for i in range (5):
##    a=[1]*6
##    matriz.append(a)
##print(matriz)
##
##
##
##
##m=int(input('Filas: \n'))
##n=int(input('columnas: \n'))
##matriz=[]
##for i in range(m):
##    matriz.append([0]*n)
##for i in range(m):
##    for j in range(n):
##        matriz[i][j]=int(input('Ingresa un numero para {0},{1}: '.format(i,j)))
##print(matriz)







##def datos(nombre,apellido):
##    nomre_completo=nombre,apellido
##    print(nomre_completo)
##    
##datos("Gerardo","Nava")
##
##def datos():
##    nom=input("Name:\t")
##    apellido=input("Apellido:\t")
##    print("Datos=\t"+nom+" "+apellido)
##datos()
##
##
##def datos(nombre,apellido,msj="Quiovo"):
##    print(msj,nombre,apellido)
##    
##datos("Gerardo","Nava")







##def sumar (x,y):
##    return x+y
##print (sumar(5,9))
##
##def f(x,y):
##    return x**2,y*2
##
##a,b=f(2,3)
##print (a,b)



##def suma (n,m):
##    print(n+m)
##def resta(n,m):
##    print(n-m)
##
##    switch = {1:suma,2:resta}
##    n1=int(input('Ingresa valor de 1:\t'))
##    n2=int(input('Ingresa valor de 2:\t'))
##    opc=int(input('que quieres hacer?\n1=suma\n2=resta:\n\t'))
##    switch[opc](n1,n2)



##deposito50=100
##deposito20=100
##deposito10=100
##
##def sacar_dinero(cantidad):
##    global deposito50,deposito20,deposito10
##    de50=cantidad//50
##    cantidad=cantidad%50
##    de20=cantidad//20
##    cantidad=cantidad%20
##    de10=cantidad//10
##
##    deposito50=deposito50-de50
##    deposito20=deposito50-de20
##    deposito10=deposito50-de10
##    return [de50,de20,de10]
##cant=int(input("que cantidad quieres:\t"))
##print(sacar_dinero(cant))





def min (a,b):
    if a<b:
        return a
    else:
        return b
    
def max (a,b):
    if a>b:
        return a
    else:
        return b


if __name__=="__main__":
    print('El maximo de 3 y 10 es: ',max(3,10))
    print('El minimo de 3 y 10 es: ',min(3,10))

    






