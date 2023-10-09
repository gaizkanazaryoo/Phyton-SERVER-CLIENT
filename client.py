from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def send(msg):
    message = msg.encode()
    message_length = len(message)
    send_length = str(message_length).encode()
    clientSocket.send(send_length)
    clientSocket.send(message)

n = int(input('Jumlah anggota kelompok: '))
for i in range(n):
    message = input('Masukkan Pesan: <Nama(spasi)NIM> ')

    send(message)

    # menerima pesan dari server
    modifiedMessage = clientSocket.recv(2028)
    print(modifiedMessage.decode())
    if(i == n-1):
        send('DC')
    
clientSocket.close()
