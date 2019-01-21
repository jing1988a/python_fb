# 近段时间发现一个 Python 连接数据库的连接是线程不安全的，结果惹得我哪哪儿都怀疑变量的多线程是否安全的问题，今天终于找到了正确答案，那就是 Python 内置类型 dict，list ，tuple 是线程安全的。
#
# 请参考官方解释: http://docs.python.org/glossary.html#term-global-interpreter-lock
# ---------------------
# 作者：独一无二的小个性
# 来源：CSDN
# 原文：https://blog.csdn.net/u010649766/article/details/79740873
# 版权声明：本文为博主原创文章，转载请附上博文链接！

'''多线程安全机制--使用锁 threading.Lock()
从程序逻辑角度，python和java的多线程安全机制都可以使用锁机制，且简单易用
'''

import threading #导入线程包
import time  #导入时间包，用于睡眠线程，方便演示效果

#创建两个同样的函数，直观对比不使用锁机制，两个线程同时进行（并行执行）
def meituan():
    for x in range(5):
        print('meituan:' +str(x))
        time.sleep(0.01) #线程睡眠0.01秒
def didi():
    for x in range(5):
        print('didi:' +str(x))
        time.sleep(0.01)  #线程睡眠0.01秒
meituan = threading.Thread(target = meituan)
didi = threading.Thread(target = didi)
meituan.start() #开启线程a
didi.start() #开启线程b
'''
输出结果：
meituan:0
didi:0
meituan:1
didi:1
didi:2
meituan:2
meituan:3
didi:3
didi:4
meituan:4
'''


#使用锁，使得两个线程按照次序执行，先meituan后didi(先didi后meituan也可以)
lock = threading.Lock() #调用线程锁方法 使用同一个锁的线程，当前线程释放锁后，另一个才能开始执行

def meituan():
    lock.acquire()  #加锁
    for x in range(5):
        print('meituan:'+str(x))
        time.sleep(0.01)
    lock.release()  #释放锁
def didi():
    lock.acquire()
    for x in range(5):
        print('didi:'+str(x))
        time.sleep(0.01)
    lock.release()

meituan = threading.Thread(target = meituan)
didi = threading.Thread(target = didi)
meituan.start()
didi.start()

'''
输出结果：
meituan:0
meituan:1
meituan:2
meituan:3
meituan:4
didi:0
didi:1
didi:2
didi:3
didi:4

---------------------
作者：mmmdotes
来源：CSDN
原文：https://blog.csdn.net/niutianzhuang/article/details/79821801
版权声明：本文为博主原创文章，转载请附上博文链接！
'''