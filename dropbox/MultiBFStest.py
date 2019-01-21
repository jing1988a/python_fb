import random
import time
import threading
class MultiBFS:

    def __init__(self):
        self.seed=1
        self.ans=[]
        self.lock=threading.Lock()
    def doit(self):
        q=[self.seed]
        self.ans.append(q[::])
        for i in range(5):
            p=[]
            for node in q:
                myWorker=threading.Thread(target=self.worker , args=(node , p))
                myWorker.start()
                myWorker.join()
            self.ans.append(p[::])
            q=p
            print(self.ans)

    def worker(self , node , p):
        with self.lock:
            for i in range(2):
                time.sleep(random.random()/10)
                p.append(node)

test=MultiBFS()
test.doit()
print(test.ans)


