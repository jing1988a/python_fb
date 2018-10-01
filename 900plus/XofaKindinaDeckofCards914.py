# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
# Example 1:
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# Example 2:
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# Example 3:
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
# Example 4:
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# Example 5:
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
#
# Note:
#
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000

import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        temp=collections.Counter(deck)
        maxK=min(temp.values())
        for i in range(2  , maxK+1):
            # print([t%i==0 for t in temp.values()])
            if all([t%i==0 for t in temp.values()]):
                return True
        return False

test=Solution()
print(test.hasGroupsSizeX([0,0,0,1,1,1,2,2,2]))

