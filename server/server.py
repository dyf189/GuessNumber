import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',4514))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    client_socket.send(b'true')
    
