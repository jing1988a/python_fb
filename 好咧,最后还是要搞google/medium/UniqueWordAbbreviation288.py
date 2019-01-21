# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
#      1
#      ↓
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
#
# Example:
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

import collections
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbrDict=collections.defaultdict(set)
        for word in dictionary:
            self.abbrDict[self.getAbbr(word)].add(word)
        #print(self.abbrDict)
    def getAbbr(self , word):
        l=len(word)
        if l<3:
            return word
        #print(word)
        return word[0]+str(l-2)+word[-1]


    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr=self.getAbbr(word)
        if abbr in self.abbrDict:
            if len(self.abbrDict[abbr])==1:
                candidate=self.abbrDict[abbr].pop()
                if candidate==word:
                    self.abbrDict[abbr].add(candidate)
                    return True
                else:
                    self.abbrDict[abbr].add(candidate)
                    return False
            else:
                return False
        else:
            return True



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)