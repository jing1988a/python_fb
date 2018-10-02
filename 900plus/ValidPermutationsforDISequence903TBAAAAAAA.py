# We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)
#
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:
#
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: "DID"
# Output: 5
# Explanation:
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
#
# Note:
#
# 1 <= S.length <= 200
# S consists only of characters from the set {'D', 'I'}.


#
# Approach 1: Dynamic Programming
# Intuition
#
# When writing the permutation P = P_0, P_1, ..., P_N from left to right, we only care about the relative rank of the last element placed. For example, if N = 5 (so that we have elements {0, 1, 2, 3, 4, 5}), and our permutation starts 2, 3, 4, then it is similar to a situation where we have placed ?, ?, 2 and the remaining elements are {0, 1, 3}, in terms of how many possibilities there are to place the remaining elements in a valid way.
#
# To this end, let dp(i, j) be the number of ways to place every number up to and inlcuding P_i, such that P_i when placed had relative rank j. (Namely, there are j remaining numbers less than P_i.)
#
# Algorithm
#
# When placing P_i following a decreasing instruction S[i-1] == 'D', we want P_{i-1} to have a higher value. When placing P_i following an increasing instruction, we want P_{i-1} to have a lower value. It is relatively easy to deduce the recursion from this fact.

class Solution:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
