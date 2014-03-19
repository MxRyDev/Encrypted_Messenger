from threading import Thread
import socket
import time, sys, os
import fluff
from fluff import loadBar


# initialize Variables:

HOST = ''
PORT = 50009
running_connect = True
running_msg = True
global conn, addr, msg
conn, addr = '', ''

#Create socket object called 's'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
fluff.bindPorts(.1)
s.bind((HOST, PORT))



# listen on created socket
print ("          ===Starting Listening Sequence===\n")
s.listen(5)
 

# Create empty lists to store connected IP's/Messages
clients = []


#:::::::::::::::::::::::::: DEFINE MAIN FUNCTIONS ::::::::::::::::::::::::::::
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
    #snd_and_rcv.join()
    
    time.sleep(1)
    
    fluff.unbindPorts()
    
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
    time.sleep(1)
    
    os._exit(1)
#
#


# Listens for new connections and adds new client ip's to 'clients list
def client_connect():
    while running_connect:
        try:
            print ('\n\nopen to connections...\n\n')
            conn, addr = s.accept()
            client = (conn, addr)
            print('Connected by', addr[0] + ':' + str(addr[1]))
            clients.append(client)
        except (OSError):
            break
        

              

# waits for a message and passes them onto the 'msg_send' function
def msg_snd_rcv():
    while running_msg:
        for i in clients: # !!! Problem here: Pauses at this line and waits. Only listens to first client!
            msg = i[0].recv(1024)
            msg_content = msg.decode(encoding= 'UTF-8')
            if msg:
                print('%s:\nmessage:%s' % (i[1], msg_content))
                msg_snd(i[1], msg)
                
                

# sub function of 'msg_snd_rcv';
# attempts to send messages to all clients except sender
def msg_snd(sender, msg):
    for i in clients:
        if sender != i[0]:
            s.sendto(msg, i)






#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::: RUNTIME :::::::::::::::::::::::::::::::::::::::
accept_connections = Thread(target = client_connect)
snd_and_rcv = Thread(target =  msg_snd_rcv)
time.sleep(.75)
print('\n')

#accept_connections.setDaemon(True)
accept_connections.start()
print('accepting connections...')
time.sleep(.75)
print('\n')

#snd_and_rcv.setDaemon(True)
snd_and_rcv.start()
print('handling messages...\n')
time.sleep(.75)

print('====================SERVER ONLINE====================')

while True:
    admin = input('>>')
    
    if admin == 'exit':
        shutdown(clients)
        

# List management needs a lot of work. I think we should ditch 'message_ que'.  
# its hard to tell whats going on until this is fixed. 
# The receiving & ditro of messages needs to be reworked now that everything else is cleaned up.
