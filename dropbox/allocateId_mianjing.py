# allocate and release id in the range of [0, N], allocate和relase都要是o(1)
# follow up 1: id分配完了怎么办，多次release 同一个id怎么办。
# follow up 2: 如何减小内存花销，allocate的复杂度可以是o(n) -->使用bitmap
# follow up 3: 如何在内存和效率上实现一个折衷，使用比bitmap多一些的内存，但是搜索接近o(1).
# 最后一个问题在提示下回答了，想法就是把bitmap分成不同部分，对每一个部分记录是否有id被分配过。

# 1.用一个 queue  O(1)

class AllocateId:
    def __init__(self, maxId):
        self.pool = self.buildPool(maxId)

    def allocate(self):
        if not self.pool:
            return None
        else:
            return self.pool.pop()

    def release(self, id):
        self.pool.append(id)

    def buildPool(self, maxId):
        for i in range(1, maxId + 1):
            self.pool.append(i)


# in above case, int use 24 byte which is 96 bit
# we can do a bit array. to sacrifise speed for space
import bitarray


class AllocateIdBitArray:
    def __init__(self, maxId):
        self.pool = bitarray.bitarray(maxId)
        self.maxId = maxId

    def allocate(self):
        for i in range(self.maxId):
            if self.pool[i]:
                self.pool[i] = 0
                print(self.pool)
                return i
        return None

    def release(self, id):
        self.pool[id] = 1


test = AllocateIdBitArray(11)
print(test.allocate())
print(test.allocate())
print(test.allocate())

import bitarray


class AllocateIdBitArrayWithTree:
    def __init__(self, maxId):
        self.pool = bitarray.bitarray(maxId * 2 + 1)
        self.maxId = maxId

    def allocate(self):
        curLoc = 1
        while curLoc < self.maxId:
            if self.pool[curLoc * 2] == 1:
                curLoc *= 2
            else:
                if self.pool[curLoc * 2 + 1] == 0:
                    return None
                curLoc = curLoc * 2 + 1
        self.pool[curLoc] = 0
        self.updatePool(curLoc // 2)
        return curLoc

    def release(self, id):
        self.pool[self.maxId + id] = 1
        self.updatePool((self.maxId + id) // 2)

    def updatePool(self, idx):
        cur = idx // 2
        if self.pool[cur * 2] == 0 and self.pool[cur * 2 + 1] == 0:
            self.pool[cur] = 0
            if cur != 1:
                self.updatePool(cur // 2)
