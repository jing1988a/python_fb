# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
import random
class Codec:
    def __init__(self):
        self.shortToLong=dict()
        self.longToShort=dict()
        self.s = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.longToShort:
            return self.longToShort[longUrl]
        else:
            shortUrl=self.generateURL(longUrl)
            self.shortToLong[shortUrl]=longUrl
            self.longToShort[longUrl]=shortUrl
            return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if shortUrl not in self.shortToLong:
            return -1
        return self.shortToLong[shortUrl]
    def generateURL(self , longURL ):
        temp=[]
        for i in range(6):
            temp.append(random.choice(self.s))
        candidate=''.join(temp)
        if candidate in self.shortToLong:
            candidate=self.generateURL(longURL)
        return candidate



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))