# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch06s04.html
# Problem
# You need to allow unlimited read access to a resource when it is not being modified while keeping write access exclusive.
#
# Solution
# “One-writer, many-readers” locks are a frequent necessity, and Python does not supply them directly. As usual, they’re not hard to program yourself, in terms of other synchronization primitives that Python does supply:
#
# import threading
#
# class ReadWriteLock:
#     """ A lock object that allows many simultaneous "read locks", but
#     only one "write lock." """
#
#     def _ _init_ _(self):
#         self._read_ready = threading.Condition(threading.Lock(  ))
#         self._readers = 0
#
#     def acquire_read(self):
#         """ Acquire a read lock. Blocks only if a thread has
#         acquired the write lock. """
#         self._read_ready.acquire(  )
#         try:
#             self._readers += 1
#         finally:
#             self._read_ready.release(  )
#
#     def release_read(self):
#         """ Release a read lock. """
#         self._read_ready.acquire(  )
#         try:
#             self._readers -= 1
#             if not self._readers:
#                 self._read_ready.notifyAll(  )
#         finally:
#             self._read_ready.release(  )
#
#     def acquire_write(self):
#         """ Acquire a write lock. Blocks until there are no
#         acquired read or write locks. """
#         self._read_ready.acquire(  )
#         while self._readers > 0:
#             self._read_ready.wait(  )
#
#     def release_write(self):
#         """ Release a write lock. """
#         self._read_ready.release(  )
# Discussion
# It is often convenient to allow unlimited read access to a resource when it is not being modified and still keep write access exclusive. While the threading module does not contain a specific class for the job, the idiom is easy to implement using a Condition object, and this recipe shows how you can do that.
#
# An instance of the ReadWriteLock class is initialized without arguments, as in:
#
# rw = ReadWriteLock(  )
# Internally, rw._readers counts the number of readers who are currently in the read-write lock (initially zero). The actual synchronization is performed by a threading.Condition object (created at _ _init_ _ around a new Lock object and held in rw._read_ready).
#
# The acquire_read and release_read methods increment and decrement the number of active readers. Of course, this happens between acquire and release calls to _read_ready—such bracketing is obviously necessary even to avoid race conditions between different threads wanting to acquire or release a read lock. But we also exploit _read_ready for another purpose, which is why release_read also does a notifyAll on it, if and when it notices it has removed the last read lock.
#
# The notifyAll method of a Condition object wakes up all threads (if any) that are on a wait condition on the object. In this recipe, the only way a thread can get into such a wait is via the acquire_write method, when it finds there are readers active after acquiring _read_ready. The wait call on the Condition object releases the underlying lock, so release_read methods can execute, but reacquires it again before waking up, so acquire_write can safely keep checking whenever it wakes up, if it’s finally in a no-readers-active situation. When that happens, acquire_write returns to its caller, but keeps the lock, so no other writer or reader can enter again, until the writer calls release_write, which lets the lock go again.
#
# Note that this recipe offers no guarantee against what is technically known as a starvation situation. In other words, there is no guarantee that a writer won’t be kept waiting indefinitely by a steady stream of readers arriving, even if no reader keeps its read lock for very long. If this is a problem in your specific application, you can avoid starvation by adding complications to ensure that new readers don’t enter their lock if they notice that a writer is waiting. However, in many cases, you can count on situations in which no readers are holding read locks, without special precautions to ensure that such situations occur. In such cases, this recipe is directly applicable, and besides eschewing complications, it avoids potentially penalizing reader performance by making several readers wait for one pending writer.



import threading

# class ReadWriteLock:
#     """ A lock object that allows many simultaneous "read locks", but
#     only one "write lock." """
#
#     def __init__(self):
#         self._read_ready = threading.Condition(threading.Lock())
#         self._readers = 0
#
#     def acquire_read(self):
#         """ Acquire a read lock. Blocks only if a thread has
#         acquired the write lock. """
#         self._read_ready.acquire(  )
#         try:
#             self._readers += 1
#         finally:
#             self._read_ready.release(  )
#
#     def release_read(self):
#         """ Release a read lock. """
#         self._read_ready.acquire(  )
#         try:
#             self._readers -= 1
#             if not self._readers:
#                 self._read_ready.notifyAll(  )
#         finally:
#             self._read_ready.release(  )
#
#     def acquire_write(self):
#         """ Acquire a write lock. Blocks until there are no
#         acquired read or write locks. """
#         self._read_ready.acquire(  )
#         while self._readers > 0:
#             self._read_ready.wait(  )
#
#     def release_write(self):
#         """ Release a write lock. """
#         self._read_ready.release(  )


class ReadWriteLock: #Efficient but could lead write starving
    def __init__(self):
        self.condition=threading.Condition()
        self.curReader=0
    def acquire_read(self):
        with self.condition:
            self.curReader+=1
        # self.condition.acquire()
        # try:
        #     self.curReader += 1
        # finally:
        #     self.condition.release()
    def release_read(self):
        with self.condition:
            self.curReader -=1
            if self.curReader==0:
                self.condition.notifyAll()

    def acquire_write(self):
        self.condition.acquire() # 应为reader每次都会release 所以这个锁肯定拿得到. 要有个wait() 让他停下来释放锁.. 所以用condition 不用最基本的lock
        if self.curReader>0:
            self.condition.wait()

    def release_write(self):
        self.condition.release()



class ReadWriteLock2: #not Efficient but better for write starving
    def __init__(self):
        self.condition=threading.Condition()
        self.curReader=0
        self.curWriter=0
    def acquire_read(self):
        self.condition.acquire()
        try:
            if self.curWriter>0:
                self.condition.wait()
            self.curReader += 1
        finally:
            self.condition.release()
    def release_read(self):
        with self.condition:
            self.curReader -=1
            if self.curReader==0:
                self.condition.notifyAll()

    def acquire_write(self):
        self.condition.acquire()
        self.curWriter+=1
        if self.curReader>0:
            self.condition.wait()

    def release_write(self):
        self.curWriter-=1
        self.condition.notifyAll()
        self.condition.release()


import time
class Readme:
    def __init__(self , data):
        self.data=data
        self.RWlock=ReadWriteLock()
    def read(self):
        self.RWlock.acquire_read()
        print(self.data)
        time.sleep(2)
        self.RWlock.release_read()
    def write(self ,data):
        self.RWlock.acquire_write()
        self.data=data
        print('write data to:'+data)
        time.sleep(2)
        self.RWlock.release_write()



test=Readme('abcdef')
for i in range(3):
    #a=threading.Thread(target=test.read())  不要加括号 加括号就是直接 call 这个method 而不是创建一个thread 来call 这个method 了
    #b=threading.Thread(target=test.read())  不要加括号 加括号就是直接 call 这个method 而不是创建一个thread 来call 这个method 了
    #c = threading.Thread(target=test.write(str(i)))
    a=threading.Thread(target=test.read)
    b=threading.Thread(target=test.read)
    c=threading.Thread(target=test.write,  args=(str(i) ,))
    a.start()
    b.start()
    c.start()
    # a.join()
    # b.join()
    # c.join()
    time.sleep(1)
