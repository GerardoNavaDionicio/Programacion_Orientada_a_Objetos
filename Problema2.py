lista=["BIOTECNOLOGIA","MECATRONICA","SISTEMAS AUTOMOTRICES","FINANCIERA", "ELECTRONICA Y TELECOMUNICACIONES", "INDUSTRIAL", "TECNOLOGIAS DE LA INFORMACION"]
ciclo = 0
pregunta=str(input("Eres un estudiante? "))
while(not ciclo):
    if(pregunta.upper()=="SI"):
        respuesta=input("Qué carrera estudias?  ")
    else:
        respuesta = input("Qué carrera te gustaría estudiar en la UPPue?  ")
    i=lista.count(respuesta.upper())
    if(i==1):
        ciclo=1
    else:
        print("Esa carrera no la tenemos")
print("Carrera correcta")
