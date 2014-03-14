from threading import Thread
from multiprocessing import Process
import socket
import time, sys, os


# initialize Variables:

HOST = ''
PORT = 56835
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
toolbar_width = 40
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
print ('==================TCP LOCK INITIATED==================\n')
time.sleep(1)
print ("                    ##############")
print ("                    ####LOCKED####")
print ("                    ##############")
time.sleep(1)    
print ('==================Port Bind Complete==================\n')
time.sleep(1)
print ("          ===Starting Listening Sequence===\n")
s.listen(5)

def listening(s):
    while True:
        for i in range(10):
            print("Listening" + "." * i)
            sys.stdout.write("\033[F") # Cursor up one line
            time.sleep(1)
        if i == 9:
            #sys.stdout.write("\033[F")
            sys.stdout.write("                   ")
            i = 0
            listening(s)
            
#listening_thread = Thread(target=listening(s))
#listening_thread.start()


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
        print('Connected by', addr[0] + ':' + str(addr[1]))
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
        
    
    

accept_connections = Process(target = client_connect)
snd_and_rcv = Process(target =  msg_snd_rcv)
time.sleep(1)
print('\n')

accept_connections.start()
print('accepting connections...')
time.sleep(1)
print('\n')

snd_and_rcv.start()
print('handling messages...\n')
time.sleep(1)

print('====================SERVER ONLINE====================')

while True:
    admin = input('>>')
    
    if (admin == 'close') or (admin == 'exit'):
        print ('==============STARTING SHUTDOWN SEQUENCE=============\n')
        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

        for i in range(toolbar_width):
            time.sleep(0.05)
            # update the bar
            sys.stdout.write("#")
            sys.stdout.flush()

        sys.stdout.write("\n")
        if clients != []:
            s.shutdown(1)
        time.sleep(1)
        
        print ('\nDISENGAGING TCP LOCK...\n')
        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))

        for i in range(toolbar_width):
            time.sleep(0.01)
            # update the bar
            sys.stdout.write("#")
            sys.stdout.flush()

        sys.stdout.write("\n")
        snd_and_rcv.terminate()
        time.sleep(1)
        
        print ('\nUN-BINDING PORTS...\n')
        print ('              >----------[=]----------<')
        time.sleep(.1)
        print ('              >----------[ ]----------<')
        time.sleep(.1)
        print ('              >---------[   ]---------<')
        time.sleep(.1)
        print ('              >--------[     ]--------<')
        time.sleep(.1)
        print ('              >-------[       ]-------<')
        time.sleep(.1)
        print ('              >------[         ]------<')
        time.sleep(.1)
        print ('              >-----[           ]-----<')
        time.sleep(.1)
        print ('              >----[             ]----<')
        time.sleep(.1)
        print ('              >---[               ]---<')
        time.sleep(.1)
        print ('              >--[                 ]--<')
        time.sleep(.1)
        print ('              >-[                   ]-<')
        accept_connections.terminate()
        time.sleep(1)
        print ('\nPERFORMING CLEANUP PROCESS...\n')
        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))

        for i in range(toolbar_width):
            time.sleep(0.03)
            # update the bar
            sys.stdout.write("#")
            sys.stdout.flush()

        sys.stdout.write("\n")
        # Clearing lists
        clients = []
        message_queue = []
        time.sleep(1)
        
        print ('\nCLOSING SOCKET...\n')
        s.close()
        time.sleep(1)
        print ('goodbye.')
        
        os._exit(1)
        
        


