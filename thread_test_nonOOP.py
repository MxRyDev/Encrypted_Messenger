from threading import Thread
import time

threadBreak = False
def Timer_function():
    while not threadBreak:
        print(time.time() - startTime)
        time.sleep(1)
        
        

startTime = time.time()

timer_function = Thread(target = TimeProcess)
timer_function.start()

input()
threadBreak = True

timer_function.join()

print('PROCESS ENDED BY USER')
