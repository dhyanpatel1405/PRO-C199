import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000

nick_name = input('choose your nick name:')

client.connect((ip_address,port))

print('client is ready!!!')

def recive():
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            if msg == 'nick_name':
                client.send(nick_name.encode('utf-8'))
        except:
            print('error occured , please try later!')
            client.close()
            break    


