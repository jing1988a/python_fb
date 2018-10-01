# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
#
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
#
# Now say a word a from A is universal if for every b in B, b is a subset of a.
#
# Return a list of all universal words in A.  You can return the words in any order.
#
#
#
# Example 1:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# Example 3:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# Example 4:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# Example 5:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
#
#
# Note:
#
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].

import collections

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        temp=collections.defaultdict(int)
        tempA=dict()
        tempB=dict()
        for a in A:
            tempA[a]=collections.Counter(a)
        for b in B:
            tempB[b] = collections.Counter(b)
        l=len(tempB)
        for a in tempA:
            for b in tempB:
                if self.isSubset(tempA[a] , tempB[b]):
                    temp[a]+=1
        ans=[]
        for t in temp:
            if temp[t]==l:
                ans.append(t)
        return ans

    def isSubset(self , a , b):
        return not (b-a)

test=Solution()
print(test.wordSubsets(["cccbb","aacbc","bbccc","baaba","acaba"], ["cb","b","cb"]))
#
# Input:
# ["amazon","apple","facebook","google","leetcode"]
# ["e","o"]
# Output:
# ["amazon","google","facebook","apple","leetcode"]
# Expected:
# ["facebook","google","leetcode"]