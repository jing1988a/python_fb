# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# Example:
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Accepted
# 45,171
# Submissions
# 94,759

import collections

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups=collections.defaultdict(list)
        for string in strings:
            if len(string)==0:
                continue
            if len(string)==1:
                groups['0'].append(string)
            else:
                format=self.getFormat(string)
                groups[format].append(string)
        return groups.values()
    def getFormat(self , string):
        myformat=''
        pre=ord(string[0])
        for i in range(1 , len(string)):
            cur=ord(string[i])
            myformat+='|'+str((cur-pre+26)%26)
            pre=cur
        return myformat