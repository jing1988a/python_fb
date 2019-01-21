# 上午1.南美小哥，写代码，各种硬币1分，5分，25分，1角，1块。给一个钱数，找各种组合种类，其实就是一个简单的DFS，一时晕了，写了好久才写完OK。然后让换一种做法。没写完。。。


class FindChanges:
    def solve(self , nums , target):
        res=set()
        self.recurBuild(nums , target , [] , res)
        return res
    def recurBuild(self , nums , target , candidate  , res):
        if target==0:
            res.add(tuple(candidate[::]))
            return
        if target<0:
            return
        for n in nums:
            candidate.append(n)
            self.recurBuild(nums , target-n , candidate , res)
            candidate.pop()


test=FindChanges()
print(test.solve([1 , 5  , 10 , 25 , 1 ] , 13))

