import socket
from ai import AI

ai = AI()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 13001)
print('starting up on' + str(server_address[0]) + 'port' + str(server_address[1]))
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(1024)
            data = data.decode("utf-8")
            data = data.replace('\n', '').replace('\t','').replace('\r','').replace(';','')
            print(data)
            thought = ai.think(data)
            ai.speak(thought)
            if not data:
                print('no more data from')
                break

    finally:
        connection.close()
        print('connection closed')
