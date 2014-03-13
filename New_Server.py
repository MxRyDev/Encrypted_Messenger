from threading import Thread
import socket
import time
import sys


# initialize Variables:

HOST = ''
PORT = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
print ('====================SOCKET CREATED====================\n')

time.sleep(1)
print ("               =====Binding Ports=====") 
s.bind((HOST, PORT))

global conn, addr
conn, addr = '', ''

# listen on created socket
time.sleep(2)
print ('              >-[                   ]-<')
time.sleep(.3)
print ('              >--[                 ]--<')
time.sleep(.3)
print ('              >---[               ]---<')
time.sleep(.3)
print ('              >----[             ]----<')
time.sleep(.3)
print ('              >-----[           ]-----<')
time.sleep(.3)
print ('              >------[         ]------<')
time.sleep(.3)
print ('              >-------[       ]-------<')
time.sleep(.3)
print ('              >--------[     ]--------<')
time.sleep(.3)
print ('              >---------[   ]---------<')  
time.sleep(.3)
print ('              >----------[ ]----------<')
time.sleep(.3)
print ('              >----------[=]----------<\n')
time.sleep(.5)
print ('=================Socket Bind Complete=================\n')
time.sleep(1)
print ("          ===Starting Listening Sequence===\n")
s.listen(5)

def listeningthread(s):
    while True:
        for i in range(10):
            print("Listening" + "." * i)
            sys.stdout.write("\033[F") # Cursor up one line
            time.sleep(1)
        if i == 9:
            #sys.stdout.write("\033[F")
            sys.stdout.write("                   ")
            i = 0
            listeningthread(s)

# Need to convert this to Python3            
#start_new_thread(listeningthread,(s,)) 

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
        
        


