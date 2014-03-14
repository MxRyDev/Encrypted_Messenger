from threading import Thread
import socket
import time, sys, os


# initialize Variables:

HOST = ''
PORT = 5007
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
print ('==================TCP LOCK INITIATED==================\n')

def spinner(delay):
    for char in '/-\|':        
      sys.stdout.write("                           "+char)
      sys.stdout.flush()
      sys.stdout.write("\b" * 28)
      time.sleep(delay)

print ("                   'ENTER'to lock\n")
lock = 1
spinner(.3)
lock = input()
lock = 2
spinner(.3)
lock = input()
lock = 3
spinner(.3)
lock = input()
lock = 4
spinner(.3)
lock = input()
lock = 5
if lock == 5:
    for x in range(0,10):
        spinner(.05)
    print ("                          \ /\n")
    #print ("========================LOCKED========================\n")
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
    
    

accept_connections = Thread(target = client_connect)
snd_and_rcv = Thread(target =  msg_snd_rcv)
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
        print ('==============STARTING SHUTDOWN SEQUENCE=============')
        if clients != []:
            s.shutdown(1)
        time.sleep(1)
        print ('DISENGAGING TCP LOCK...\n')

        time.sleep(1)
        print ('UN-BINDING PORTS...\n')
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
      
        time.sleep(1)
        print ('PERFORMING CLEANUP PROCESS...\n')
        # Clearing lists
        clients = []
        message_queue = []
        time.sleep(1)
        print ('CLOSING SOCKET...\n')
        s.close()
        time.sleep(1)
        print ('goodbye.')
        
        os._exit(1)
        
        


