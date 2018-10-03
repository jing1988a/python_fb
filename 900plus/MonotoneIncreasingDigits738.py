# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
#
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].
#
# 1232    1222  1199

#
# class Solution(object):
#     def monotoneIncreasingDigits(self, N):
#         digits = []
#         A = map(int, str(N))
#         for i in xrange(len(A)):
#             for d in xrange(1, 10):
#                 if digits + [d] * (len(A)-i) > A:
#                     digits.append(d-1)
#                     break
#             else:
#                 digits.append(9)
#
#         return int("".join(map(str, digits)))

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = []
        A = list(map(int, str(N)))
        # print(list(A))
        l=len(A)
        for i in range(l):
            for j in range(1 , 10):
                if digits+[j]*(l-i)>A: # why not l-1-i
                    digits.append(j-1)
                    break
            else:
                digits.append(9)
        return int("".join(map(str ,digits)))

test=Solution()
print(test.monotoneIncreasingDigits(11))

# Submission Result: Wrong Answer
# Input:
# 10
# Output:
# 19
# Expected:
# 9