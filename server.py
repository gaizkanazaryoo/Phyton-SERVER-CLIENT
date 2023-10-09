from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

print("[SERVER] Server is Starting..")

while True:
    serverSocket.listen()
    print("[SERVER] The Server is wait for connection..")
    connection, clientAddress = serverSocket.accept()
    print("[SERVER] Got connection from", clientAddress)

    connected = True

    while connected:
        message_length = connection.recv(2048).decode()
        message_length = int(message_length)
        message = connection.recv(message_length).decode()
        if (message == "DC"):
            connected = False
        else:
            print(f"[{clientAddress}]",message)

            #sendback
            connection.send(("[SERVER] Pesan diterima: "+ message + "\n").encode())

        if(connected == False):
            print("[SERVER] Connection from "+str(clientAddress[0])+ ":"+ str(clientAddress[1])+ ' is disconnected\n')

        connection.close()


