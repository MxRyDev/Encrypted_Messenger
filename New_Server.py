from threading import Thread
import socket
import sys


# initialize Variables:

HOST = ''
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.bind((HOST, PORT))

global conn, addr
conn, addr = '', ''

# listen on created socket
s.listen(5)


print ("Socket Created")


# Create empty lists to store connected IP's/Messages
clients = []
message_queue = []

# Will run on its own thread, listening for new connections,
# and adding connecting ip's to 'clients' list.
def client_connect():
    while True:
        print ("Socket Listening...")
        conn, addr = s.accept()
        print('Connected by', addr)
        clients.append(conn)
        
        
def msg_snd(sender, msg):
    for client in clients:
        if sender != client:
            sender.send(msg)
        
        
def msg_snd_rcv():
    
    while True:
        for client in clients:
            msg = client.recv(1024)
            msg = msg.decode(encoding= 'UTF-8')
            if message:
                print('Message recieved from %s:\n%s' % (client, msg))
                messages.append((sender, msg))
            for message in msg:
                msg_snd(message)
    


accept_connections = Thread(target = client_connect)
snd_and_rcv = Thread(target =  msg_snd_rcv)

accept_connections.start()
print('accepting connections...')

snd_and_rcv.start()
print('handling messages...')


print('Server fully operational')

while True:
    admin = input('>>')
    
    if admin == 'close':
        quit()
        
        


