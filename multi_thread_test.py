from time import sleep
from threading import Thread

class worker(Thread):
    def run(self):
        for x in range(0,11):
            print(x)
            sleep(1)
            

class waiter(Thread):
    def run(self):
        for x in range(100,105):
            print(x)
            sleep(3)

def run():
    worker().start()
    waiter().start()

    
run()

print('hello, world')
