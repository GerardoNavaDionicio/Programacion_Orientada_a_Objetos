evidenciasPOO=[]
unidad1={}
unidad2={}
unidad3={}

class Promedio(Exception):
    def __init__(self,mensaje = 'El promedio no puede ser mayor a 10'):
        self.mensaje=mensaje
        super().__init__(self.mensaje)

    def __str__(self):
        return f'{self.mensaje}'

class Evidencias(Exception):
    def __init__(self,mensaje2 = 'Exceso o insuficiencia de evidencias'):
        self.mensaje2 = mensaje2
        super().__init__(self.mensaje2)

    def __str__(self):
        return f'{self.mensaje2}'
class Calificacion(Exception):
    def __init__(self,mensaje3 = 'Lo siento, Reprobaste'):
        self.mensaje3 = mensaje3
        super().__init__(self.mensaje3)

    def __str__(self):
        return f'{self.mensaje3}'

def evalu(num):
    if num > 3:
        return False
    elif num < 3:
        return False
    else:
        return True

def final(c1,c2,c3):
    calFi = (c1 + c2 +c3)/3.0
    ca = round(calFi,2)
    if calFi < 7:
        print('Calificacion: ',ca)
        raise Calificacion
    else:
        print('Felicidades aprobaste la materia con calificacion final: ',ca)

def promU(prom):
    if prom > 10:
        return False
    else:
        return True

def Ordinario(unidad,prom=0):
    for i in unidad:
        print('-----------------------------------')
        print('Evidencia {}  Calificacion: {} '.format(i+1,unidad[i]))
    print('-----------------------------------')
    cali = 0
    for i in unidad:
        cali = cali + unidad[i]
    prom = cali/3.0
    prome = promU(prom)
    if not(prome):
        raise Promedio
    if prom < 7:
        ot=Recuperacion(unidad)
        cali = 0
        for i in unidad:
            cali = cali + unidad[i]
        ot = cali/3.0
        return ot
    else:
        return prom

def Recuperacion(unidad,prom=0):
    print('Recuperacion de evidencias reprobadas')
    for i in unidad:
        if unidad[i] < 7:
            unidad[i] = float(input('Nueva calificacion de evidencia reprobada: '))
    for n in unidad:
        print('-----------------------------------')
        print('Evidencia {}  Calificacion: {} '.format(n+1,unidad[n]))
    print('-----------------------------------')
    cali = 0
    for i in unidad:
        cali = cali + unidad[i]
    prom = cali/3.0
    prome = promU(prom)
    if not(prome):
        raise Promedio
    if prom < 7:
        ot = Extraordinario(unidad)
        cali = 0
        for i in unidad:
            cali = cali + unidad[i]
        ot = cali/3.0
        return ot
    else:
        return prom
    
def Extraordinario(unidad,prom=0):
    print('Recuperacion extraordinaria de evidencias reprobadas')
    for i in unidad:
        if unidad[i] < 7:
            unidad[i] = float(input('Nueva calificacion de evidencia reprobada: '))
    for n in unidad:
        print('-----------------------------------')
        print('Evidencia {}  Calificacion: {} '.format(n+1,unidad[n]))
    print('-----------------------------------')
    cali = 0
    for i in unidad:
        cali = cali + unidad[i]
    prom = cali/3.0
    prome = promU(prom)
    if not(prome):
        raise Promedio
    else:
        return prom

def Lista(un1,un2,un3):
    evidenciasPOO=[un1,un2,un3]
    return evidenciasPOO

def calificacion(c1,c2,c3,evidenciasPOO):
    cali=[CAL1,CAL2,CAL3]
    for i in range(len(evidenciasPOO)):
        print('Unidad ',i+1,' ',evidenciasPOO[i])
        ca = round(cali[i],2)
        print('Promedio Unidad',i+1,' :',ca,'\n')

try:
    ciclo = 1
    while(ciclo):
        print('1.-Evidencias Unidad 1 ')
        print('2.-Evidencias Unidad 2 ')
        print('3.-Evidencias Unidad 3 ')
        print('4.-Promedio general de la materia')
        print('5.- Salir ')
        op=int(input("   :"))
        if op == 1:
            unidad1={}
            evidencias=int(input('Numero de evidencias: '))
            tot = evalu(evidencias)
            if not(tot):
                raise Evidencias
            for n in range(evidencias):
                ev=float(input('Evidencia: '))
                if(not(n in unidad1)):
                    unidad1[n]=ev
            CAL1=Ordinario(unidad1)
            ca = round(CAL1,2)
            print('Este es tu promedio',ca)

        elif(op == 2):
            unidad2={}
            evidencias=int(input('Numero de evidencias: '))
            tot = evalu(evidencias)
            if not(tot):
                raise Evidencias
            for n in range(evidencias):
                ev=float(input('Evidencia: '))
                if(not(n in unidad2)):
                    unidad2[n]=ev
            CAL2=Ordinario(unidad2)
            ca = round(CAL2,2)
            print('Este es tu promedio',ca)

        elif(op == 3):
            unidad3={}
            evidencias=int(input('Numero de evidencias: '))
            tot = evalu(evidencias)
            if not(tot):
                raise Evidencias
            for n in range(evidencias):
                ev=float(input('Evidencia: '))
                if(not(n in unidad3)):
                    unidad3[n]=ev
            CAL3=Ordinario(unidad3)
            ca = round(CAL1,2)
            print('Este es tu promedio',ca)

        elif(op == 4):
            lis = Lista(unidad1,unidad2,unidad3)
            calificacion(CAL1,CAL2,CAL3,lis)
            final(CAL1,CAL2,CAL3)

        elif(op == 5):
            ciclo=0
            print('Gracias por su atencion')
            
        else:
            print('Opcion no valida, Intentalo de nuevo')

except Promedio as err:
    print('El error es: ',err.mensaje)

except Evidencias as err:
    print('El error es: ',err.mensaje2)

except Calificacion as err:
    print('Mensaje: ',err.mensaje3)

except Exception as err:
    print('El error es',err)