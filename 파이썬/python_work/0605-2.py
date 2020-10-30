import threading
import time

def A():
    i = 0
    while True:        
        time.sleep(1)
        
        print("%d초" % i)

        if i >10:
            break
        i+=1

def b():
    
        
        print("B작업")
        


        
t = threading.Thread(target = A)
t1 = threading.Thread(target = b)

t.start()
t1.start()
