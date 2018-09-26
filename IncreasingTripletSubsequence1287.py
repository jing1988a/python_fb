class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def increasingTriplet(self, nums):
        # write your code
        a=b=None
        for n in nums:
            if a is None:
                a=n
            else:
                if n>a:
                    if not b:
                        b=n
                    elif n<b:
                        b=n
                    elif n>b:
                        return True
                if n<a:
                    a=n
        return False

test=Solution()
test.increasingTriplet([1, 2, 3, 4, 5])