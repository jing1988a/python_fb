#
#
# import random
# import collections
# import threading
#
# class Mylock():
#     def __init__(self):
#         self.condition=threading.Condition()
#         self.curGet=0
#     def acquireGet(self):
#         with self.condition:
#             self.curGet+=1
#     def releaseGet(self):
#         with self.condition:
#             self.curGet-=1
#             if self.curGet==0:
#                 self.condition.notifyAll()
#     def acquirePut(self):
#         self.condition.acquire()
#         if self.curGet>0:
#             self.condition.wait()
#     def releasePut(self):
#         self.condition.release()
#
#
# class KVTstore:
#     def __init__(self):
#         self.data=collections.defaultdict(dict)
#         self.myLock=Mylock()
#     #def begin(self):
#     #    return random.randint(0 , 100)
#
#     def put(self ,  trasactionId , k , v):
#         self.myLock.acquirePut()
#         try:
#             self.data[k][trasactionId]=v
#         finally:
#             self.myLock.releasePut()
#
#     def get(self , trasactionId  , k ):
#         self.myLock.acquireGet()
#         try:
#             if k not in self.data:
#                 return False
#             if trasactionId not in self.data[k]:
#                 return False
#             return self.data[k][trasactionId]
#         finally:
#             self.myLock.releaseGet()
#     #def commit(self):
#
#
# test=KVTstore()
# test.put(1 , 1 , 1)
# test.put(2 , 1 , 2)
# print(test.get(2 , 1))
# print(test.get(1 , 1))
# print(test.get(3 , 1))


# 想法不错 但是人家问的不是上面这种

#
# KV Store这道题的问题是设计一个transaction， 有一个start() 方法，
#  返回一个transaction id. 有一个put(transactionId, String key, int value),
# 有一个get(transactionId, String key), 和一个commit(transactionID)。
#  要理解这道题到底什么意思， 首先得先翻翻Database的书， 看下transaction那一章，
# transaction的四个属性ACID。 主要是Isolation level。 transaction有四个level， Read Uncommitted, Read Committed, Repeatable Read和Serializable。
#  根据面试官的要求， 你要实现其中的一个level， 比如面试官如果说这个transaction会用在bank system里面，
#  那么最好就是实现Repeatable Read那个level。 因为这个level可以避免dirty reads, non-repeatable reads, and lost updates。
# 想象下如果有两个transaction以下面这个顺序进行读写(假设a之前的值为1)
# start()  // start transaction 1
# start() // start transaction 2
# int val1 = get(1, "a");
# int val2 = get(2, "a");
# put(1, "a", val1+1);
# put(2, "a", val2+1);
# commit(1);
# commit(2);
# 那么transaction 1的操作就会overwritten， 这个就是update lost。
# 解决update lost就需要实现repeatable read， 意思就是当一个transaction得到一个key的读的lock时， 要一直hold这个lock到这个transaction结束为止。 这样一来当例子中的第二个transaction要读a的时候就会被拒绝。 根据面试官的要求， 一般会直接throw一个error然后把第二个transaction取消掉（rollback之前所有已做过的操作）。
#  还有一点要注意的是， 这其实是一个单线程题， 所以不需要考虑多线程， 比如上一个例子中所有code都是有时间先后顺序的， 因为他们都发生在同一个thread里。
# 至于在实现锁的这块， 可以使用Map来记录当前哪些key已经有读的锁， 哪些有写的锁。 如果一个key已经有读的锁， 那么其他transaction只能获得读的锁，
# 如果一key已经有写的锁， 那么其他transaction不能再获得读或写的锁。 还有一点要注意的是，
#  一个key上的锁如果只有一个transaction并且此时要求锁的那个transaction就是holding锁的那个transaction，
#  那么这个transaction的读或写应该被允许。 如果一个transaction之前改变了一个值， 在后来的操作发现有conflict， 那么要把这个transaction之前修改过的值都改回原先值。
# 比如说有这些操作，
# start()  // start transaction 1
# start() // start transaction 2
# int val1 = get(1, "a");
# put(2, "b", 2);
# put(2, "a", 2);
# commit(1);
# commit(2);
#
# 当transaction 2 改b的值时， b的值可以被成功修改， 但是当transaction 2 修改a的值时，因为此时a的lock已经被transaction 1 hold， 所以这里有一个conflict， 所以transaction 2要被cancel掉。这里可以用一个Map来记录一个key和它原先的值， 每一个transaction都有一个这样的map。 当发现一个transaction需要被cancel时， 把这个transaction之前改过的所有key都要恢复原来的值。这道题的基本就是这个意思了。面试的时候要跟面试官讨论到底要实现那种isolation level。 isolation level越高越复杂。

import collections
import random
class KVstore:
    def __init__(self):
        self.trasactionActionMap=collections.defaultdict(list)
        self.locks=dict()
        self.counter=0
        self.data=dict()
    def begin(self):
        self.counter+=1
        return self.counter
    def put(self , trasactionId , k , v):
        if k in self.locks and self.locks[k]!=trasactionId:
            self.rollback(trasactionId)
            return
        if not k in self.locks:
            self.locks[k]=trasactionId
        oldV=None
        if k in self.data:
            oldV=self.data[k]
        self.trasactionActionMap[trasactionId].append(['put', k, oldV])
        self.data[k]=v

    def get(self , trasactionId , k):
        if k not in self.data:
            return None
        if self.locks[k] and self.locks[k]!=trasactionId:
            self.rollback(trasactionId)
            return
        if not self.locks[k]:
            self.locks[k]=trasactionId

        self.trasactionActionMap[trasactionId].append(['get', k, None])
        return self.data[k]
    def commit(self, trasactionId  ):
        for action , k , v in self.trasactionActionMap[trasactionId]:
            if k in self.locks:
                del self.locks[k]
        del self.trasactionActionMap[trasactionId]
    def rollback(self , transactionId):
        # if not transactionId in self.trasactionActionMap:
        #     raise Exception('unable to find transactionId: '+str(transactionId))
        while self.trasactionActionMap[transactionId]:
            action, k, v=self.trasactionActionMap[transactionId].pop()
            if k in self.locks:
                print(k)
                print(self.locks)
                del self.locks[k]
            if action=='put':
                if v==None:
                    del self.data[k]
                else:
                    self.data[k]=v
        del self.trasactionActionMap[transactionId]
        print('conflict found, transaction canceled and rollback , please start a new one')

test=KVstore()
idx1=test.begin()
idx2=test.begin()

test.put(1 , 'a' , 1)
# print(test.trasactionActionMap)
# print(test.locks )
# print(test.counter )
# print(test.data)
# print(' ')



val1 = test.get(1, "a")
# print(test.trasactionActionMap)
# print(test.locks )
# print(test.counter )
# print(test.data)
# print(' ')


val2 = test.put(2, "b" , 2)
# print(test.trasactionActionMap)
# print(test.locks )
# print(test.counter )
# print(test.data)
# print(' ')


val2 = test.get(2, "a" )
# print(test.trasactionActionMap)
# print(test.locks )
# print(test.counter )
# print(test.data)
# print(' ')

test.put(1, "a", val1+1)
# print(test.trasactionActionMap)
# print(test.locks )
# print(test.counter )
# print(test.data)
# print(' ')


test.commit(1)
print(test.trasactionActionMap)
print(test.locks )
print(test.counter )
print(test.data)
print(' ')

# test.commit(2)