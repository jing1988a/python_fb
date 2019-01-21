# 给了一个Iterator遍历{PhotoId, Timestamp}这样的数据(Timestamp和这个题没关系。。。)，
# 实现getTopM获取访问最多的PhotoId，假设数据都可以放在内存中
# FollowUp：1. 如果getTopM会被调用多次，同时iterator只会获取自上次调用getTopM之后的新数据如何处理。
# 2. 用了一个Heap加HashMap，FollowUp就把这个结构状态存在Class中每次getTopM的时候进行更新。
# 由于Java的PriorityQueue取TopK需要不断Poll，为了维护数据最后还需要把TopK再给add回去。
# 另外Followup每次更新Count的时候PriorityQueue没有API能够直接进行Adjust，
# 最直接的办法是remove再add但是remove是O(N)复杂度。所以自己实现了一个Heap的adjust，
# 不断把Node给bubble up就好了。感觉应该也可以用bucket sort，不过最好和面试官确定一下数据范围；
# 我并没有提这个方法，大家自行判断吧。
# LeetCode: https://discuss.leetcode.com/top ... olution-bucket-sort



# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
#




# 没有每次进real time update 的时候
# 1 用heap  Nlog(k) 先算出count for each photoID O(n) 然后保持一个K大小的minHeap 如果出现的photoId Count 比min 大就 pushpop. O(NlogK)
# 2 bucket sort  先算出count for each photoID O(n) 然后创建一个 list, idx is count (我们知道有 n个数, 所以可以开一个n大小的list 就算所有photoid 都是一样 , count 最多也就是n)
# , v is list of photoId.  然后从后往前加


# 有real time 进
# 1.heap+ dict  heap 里是node (self.photoId , self.count)  def __lt__(self, other):return self.count < other.count. dict key is photoID , value is Node.
# and another set that track of node in heap. if the incoming photoID in heap, count+1 and bubule down. else . heappushpop. update and update heapset.
# O(logK) insert , O(1) find

# 2.dict + 普通doubleLinkedList  worst case O(n) .  N 个photo 都是1 然后最头上的那个+1, 要从队头update到队尾.
# 3.dict + LFU 那样的linkedlist.   dict key=photoID , v =node
# O(1) insert  , O(k) find

     1----4----5
     |    |    |
     n1   n3   n4
     |
     n2
     |
     n5
# 4. above is hard to impliment make it easier like bubbule sort dict key=photoID v=count. list index is count, v is a set of photoID
#O(1) insert , O(n) find
 0 , 1 , 2 , 3 , 4, 5
     n1      n2
     n3      n4


import heapq


class Solution(object):
    def topKFrequentWithHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        sort take nlogn

        or hashtable take n
        """
        ansMap = {}
        for i in nums:
            if i in ansMap:
                ansMap[i] += 1
            else:
                ansMap[i] = 1

        ans = []

        freq = []
        # print(ansMap)
        for v, f in ansMap.items():
            if len(freq) < k:
                heapq.heappush(freq, (f, v))
            else:
                if freq[0][0] < f:
                    heapq.heappushpop(freq, (f, v))
        # print(freq)

        ans = []

        for i in range(k):
            f, v = heapq.heappop(freq)
            ans.append(v)

        return ans

    def topKFrequentWithBucketSort(self, nums, k):
        ansMap = {}
        for i in nums:
            if i in ansMap:
                ansMap[i] += 1
            else:
                ansMap[i] = 1

        ans = []
        freqMap = {}
        for i in ansMap:
            if ansMap[i] in freqMap:
                freqMap[ansMap[i]].append(i)
            else:
                freqMap[ansMap[i]] = [i]

        for i in range(len(nums), 0, -1):
            if i in freqMap:
                ans += freqMap[i]
                if len(ans) >= k:
                    break

        return ans[:k]

class Node:
    def __init__(self , photoId):
        self.photoId=photoId
        self.count=1

class topKFrequentWithRealTimeUpdate_doubleLinkedList:
    def __init__(self, nums, k):
        self.photoIdMap=dict()
        for n in nums:
            if

    def getTopM(self):

    def view(self , photo_id , timestamp):

