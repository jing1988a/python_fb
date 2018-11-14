# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


import collections


class LRUCacheEasyWay:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.d = collections.OrderedDict()
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if not key in self.d:
            return -1
        ans = self.d.pop(key)
        self.d[key] = ans
        return ans

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.d:
            self.d.pop(key)
            self.d[key] = value
        else:
            if len(self.d) == self.capacity:
                self.d.popitem(last=False)
            self.d[key] = value


class Node:
    def __init__(self, v=None, key=None):
        self.v = v
        self.key = key
        self.left = None
        self.right = None


class LRUCacheHardWay:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        if capacity < 1:
            raise Exception('capacity can not be smaller than 1')
        self.d = dict()
        self.preHead = Node()
        self.end = self.preHead
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if not key in self.d:
            return -1
        cur = self.d[key]
        self.moveToEnd(cur)
        return cur.v

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.d:
            cur = self.d[key]
            cur.v = value
            self.moveToEnd(cur)
        else:
            if len(self.d) == self.capacity:
                self.removeHead()
            cur = Node(value, key)
            self.d[key] = cur
            self.end.right = cur
            cur.left = self.end
            self.end = cur

    def removeHead(self):
        head = self.preHead.right
        headKey = head.key
        self.d.pop(headKey)
        if self.end == head:
            self.end = self.preHead
            self.preHead.right = None
        else:
            self.preHead.right = head.right
            head.right.left = self.prehead
        del head

    def moveToEnd(self, cur):
        if self.end == cur:
            return
        cur.left.right = cur.right
        cur.right.left = cur.left
        cur.left = self.end
        cur.right = None
        self.end.right = cur
        self.end = cur


test = LRUCacheHardWay(2)

print(test.set(2, 1))
print(test.set(1, 1))
print(test.get(2))
print(test.set(4, 1))
print(test.get(1))
print(test.get(2))
