# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
#
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
#
# You can assume the string has only upper and lower case letters (a-z).
#
# Example
# str=aabcccccaaa return a2b1c5a3
# str=aabbcc return aabbcc
# str=aaaa return a4

class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """

    def compress(self, originalString):
        ans=[]
        count=0
        pre=None
        for c in originalString:
            if c!=pre:
                if pre:
                    ans.append(pre)
                    ans.append(str(count))
                count=1
            else:
                count+=1
            pre=c
        ans.append(pre)
        ans.append(str(count))
        return originalString if len(originalString)<=len(ans) else ''.join(ans)



    def realCompress(self, originalString):
        # write your code here
        ans=[]
        count=0
        pre=None
        for c in originalString:
            if c!=pre:
                if pre:
                    if count<3:
                        for i in range(count):
                            ans.append(pre)
                    else:
                        ans.append(pre)
                        ans.append(str(count))
                count=1
            else:
                count+=1
            pre=c
        # print(count)
        # print(pre)
        if count<3:
            for i in range(count):
                    ans.append(pre)
        else:
            ans.append(pre)
            ans.append(str(count))
        return ''.join(ans)