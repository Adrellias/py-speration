import multiprocessing as mp
from lib import comic
import time


def job_engine(que):
    """ Handle jobs multi """
    if que == 2:
        print que
        while True:
            pass
    time.sleep(que)
    print que

    """
    while True:
        data = que.get()
        if data == None:
            break
        else:
            print data
    """

if __name__=="__main__":
    """ Setting up some process'es to handle our database updates.
    We will only be moving the image grab bits to a process for now """

    for i in range(1,10):
        mp.Process(target=job_engine,args=(i,)).start()

"""
    que = mp.Queue()
    jobs = mp.Process(name="JobEngine", target=job_engine, args=(que,))
    jobs.daemon = True
    jobs.start()
    for i in range(1,10):
        que.put(i) 
    jobs.join(3)
    que.put(None)
"""
