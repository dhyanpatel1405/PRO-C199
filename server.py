import socket
from threading import Thread

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000

server.bind((ip_address,port))
server.listen()
print('server is ready!!!')

list_of_client = []
def client_thread(conn,addr):
    conn.send('Welcome Everybody'.encode('utf-8'))
break
def remove(connection):
    if connection in list_of_client:
        list_of_client.remove(connection)
