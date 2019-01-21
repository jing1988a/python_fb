# - 用Heap来实现Stack，Stack的功能包括Push(int num), Pop(), getMax(), getAverage()，我并没有想出来，小哥提示之后做出来了。
# 思路大概是定义一个新的class，比如Node类，里面包含attribute包括order和maxVal。所以Heap里装的是这个Node，Heap里的nodes是用order来作为comparator。. check 1point3acres for more.
# 因此每次要push一个数字的话，要新建一个Node，然后根据Heap顶元素来确定当前数字的order，并求出当前的maxVal，全部存到Node里面然后push进Heap。
# class Node {
#       int order;
#       int maxVal;
# }



import heapq


class MyStack:
    def __init__(self):
        self.hq = []
        self.total = 0

    def push(self, v):
        curMax = None
        if not self.hq:
            order = 0
            curMax = v
        else:
            preOrder, preV, preMax = self.hq[0]
            curMax = max(preMax, v)
            order = preOrder - 1
        heapq.heappush(self.hq, (order, v, curMax))
        self.total += v

    def pop(self):
        if not self.hq:
            return None
        else:
            order, v = heapq.heappop(self.hq)
            self.total -= v
            return v

    def getAVG(self):
        return self.total / len(self.hq)

    def getMax(self):
        if not self.hq:
            return
        return self.hq[0][2]