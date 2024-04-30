import socket
import os

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
    client_socket.send(num2.encode('utf-8'))
    接收信息 = client_socket.recv(1024).decode('utf-8')
    while True:
        if 接收信息 == 'true':
            break
        else:
            client_socket.send(num2.encode('utf-8'))
            接收信息 = client_socket.recv(1024).decode('utf-8')

def dl(name):
    client_socket.send(name.encode('utf-8'))
    接收信息 = client_socket.recv(1024).decode('utf-8')
    while True:
        if 接收信息 == 'true':
            print('发送成功')
            os.system('pause')
            break
        else:
            print('发送失败，请检查网络或在 https://github.com/dyf189/GuessNumber 报issuse')
            接收信息 = client_socket.recv(1024).decode('utf-8')
            os.system('pause')