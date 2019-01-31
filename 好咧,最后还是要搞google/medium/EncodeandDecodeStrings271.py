# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
#
#
# Note:
#
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<1:
            return None
        return '/'.join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s is None:
            return []
        if len(s)==0:
            return [""]
        return s.split('/')


#上面这个搞法如果你string里可以包含任何字符, 你的 separate会和string里的value冲突所以是不行的..


#加个 header, 每个字符串长度 放在header 然后再用 | 把heder 和 content隔开
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return None
        header=[]
        for s in strs:
            header.append(str(len(s)))
        header='-'.join(header)
        content=''.join(strs)
        return header+'|'+content


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s is None:
            return []
        header , content=s.split( '|' , 1)
        header=map(int , header.split('-'))
        ans=[]
        cur=0
        for size in header:
            ans.append(content[cur:cur+size])
            cur=cur+size
        return ans
test=Codec()
print(test.encode([""]))
print(test.decode(test.encode([""])))
