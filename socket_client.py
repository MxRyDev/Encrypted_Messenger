# Royce Pope
# Feb 28 2014
# Socket Client

import socket

HOST = '192.168.0.6'
PORT = 50009
#USR = input("Username?: \n>>")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('connected to %s on port %s' %(HOST, PORT))

while True:
    message = input("MESSAGE:\n>>")
    #message = USR + ': ' + message
    message = str.encode(message)   
    s.sendall(message)
    
    if s.recv(1024):
        data = s.recv(1024)
        data = data.decode(encoding = 'UTF-8')
        print('NEW MESSAGE:\n>>' + data)
    else:
        print("no new messages")
        
        
    #s.close()
