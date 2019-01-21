from  abc import ABCMeta , abstractmethod

from enum import Enum

class Status(Enum):
    UNREAD=0
    READ=1
    ACCEPT=2
    RECJECT=3

class Server:
    __instance=None
    def _getInstance(self):
        if self.__instance==None:
            Server()
        return Server._instance
    def __init__(self):
        if Server.__instance:
            raise Exception('server has already been created')
        self._users=set()
        Server.__instance=self

    def addUser(self , user):
    def removeUser(self , user):

class Message:
    def __init__(self , id , text , sender  , timestamp ):
        self._id = id
        self._text=text
        ...
        ...
        ...
class Request:

class User:
    def __init__(self , id , name ):
        self._id=id
        self._name=name
        self._server=None
        self._friends=dict()
        self._receivedFrindRequests=[]
        self._sendFriendRequest=[]
        self._privatChats=dict() #key:chatId value: chat Object
        self._GroupChats=dict()

    def sendFrindRequest(self , receiver):

    def rejectFriendRequest(self , request):

    def approveFriendRequest(self , request):

    def viewFriendRequest(self):

    def viewAllChat(self):

    def addFriendtoPrivateChat(self , friend):

    def addFriendtoGroupChat(self , friend):

    def addFriendtoGroupChat(self, friend , groupId):

    def sendMessagetoGroup(self , groupId):

    def viewMassagefromGroup(self groupId):


class Chat(metaclass=ABCMeta):
    def __init__(self , id ):
        self._id=id
        self._users=set()
        self._messages=[]

    def postMessage(self, message):

class GroupChat(Chat):

class PrivateChat(Chat ):
    def __init__(self , user1 , user2):
        super.__init__()
        self._users.append(user1)
        self._users.append(user2)

class GroupChat(Chat):


    def addUser(self , user):
        self._users.add(user)
    def removeUser(self , user):
        self._users.remove(user)






