import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 4514))

def nd(num1,num2):
    #(难度1，难度2)
    client_socket.send(num1.encode('utf-8'))
    接收信息 = client_socket.recv(1024).decode('utf-8')
    while True:
        if 接收信息 == 'true':
            break
        else:
            client_socket.send(num1.encode('utf-8'))
            接收信息 = client_socket.recv(1024).decode('utf-8')
    接收信息 = client_socket.recv(1024).decode('utf-8')
    client_socket.send(num2.encode('utf-8'))
    while True:
        if 接收信息 == 'true':
            break
        else:
            client_socket.send(num2.encode('utf-8'))
            接收信息 = client_socket.recv(1024).decode('utf-8')
