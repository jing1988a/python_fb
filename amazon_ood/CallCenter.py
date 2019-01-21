from abc import ABCMeta, abstractmethod
from enum import Enum

import collections


class Level(Enum):
    LEVEL1 = 0
    LEVEL2 = 1
    LEVEL3 = 2


class CallStatus(Enum):
    ACTIVE = 0
    ONGOING = 1
    CLOSED = 2


class Employee(metaclass=ABCMeta):
    def __init__(self, name, level, callcenter , id):
        self_id=id
        self._name = name
        self._level = level
        self._callCenter = callcenter
        self._call = None

    def handleCall(self, call):
        self._call = call
        call.assignAgent(self)

    def closeCall(self):
        self._callCenter.notifyCallComplete(self._call)
        self._call = None

    def isOnCall(self):
        return not self._call

    @abstractmethod
    def esclateCall(self):
        pass


class CallAgentLevel1(Employee):
    def __init__(self, name , id):
        super.__init__(name, Level.LEVEL1 , id)

    def esclateCall(self):
        self._call.levelNeed = Level.LEVEL2
        self._call.setStatus(CallStatus.CLOSED)
        self._callCenter.notifyCallEsclate(self._call)
        self._call = None


class CallAgentLevel2(Employee):
    def __init__(self, name , id):
        super.__init__(name, Level.LEVEL2  , id)

    def esclateCall(self):
        self._call.setLevel(Level.LEVEL2)
        self._call.setStatus(CallStatus.ACTIVE)
        self._callCenter.notifyCallEsclate(self._call)
        self._call = None


class CallAgentLevel3(Employee , id):
    def __init__(self, name):
        super.__init__(name, Level.LEVEL2 , id)

    def esclateCall(self):
        raise Exception("this is max level")


class Call:
    def __init__(self, levelNeed):
        self._level = levelNeed
        self._status = CallStatus.ACTIVE
        self._agent = None

    def setLevel(self, level):
        self._level = level

    def getLevel(self):
        return self._level

    def getStatus(self):

    def setStatus(self):

    def setAgent(self):

    def getAgent(self):


class CallCenter:
    def __init__(self, levels):
        self._levels = levels
        self._level1sCallQueue = collections.deque()
        self._level2sCallQueue = collections.deque()
        self._level3sCallQueue = collections.deque()

    def disPatchCall(self, call):
        agent = self.getAvaliableAgent(call)
        if agent:
            call.setAgent(agent)
            call.setStatus(CallStatus.ONGOING)
            agent.handleCall(call)

    def getAllAvaliableAgent(self):

    def notifyCallEsclate(self, call):

    def notifyCallComplete(self, call):
        # check if there are job in queue. and do job in queue

    def dispacthQeuedCall(self):

    def getAvaliableAgent(self, call):
        level=0
        if call.getLevel()==Level.LEVEL2:
            level=1
        if call.getLevel() == Level.LEVEL3:
            level = 2
        for i in range(level , 3):
            for agent in self._levels:
                if not agent.isOnCall():
                    return agent

        if call.getLevel() == Level.LEVEL3:
            self._level3sCallQueue.append(call)
        if call.getLevel() == Level.LEVEL2:
            self._level2sCallQueue.append(call)
        if call.getLevel() == Level.LEVEL1:
            self._level1sCallQueue.append(call)
        return None
