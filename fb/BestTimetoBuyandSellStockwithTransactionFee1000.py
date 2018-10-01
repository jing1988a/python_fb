class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        # write your code here
        l=len(prices)
        if l==0:
            return 0
        candiBuy=prices[0]
        candiSell=None
        ans=0
        for i in range(1 , l):
            if candiSell is None:
                if prices[i]>candiBuy+fee:
                    candiSell=prices[i]
                elif prices[i]<candiBuy:
                    candiBuy=prices[i]
            else:
                if prices[i]<candiSell-fee:
                    ans+=candiSell-fee-candiBuy
                    candiBuy=prices[i]
                    candiSell=None
                elif prices[i]>candiSell:
                    candiSell=prices[i]
        if candiSell!=None:
            ans+=candiSell-fee-candiBuy
        return ans