from socket import *
host = ''
serverPort = 12006
dir_server = host,serverPort
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(dir_server)
print('A recibir msjs alv')

while True:
    mensaje, clienteAddress =  serverSocket.recvfrom(2048)
    mensajeModificado =  mensaje.decode().upper()
    serverSocket.sendto(mensajeModificado.encode(),clienteAddress)
    print ('Meensaje modificado')

