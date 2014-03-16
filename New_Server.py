from threading import Thread
import socket
import time, sys, os
import fluff
from fluff import loadBar


# initialize Variables:

HOST = ''
PORT = 5009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
running_connect = True
running_msg = True
print ('====================SOCKET CREATED====================\n')

time.sleep(1)
print ("               =====Binding Ports=====") 
s.bind((HOST, PORT))

global conn, addr
conn, addr = '', ''

# listen on created socket
fluff.bindPorts()

print ("          ===Starting Listening Sequence===\n")
s.listen(5)
 

# Create empty lists to store connected IP's/Messages
clients = []
message_queue = []
# Will run on its own thread, listening for new connections,
# and adding connecting ip's to 'clients' list.
def client_connect():
    while running_connect:
        try:
            print ("Socket Listening...")
            conn, addr = s.accept()
            print('Connected by', addr[0] + ':' + str(addr[1]))
            clients.append(conn)
        except (OSError):
            pass
        
        
        
def msg_snd(sender, msg):
    for client in clients:
        if sender != client:
            sender.send(msg)
            
        
        
def msg_snd_rcv():
    while running_msg:
        for client in clients:
            msg = client.recv(1024)
            msg = msg.decode(encoding= 'UTF-8')
            if message:
                print('Message recieved from %s:\n%s' % (client, msg))
                messages.append((sender, msg))
            for message in msg:
                msg_snd(message)
                
                
def shutdown(connected_users):
    print ('==============STARTING SHUTDOWN SEQUENCE=============\n')
    # setup toolbar with 0.05s
    loadBar(0.05)
    
    if connected_users:
        s.shutdown(1)
    time.sleep(1)
    
    print ('\nDISENGAGING TCP LOCK...\n')
    # setup toolbar with 0.01
    loadBar(0.01)
    
    #Stop the msg_snd_rcv Thread
    running_msg = False
    snd_and_rcv.join()
    
    time.sleep(1)
    
    unbindPorts()
    
    #stop the accept_connections Thread
    running_connect = False
    
    time.sleep(1)
    print ('\nPERFORMING CLEANUP PROCESS...\n')
    # setup toolbar with 0.03s
    loadBar(0.03)
    
    # Clearing lists
    clients = []
    message_queue = []
    time.sleep(1)
    
    print ('\nCLOSING SOCKET...\n')
    s.close()
    time.sleep(1)
    print ('goodbye.')
    
    os._exit(1)
        
    
    


#::::::::::::::::::::::::::::::: RUNTIME ::::::::::::::::::::::::::::::::::::::::::::::::::
accept_connections = Thread(target = client_connect)
snd_and_rcv = Thread(target =  msg_snd_rcv)
time.sleep(1)
print('\n')

#accept_connections.setDaemon(True)
accept_connections.start()
print('accepting connections...')
time.sleep(1)
print('\n')

#snd_and_rcv.setDaemon(True)
snd_and_rcv.start()
print('handling messages...\n')
time.sleep(1)

print('====================SERVER ONLINE====================')

while True:
    admin = input('>>')
    
    if admin == 'exit':
        shutdown(clients)
        

