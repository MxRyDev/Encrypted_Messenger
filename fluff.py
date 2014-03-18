# Royce Pope
# March 15 2014
# Fluff

import time, sys, os



toolbar_width = 40
delay = int()

# FROM MAX:
'''
I sped up this function in general, 
I also added an argument that controls the pauses in the animation.
this is now controled when the function is called in the server script
(Currently set to .1)
'''
def bindPorts(t):
    print ('====================SOCKET CREATED====================\n')
    time.sleep(.5)
    print ('               =====Binding Ports=====')     
    time.sleep(.5)
    print ('              >-[                   ]-<')
    time.sleep(t)
    print ('              >--[                 ]--<')
    time.sleep(t)
    print ('              >---[               ]---<')
    time.sleep(t)
    print ('              >----[             ]----<')
    time.sleep(t)
    print ('              >-----[           ]-----<')
    time.sleep(t)
    print ('              >------[         ]------<')
    time.sleep(t)
    print ('              >-------[       ]-------<')
    time.sleep(t)
    print ('              >--------[     ]--------<')
    time.sleep(t)
    print ('              >---------[   ]---------<')  
    time.sleep(t)
    print ('              >----------[ ]----------<')
    time.sleep(t)
    print ('              >----------[=]----------<\n')
    time.sleep(.3)
    print ('==================TCP LOCK INITIATED==================\n')
    time.sleep(.5)
    print ("                    ##############")
    print ("                    ####LOCKED####")
    print ("                    ##############\n")
    time.sleep(.5)    
    print ('==================Port Bind Complete==================\n')
    time.sleep(.5)


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



