


# Event事件
#
# Event内部包含了一个标志位，初始的时候为false。
# 可以使用使用set()来将其设置为true；
# 或者使用clear()将其从新设置为false；
# 可以使用is_set()来检查标志位的状态；
# 另一个最重要的函数就是wait(timeout=None)，用来阻塞当前线程，直到event的内部标志位被设置为true或者timeout超时。如果内部标志位为true则wait()函数理解返回
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, signal):
        threading.Thread.__init__(self)
        self.singal = signal

    def run(self):
        print( "I am %s,I will sleep ..."%self.name)
        self.singal.wait()
        print( "I am %s, I awake..." %self.name)

if __name__ == "__main__":
    singal = threading.Event()
    for t in range(0, 3):
        thread = MyThread(singal)
        thread.start()

    print( "main thread sleep 3 seconds... ")
    time.sleep(3)

    singal.set()