from socket import *
serverName = 'localhost'
serverPort = 12006
clienteSocket = socket(AF_INET,SOCK_DGRAM)
mensaje=input('Hola Mundo')
clienteSocket.sendto(mensaje.encode(),(serverName,serverPort))
mensajeModificado, serverAdrress = clienteSocket.recvfrom(2048)
print( mensajeModificado.decode())
clienteSocket.close()