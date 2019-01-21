class Node:
    def __init__(self , query  , result):
        self._value=result
        self._key=query
    def getKey(self):

    def getValue(self):

    def setValue(self):

class DoubleLinkedList:
    def __init__(self):
        self._head=None
        self._tail=None

    def deleteNode(self , node):

    def moveToHead(self , node):

    def deleteTail(self):

    def appendToHead(self , node):

    def getTail(self):

class LRU:

    def __init__(self , maxSize):
        self._linkedList=DoubleLinkedList()
        self._dict=dict()
        self._maxSize=maxSize

    def get(self, query):
        node=self._dict.get(query , None)
        if not node:
            return None
        self._linkedList.moveToHead(node)
        return node.getValue()

    def set(self , results , query):
        node=self._dict.get(query)
        if not node:
            if len(self._dict)==self._maxSize:
                tail=self._linkedList.getTail()
                tailKey=tail.getKey()
                self._dict.pop(tailKey)
                self._linkedList.deleteTail()
            newNode=Node(query , results)
            self._dict[query]=newNode
            self._linkedList.appendToHead(newNode)
        else:
            node.setValue(results)
            self._linkedList.moveToHead(node)
