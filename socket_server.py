# Royce Pope
# Feb 28 2014
# Socket Test

import socket


HOST = ''             
PORT = 50005              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while True:
    s.listen(1)
    conn, addr = s.accept()
    print ("Connected by", addr)
    data = conn.recv(1024)
    data = data.decode(encoding='UTF-8')
    if data:
        print (data)
        data = str.encode(data)
        conn.sendall(data)
        data = ""
    

    
