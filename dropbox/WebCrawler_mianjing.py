class WebCrawler:
    def __init__(self, startUrl):
        self.startUrl = startUrl
        self.visited = set()
        self.domain = self.getDomain()

    def getURL(self):
        #self.dfs(self.startUrl)
        self.bfs(self.startUrl)
        return self.visited

    def dfs(self, url):
        links = self.getLinks(url)
        for link in links:
            if self.inDomain(link) and not link in self.visited:
                self.visited.add(link)
                self.dfs(link)
    def bfs(self , url):
        q=[url]
        while q:
            p=[]
            for url in q:
                links=self.getLinks(url)
                for link in links:
                    if self.inDOmain(links) and not links in self.visited:
                        self.visited.add(link)
                        p.append(link)
            q=p

    def getDomain(self):

    def getLinks(self):

    def inDOmain(self, url):


import queue
import threading


class WebCrawlerMultiWithQueue:
    def __init__(self, startUrl):
        self.startUrl = startUrl
        self.visited = set()
        self.domain = self.getDomain()
        self.queue = queue.Queue()
        self.queue.put(startUrl)
        self.threads = []

    def getURL(self):
        for i in range(50):
            myWorker = threading.Thread(target=self.worker )
            myWorker.start()
            self.threads.append(myWorker)
        # block until all tasks are done
        self.queue.join()
        for i in range(50):
            self.queue.put(None)
        # stop workers
        for t in self.threads:
            t.join()

    def worker(self):
        while True:
            if not self.queue.empty():
                url = self.queue.get()
                if url is None:
                    break

                links = self.getLinks(url)

                self.visited.add(url)
                for link in links:
                    if self.inDomain(link) and not link in self.visited:
                        self.queue.put(link)
                self.queue.task_done()

class WebCrawlerMultiWithQueueAndEvent:
    def __init__(self, startUrl):
        self.startUrl = startUrl
        self.visited = set()
        self.domain = self.getDomain()
        self.queue = queue.Queue()
        self.queue.put(startUrl)
        self.threads = []
        self.stopEvent=threading.Event()
        self.lock=threading.Lock()

    def getURL(self):
        for i in range(50):
            myWorker = threading.Thread(target=self.worker )
            myWorker.start()
            self.threads.append(myWorker)
        # block until all tasks are done
        self.queue.join()
        self.stopEvent.set()

    def worker(self):
        #Queue is designed for multi thread so with the call .get() , .put() .task_done() are all thread safe
        while not self.stopEvent.is_set():
            if not self.queue.empty():
                url = self.queue.get()
                links = self.getLinks(url)
                self.visited.add(url)
                for link in links:
                    if self.inDomain(link) and not link in self.visited:
                        self.queue.put(link)
                self.queue.task_done()


#what if queue is empty?
class WebCrawlerMultiWithQueueAndEventAndCondition:
    def __init__(self, startUrl):
        self.startUrl = startUrl
        self.visited = set()
        self.domain = self.getDomain()
        self.queue = queue.Queue()
        self.queue.put(startUrl)
        self.threads = []
        self.stopEvent = threading.Event()
        self.condition = threading.Condition()

    def getURL(self):
        for i in range(50):
            myWorker = threading.Thread(target=self.worker)
            myWorker.start()
            self.threads.append(myWorker)
        # block until all tasks are done
        self.queue.join()
        self.stopEvent.set()

    def worker(self):
        # Queue is designed for multi thread so with the call .get() , .put() .task_done() are all thread safe
        while not self.stopEvent.is_set():
            self.condition.acquire()
            try:
                if self.queue.empty():
                    self.condition.wait()
                url = self.queue.get()
                links = self.getLinks(url)
                self.visited.add(url)
                gotMoreLink=False
                for link in links:
                    gotMoreLink=True
                    if self.inDomain(link) and not link in self.visited:
                        self.queue.put(link , block=True)
                if gotMoreLink:
                    self.condition.notifyAll()
                self.queue.task_done()
            finally:
                self.condition.release()
# 1 worker 什么时候停止


class WebCrawlerMultiWithCondition:
    def __init__(self, startUrl):
        self.startUrl = startUrl
        self.visited = set()
        self.domain = self.getDomain()
        self.lock = threading.Lock()

    def getURL(self):
        q = []
        q.append(self.startUrl)
        while q:
            p = []
            for url in q:
                myWorker = threading.Thread(target=self.worker, agrs=(url, p))
                myWorker.start()
                myWorker.join()
            q = p
        return self.visited

    def worker(self, url, p):

        links = self.getLinks(url)  # 这个不能写在lock 里 不然 就和单线程没区别了, 就是这一步废时间, 要同时执行这一步
        with self.lock:
            self.visited.add(url)
            for link in links:
                if self.inDomain(link) and not link in self.visited:
                    p.append(link)

    def getDomain(self):

        def getLinks(self):

        def inDOmain(self, url):


