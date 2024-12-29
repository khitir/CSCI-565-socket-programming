from socket import *

serverName = 'device'  # Replace 'hostname' with the actual server name or IP address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')  # `input` is used instead of `raw_input` in Python 3
clientSocket.sendto(message.encode(), (serverName, serverPort))  # Encoding the message to bytes
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())  # Decoding the received message from bytes
clientSocket.close()
