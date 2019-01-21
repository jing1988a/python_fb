import threading
import time
class TokenBucketwithProducer:
    def __init__(self , max_capacity , fill_rate):
        self._timeInterval=1/fill_rate
        self._maxCapacity=max_capacity
        self._tokens=0
        self.lock=threading.Lock()
        self.signal = True
        # self.producer=threading.Thread(target=self.producer()  )
        self.producer = threading.Thread(target=self.producer , daemon=True) # 学到了没!!!!!
        self.producer.start()
        #self.producer.join()
    # def producer(self):
    #     with self.lock:
    #         while self.signal:
    #             if self._tokens<self._maxCapacity:
    #                 self._tokens+=1
    #             time.sleep(self._timeInterval)
    #             print(self._tokens)
    # 上面这个直接就整个锁住了 会一直在这个while 里出不来
    def producer(self):
        while self.signal:
            if self._tokens < self._maxCapacity:
                with self.lock:
                    self._tokens+=1
            time.sleep(self._timeInterval)
            print(self._tokens)


    def getToken(self , tokenNeed):
        self.lock.acquire()
        print('try get token')
        if self._tokens>=tokenNeed:
            self._tokens-=tokenNeed
            #print(self._tokens)
            self.lock.release()
            return True
    #print(self._tokens)
        self.lock.release()
        return False

    def stopProducer(self):
        self.signal=False

# bucket=TokenBucketwithProducer(10 , 2)
# time.sleep(2)
# bucket.getToken(2)
# time.sleep(2)
# bucket.getToken(3)
# time.sleep(2)
# bucket.getToken(3)



# import unittest
# class TestBucket(unittest.TestCase):
#     def setUp(self):
#         self.bucket=TokenBucketwithProducer()
#     def testCase1(self):
#         self.assertEqual()


# question , whtn bucket is initialized , is it full or empty?

class TokenBucketwithtimestamp:
    def __init__(self , max_capacity , fill_rate):
        self.lastRequestTime=int(time.time())
        self.max_capacity=max_capacity
        self.fill_rate=fill_rate
        self._token=max_capacity
        self.lock=threading.Lock()
    def consume(self , tokenNeed):
        with self.lock:
            print('try get token')
            if tokenNeed<=self._getCurToken():
                self._token-=tokenNeed
                print(self._token)
                return True
            else:
                print(self._token)
                return False

    def consumeWithOutBigrequreStarving(self , tokenNeed):
        if tokenNeed>self.max_capacity:
            return False
        with self.lock:
            while True:
                if self._token<=self._getCurToken():
                    self._token=tokenNeed
                    return True
                else:
                    time.sleep(1)

    def putToken(self , tokenAdd):
        with self.lock:
            print('add token')
            if self._token==self.max_capacity:
                return
            else:
                self._token=min(self._token+tokenAdd , self.max_capacity)

    def _getCurToken(self):
        nowTimestamp=int(time.time())
        if self._token<self.max_capacity:
            self._token=min(self.max_capacity , self._token+self.fill_rate*(nowTimestamp-self.lastRequestTime))
        self.lastRequestTime=nowTimestamp
        return self._token






# bucket=TokenBucketwithtimestamp(10 , 2)
# time.sleep(2)
# bucket.comsume(2)
# time.sleep(2)
# bucket.comsume(3)
# time.sleep(2)
# bucket.comsume(3)
#
#


class TokenBucketwithMultiProducer:
    def __init__(self , max_capacity , fill_rates):
        self.fill_rates=fill_rates
        self._maxCapacity=max_capacity
        self._tokens=0
        self.lock=threading.Lock()
        # self.producer=threading.Thread(target=self.producer()  )
        self.producers =[]
        self.stopEvents=[]
        for fill_rate in fill_rates:
            stopEvent=threading.Event()
            worker=threading.Thread(target=self.producer , args=(fill_rate , stopEvent)  , daemon=True)
            worker.start()
            self.stopEvents.append(stopEvent)
            self.producers.append(worker)

        #self.producer.join()

    def producer(self , fillRate , stopEvent):
        while not stopEvent.is_set():
            if self._tokens < self._maxCapacity:
                with self.lock:
                    self._tokens = min(self._tokens + fillRate, self._maxCapacity)
                    print(self._tokens)
            time.sleep(1)



    def getToken(self , tokenNeed):
        self.lock.acquire()
        print('try get token')
        if self._tokens>=tokenNeed:
            self._tokens-=tokenNeed
            #print(self._tokens)
            self.lock.release()
            return True
    #print(self._tokens)
        self.lock.release()
        return False

    def stopProducer(self):
        self.signal=False

# bucket=TokenBucketwithMultiProducer(100 , [1 , 10])
# time.sleep(2)
# bucket.getToken(2)
# time.sleep(2)
# bucket.getToken(3)
# bucket.stopEvents[1].set()
# time.sleep(2)
# bucket.getToken(3)
# time.sleep(2)
# bucket.getToken(3)


class TokenBucketwithMultiProducerAndCondition:
    def __init__(self , max_capacity , fill_rates):
        self.fill_rates=fill_rates
        self._maxCapacity=max_capacity
        self._tokens=0
        self.condition=threading.Condition()
        # self.producer=threading.Thread(target=self.producer()  )
        self.producers =[]
        self.stopEvents=[]
        for fill_rate in fill_rates:
            stopEvent=threading.Event()
            worker=threading.Thread(target=self.producer , args=(fill_rate , stopEvent)  , daemon=True)
            worker.start()
            self.stopEvents.append(stopEvent)
            self.producers.append(worker)
        #self.producer.join()

    def producer(self , fillRate , stopEvent):
        while not stopEvent.is_set():
            self.condition.acquire()
            try:
                if self._tokens == self._maxCapacity:
                    self.condition.wait()
                self._tokens=min(self._tokens+fillRate , self._maxCapacity)
                print(self._tokens)
            finally:
                self.condition.release()
                time.sleep(1)



    def getToken(self , tokenNeed):
        with self.condition:
            print('try get token')
            if self._tokens>=tokenNeed:
                self._tokens-=tokenNeed
                self.condition.notify_all()
                #print(self._tokens)

                return True
            #print(self._tokens)

            return False



    def stopProducer(self):
        self.signal=False



bucket=TokenBucketwithMultiProducerAndCondition(100 , [1 , 10])
time.sleep(2)
bucket.getToken(2)
time.sleep(2)
bucket.getToken(3)
bucket.stopEvents[1].set()
time.sleep(2)
bucket.getToken(3)
time.sleep(2)
bucket.getToken(3)