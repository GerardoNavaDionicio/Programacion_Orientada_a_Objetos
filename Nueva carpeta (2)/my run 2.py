from threading import Thread
suma=0
def incremento(num):
    print("\t comienza el hilo")
    global suma
    suma=suma+num
    print("El incremento es: ",suma)

print("Probando variable local")
print("'Valor inicial",suma)
try:
    for i in range (0,3):
        hilo1=Thread(target=incremento(i))
        hilo1.start()
        hilo1.join()
except NameError as:
    print("El error es")
else:
    print("El  valor final es",suma)





