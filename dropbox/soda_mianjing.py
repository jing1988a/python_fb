# // Let's assume sodas are sold in packages of 1, 2, 6, 12, 24.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
# // e.g. if N = 10, you could buy 1 x 10,  6 + 2 + 2, 6 + 1 + 1 + 1 + 1, ....
# // input : N
# // output : all possible combinations, for instance N=10 { {1,1,...,1}, {6,2,2}, {6,1,1,1,1}, {6,2,1,1}, {2,1,..,1}, .... } (don't include {2,2,6} since we have {6,2,2})
# combination sum (递归的时间复杂，如何减少递归的层数, dfs时间复杂度O(n!), 还要会用DP写)
#
# 经典买soda题，用dfs，要求改进，用dp，然后分析两者复杂度。

class Buysoda:
    def solve(self, packages, need):
        # can i assume packages are unique?
        res = []
        # packages.sort()
        self.dfs(0, [], 0, packages, need, res)
        return res

    def dfs(self, curTotal, cur, idx, packages, need, res):
        if curTotal == need:
            res.append(cur[::])
            return
        if curTotal > need:
            return
        for i in range(idx, len(packages)):
            cur.append(packages[i])
            self.dfs(curTotal + packages[i], cur, i, packages, need, res)
            cur.pop()

    def solveDPCount(self, packages, need):
        #if we know all combination for every n and use only m-1 package . dp[n][m]=dp[n-package[n-packages[m]]][m-1]
        packages.sort()
        m=len(packages)
        dp=[0 for i in range(need+1)]
        dp[0]=1
        for j in range(m):
            for i in range(1 , need+1):
                if i-packages[j]>=0:
                    dp[i]+=dp[i-packages[j]]
        return dp[-1]
    def solveDP(self, packages, need):
        #if we know all combination for every n and use only m-1 package . dp[n][m]=dp[n-package[n-packages[m]]][m-1]
        packages.sort()
        m=len(packages)
        dp=[[] for i in range(need+1)]
        dp[0]=[[]]
        for j in range(m):
            for i in range(1 , need+1):
                if i-packages[j]>=0 :
                        #and len(dp[i-packages[j]])>0:
                    for candidate in  dp[i-packages[j]]:
                        # print(i)
                        # print(dp[i])
                        # print(candidate)
                        # print(packages[j])
                        dp[i].append(candidate+[packages[j]])
            # print(dp)
        return dp[-1]


test=Buysoda()
print(test.solve([1  ,3 , 6] , 7))
print(test.solveDP([1  ,3 , 6] , 7))