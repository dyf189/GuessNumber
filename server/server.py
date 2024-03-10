import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',4514))
server_socket.listen(5)
print('GuessNumber Server is running\nChinese(简体中文):猜数服务器已开启')

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024).decode('utf-8')
    while True:
        if data == '1':
          print('[info]' , data)
          client_socket.send(b'true')
          ndnum1 = '1'
          data = client_socket.recv(1024).decode('utf-8')
        elif data == '20':
            print('[info]' , data)
            client_socket.send(b'true')
            ndnum2 = '20'
            data = client_socket.recv(1024).decode('utf-8')
            break
        else:
            data = client_socket.recv(1024).decode('utf-8')
            print('[info]' + str('“') + data + str('”加入了游戏'))
            client_socket.send(b'true')
            username = data
            
            
    
