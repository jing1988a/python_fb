#
# Semaphore 信号量对象
#
# 信号量是一个更高级的锁机制。信号量内部有一个计数器而不像锁对象内部有锁标识，而且只有当占用信号量的线程数超过信号量时线程才阻塞。这允许了多个线程可以同时访问相同的代码区。
#
# Semaphore管理一个内置的计数器，每当调用acquire()时内置计数器-1；调用release() 时内置计数器+1；
#
# 计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程调用release()。
#
# 直接上代码，我们把semaphore控制为3，也就是说，同时有3个线程可以用这个锁，剩下的线程也之只能是阻塞等待了…

import threading , time
semaphore=threading.Semaphore(3)

def test():
    if semaphore.acquire():
        for i in range(3):
            time.sleep(1)
            print(threading.current_thread().getName()+'获取锁')
        semaphore.release()
        print(threading.currentThread().getName() + ' 释放锁')


for i in range(5):
  t1 = threading.Thread(target=test)
  t1.start()