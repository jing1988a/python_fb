class Solution:
    """
    @param timeSeries: the Teemo's attacking ascending time series towards Ashe
    @param duration: the poisoning time duration per Teemo's attacking
    @return: the total time that Ashe is in poisoned condition
    """
    def findPoisonedDuration(self, timeSeries, duration):
        # Write your code here
        # assume timeSeries is sorted????
        l=len(timeSeries)
        if l==0:
            return 0

        curStart=timeSeries[0]
        curEnd=curStart+duration
        ans=0
        i=1
        while i<l:
            if timeSeries[i]<curEnd:
                ans+=timeSeries[i]-curStart
            else:
                ans+=curEnd-curStart
            curStart=timeSeries[i]
            curEnd=curStart+duration
            i+=1
        ans+=duration
        return ans