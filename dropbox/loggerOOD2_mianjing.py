# https://thispointer.com/designing-a-configurable-logging-framework-using-observer-design-pattern/
#
# A configurable option for other application modules to save logs at more than one platform like, on Console, in txt files or on network etc.
# A Facility to Log messages in different categories like, ERROR, WARNING, GENERAL_MESSAGES and also provision to control each category independently.
# A Facility to configure & bind category and Logging platform at run time i.e. user will be able to specify at runtime that,
# Messages of any particular category should be logged or not etc.
# Messages of any particular category like ERROR should be logged in error.txt and remaining categories on console only etc.



import enum


class LogType(enum.Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2


class Observer:  # logging platform
    def update(self, subject):
        raise Exception('implement this first')


import collections
import time


class Subject:
    def __init__(self):
        self.registryMap = collections.defaultdict(set)
        self.data = None

    def getData(self):
        return self.data

    def setData(self, value, event):
        self.data = str(event) + ': ' + value + " at " + time.strftime("%b %d %Y %H:%M:%S")

    def register(self, event, logPlatform):
        self.registryMap[event].add(logPlatform)

    def deregister(self, logPlatform):
        for event in self.registryMap:
            if logPlatform in self.registryMap[event]:
                self.registryMap[event].remove(logPlatform)

    def notify(self, event):
        for logPlatform in self.registryMap[event]:
            logPlatform.update(self)


class Logger(Subject):
    def __init__(self):
        super().__init__()
        self.messageStatusMap = dict()
        self.messageStatusMap[LogType.ERROR] = True
        self.messageStatusMap[LogType.WARNING] = True
        self.messageStatusMap[LogType.INFO] = True

    def writeLog(self, event, message):
        if self.messageStatusMap[event]:
            self.setData(message, event)
            self.notify(event)

    def enableLoggingforEvent(self, event):
        self.messageStatusMap[event] = True

    def disableLoggingforEvent(self, event):
        self.messageStatusMap[event] = False


class ConsolePlatform(Observer):
    def update(self, subject):
        print("written in console: " + subject.getData())


class FilePlatform(Observer):
    def update(self, subject):
        data = subject.getData()
        with open('Filelog.txt', 'a') as fh:
            fh.write(data)

        print("written in file: " + subject.getData())


class NetworkPlatform(Observer):
    def update(self, subject):
        print("Sent on network: " + subject.getData())


logger = Logger()
consolePlatform = ConsolePlatform()
filePlatform = FilePlatform()
networkPlatform = NetworkPlatform()

logger.register(LogType.ERROR, consolePlatform)
logger.register(LogType.WARNING, consolePlatform)
# logger.register(INFO , consoleLogPlatform)
logger.register(LogType.ERROR, filePlatform)
logger.register(LogType.ERROR, networkPlatform)
logger.register(LogType.WARNING, networkPlatform)
logger.register(LogType.INFO, networkPlatform)
logger.writeLog(LogType.ERROR, 'this is an error message')  # logger.notify(event , message)
logger.writeLog(LogType.INFO, 'this is an info message')
logger.writeLog(LogType.WARNING, 'this is an warning message')
logger.disableLoggingforEvent(LogType.ERROR);
# logger.writeLog(LogType.ERROR , 'this is an error message' )
# logger.writeLog(LogType.INFO , 'this is an info message' )
# logger.writeLog(LogType.WARNING , 'this is an warning message' )
logger.deregister(networkPlatform)
# logger.writeLog(LogType.ERROR , 'this is an error message' )
# logger.writeLog(LogType.INFO , 'this is an info message' )
# logger.writeLog(LogType.WARNING , 'this is an warning message' )
