class Solution:
    """
    @param k: Write your code here
    @return: the sum of first k even-length palindrome numbers
    """
    def sumKEven(self, k):
        #
        if k<1:
            return 0
        ans=0
        seed=1
        i=1
        while i <k+1:
            temp=str(i)
            ans+=int(temp+temp[::-1])
            i+=1
        return ans