class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        l=len(prices)
        if l<2:
            return 0
        lProfit=self.getLmax(prices , l)
        rProfit=self.getRmax(prices , l)
        ans=0
        for i in range(l):
            ans=max(ans , lProfit[i]+rProfit[i])
        return ans

    def getLmax(self , prices , l):
        buy=prices[0]
        ans=[0 for i in range(l)]
        cur=0
        for i in range(1 , l):
            if prices[i]-buy>cur:
                cur=prices[i]-buy
            if prices[i]<buy:
                buy=prices[i]
            ans[i]=cur
        return ans
    def getRmax(self , prices , l):
        sell=prices[l-1]
        ans=[0 for i in range(l)]
        cur=0
        for i in range(l-2 , -1 , -1):
            if sell-prices[i]>cur:
                cur=sell-prices[i]
            if prices[i]>sell:
                sell=prices[i]
            ans[i]=cur
        return ans
test=Solution()
print(test.maxProfit([2,1,2,0,1]))