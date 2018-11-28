# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
#
#
# Example 1:
#
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#
#
# Note:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.

import functools


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        def myCmp(A, B):

            def containsNoLetter(strs):
                return all(x.isdigit() for x in strs.split(' '))

            idA, dataA = A.split(' ', 1)
            idB, dataB = B.split(' ', 1)

            typeA = containsNoLetter(dataA)
            typeB = containsNoLetter(dataB)
            if typeA is True and typeB is True:
                return 0
            if typeA is True and typeB is False:
                return 1
            if typeA is False and typeB is True:
                return -1

            if dataA > dataB:
                return 1
            elif dataA < dataB:
                return -1
            else:
                if idA > idB:
                    return 1
                else:
                    return -1

        logs.sort(key=functools.cmp_to_key(myCmp))
        return logs