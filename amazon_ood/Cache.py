class Item:
    def __init__(self , key , value):

    def getValue(self):

    def setValue(self):

    def getKey(self):
class HashMap:
    def __init__(self , size):
        self._size=size
        self._dict=[[] for i in range(size)]
    def set(self , key , value):
        hasedIdx=self._getHashedIdx(key)
        for items in self._dict[hasedIdx]:
            if items.getKey()==key:
                items.setValue()=value
                return True
        self._dict[hasedIdx].append(Item(key , value))

    def get(self , key):


    def remove(self ,  key):


    def _getHashedIdx(self  , key):
        return key%self._size
