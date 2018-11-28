# K
# nearset
# Ponits.求最近K个点.排序或者优先队列都可以
# 第一题 频率最高的K个词，优先队列搞定，注意输入为0的edge case  这个和这题是一个意思吧..  就是这K 频率是 minheap
import heapq


class Problem:
    def solve(self, numOfLoc, allLoc, K):
        hq = []
        for loc in allLoc:
            # if len(loc)!=2:
            #     continue
            curDis = loc[0] * loc[0] + loc[1] * loc[1]
            # if hq and curDis > -hq[0][0]:
            #     continue
            heapq.heappush(hq, (-curDis, loc))
            if len(hq) > K:
                heapq.heappop(hq)
        ans = []
        # if there are duplicate point then need to change ans to set()
        while hq:
            temp = heapq.heappop(hq)
            ans.append(temp[1])
        return ans


test = Problem()
allLoc = [[1, 2], [3, 4], [1, -1]]
K = 2
print(test.solve(3, allLoc, K))


# think: its very easy to think of the brutefoce way , which is caculate all the distance and sort it then
# only choose the top K point. but this involve with a lot of useless aculation that we do not need.
#
# the question want top K smallest. ususally if we want the top K element this is a strong indicator that heap would help.
# a tricky part of this question is wether using min heap or max heap. originally i was think of min heap
# beacause it want top k smallest distance then i notice this is actually a max heap
# because we need track the largest distance within our K candidate and throw away the largest when a new candidate
# get pushed into this heap





