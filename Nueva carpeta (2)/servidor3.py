from socket import *
serverName = 'localHost'
serverPort = 12007
direccionCliente = serverName,serverPort
clienteTCPsocket =  socket(AF_INET,SOCK_STREAM)
mensajeTCP = input('Ingresa una frase')
clienteTCPsocket.send(mensajeTCP.encode())
mensajeTCPModificado= clienteTCPsocket.recv(1024)
print('Mensaje enviado desde el server',mensajeTCPModificado.decode())
clienteTCPsocket.close()
print('socket cerrado')
