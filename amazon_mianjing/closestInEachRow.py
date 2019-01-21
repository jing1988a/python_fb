# 上午3.两个小哥印度+亚裔，先BQ，然后写代码，搞了好久才弄明白题目意思，浪费好长时间，题目就是给个list of list, 输出每个list中的某个数，这个数与下一行的list中的某个数差值最小，最后一行与它上一行比较。输出的结果是个list。简单说，在list row1里找一个数和list row2里的某个数最接近，输出个数就行了。最简单的方法谁都会写，但是没时间优化了。




#
# 上午1.南美小哥，写代码，各种硬币1分，5分，25分，1角，1块。给一个钱数，找各种组合种类，其实就是一个简单的DFS，一时晕了，写了好久才写完OK。然后让换一种做法。没写完。。。
# 上午2.manager+bar raiser。纯BQ吹逼。
# 上午3.两个小哥印度+亚裔，先BQ，然后写代码，搞了好久才弄明白题目意思，浪费好长时间，题目就是给个list of list, 输出每个list中的某个数，这个数与下一行的list中的某个数差值最小，最后一行与它上一行比较。输出的结果是个list。简单说，在list row1里找一个数和list row2里的某个数最接近，输出个数就行了。最简单的方法谁都会写，但是没时间优化了。
# 中午吃饭，很开心，中国小哥。
# 下午1.印度小哥，简单BQ，然后系统设计，在线卡牌游戏，主要谈怎么scale，如何与db交互。
# 下午2.两个小哥印度+中国，先BQ，然后OOD，设计一个能够自定义功能的Cache。这里呵呵了。



import sys
class MinDiff:
    def solve(self , lists):
        for row in lists:
            row.sort()
        l=len(lists)
        if l==0:
            return []
        ans=[]
        for i in range(l-1):
            ans.append(self.getMinV(lists[i] , lists[i+1]))
        ans.append(self.getMinV(lists[l-1] , lists[0]))
        return ans

    def getMinV(self , list1 , list2):
        l=len(list1)
        i=j=0
        candidate=None
        minDiff=sys.maxsize
        while i<l and j<l:
            curDiff=abs(list1[i]-list2[j])
            if curDiff<minDiff:
                minDiff=curDiff
                candidate=list1[i]
            if list1[i]<list2[j]:
                i+=1
            else:
                j+=1
        return candidate


test=MinDiff()
nums=[ [ 2 , 3 , 4]  , [4 , 5 , 6 ]  ,[ 2, 5 , 9] ]
print(test.solve(nums))


