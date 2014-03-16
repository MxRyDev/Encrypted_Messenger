# Royce Pope
# March 15 2014
# Fluff

import time, sys, os



toolbar_width = 40
delay = int()

def bindPorts():
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
    print ("                    ##############\n")
    time.sleep(1)    
    print ('==================Port Bind Complete==================\n')
    time.sleep(1)


def loadBar(delay):
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(delay)
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("\n")
    
    
def unbindPorts():
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

def shutdown():
    print ('==============STARTING SHUTDOWN SEQUENCE=============\n')
    # setup toolbar with 0.05s
    loadBar(0.05)
    
    if clients != []:
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


