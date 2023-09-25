from multiprocessing import Process
from threading import Thread
import time #-
import random #-
#-
shared_x = random.randint(10,99)
#-

def sleeping(name):
    global shared_x
    x = 0.0
    t = time.gmtime() #-
    s = random.randint(1,20)
    txt = str(t.tm_min)+':'+str(t.tm_sec)+' '+name+' is going to sleep for '+str(s)+' seconds' #-
    print(txt) #-
    t = time.time()
    c = s * 8000000
    for i in range(c):
        x = x + 1.0
    print(time.time()-t)
    t = time.gmtime() #-
    shared_x = shared_x + 1
    txt = str(t.tm_min)+':'+str(t.tm_sec)+' '+name+' has woken up, seeing shared x being '+str(shared_x) #-
    print(txt) #-


def sleeper(name):
    sleeplist = list()
    print(name, 'sees shared x being', shared_x) #-
    for i in range(3):
        subsleeper = Thread(target=sleeping, args=(name+' '+str(i),))
        sleeplist.append(subsleeper)

    for s in sleeplist:
        s.start()
    for s in sleeplist:
        s.join()
    print(name, 'sees shared x being', shared_x) #-
#-        
if __name__ == '__main__': #-
    p = Process(target=sleeper, args=('eve',)) #-
    q = Process(target=sleeper, args=('bob',)) #-
    p.start() #-
    q.start() #-
    p.join()  #-
    q.join()  #-

