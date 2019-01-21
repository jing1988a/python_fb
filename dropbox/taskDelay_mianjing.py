# 2： Coding. 多线程题目。 具体忘记了， 实现一个方法， def(Task task, long dealy)  task 是个interface， 有个action()方法。 用户端用调用def方法， 然后task将会在延迟后执行。里面涉及到lock, condition, notify,wait之类，小伙伴要是去面Dropbox就多看看多线程相关吧。

import threading
import time

def task():
    print('task at: '+time.strftime("%b %d %Y %H:%M:%S"))

class delayDo:

    def do(self , task , delay):
        worker=threading.Thread(target=self.worker , args=(task , delay))
        worker.start()
    def worker(self , task , delay):
        time.sleep(delay)
        task()


test=delayDo()
for i in range(3):
    for j in range(3):
        test.do(task , i)

