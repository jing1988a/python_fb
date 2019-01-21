# 第四轮： Bar raiser， 还是20分钟BQ, 不同于前三轮的都听你说。这个小哥只有我说一句新东西，他都要 dive deep 的扣。几乎一直的被打断。还好好像对我的回答还算满意。
# 问的算法题是： 设计 AI Search 的 API. 大体意思是。给你一个 guess() api, 返回 secret 和你猜的string有多少match. 返回的是一个数组，数组表示的是第几个index是 match的。比如 secret = "apple" , guess("adobe"). 就会返回{1,5}
# 要求设计一个新 api 返回下面最有可能要猜的string. 这题我基本上是崩了。最后几分钟说了大体思路，写了基本逻辑代码。
#
# 回家准备GG面试的时候发现很像 谷歌高频 蠡口 巴斯三  但也不一样，要求设计的api不同，但背景很像（日哦）

import random

class Game:

    def __init__(self , wordlist):
        self.wordlist=wordlist
    def guess(self , word):
        return []

    def mostLikelyGuess(self ):
        res=self.myChoice()
        match=self.guess()
        self.stripWordlist(match  , res)
        return res

    def myChoice(self):
        return random.choice(self.wordlist)

    def stripWordlist(self , match , candidate):
        res=[]
        for w in self.wordlist:
            if all(w[x]==candidate[x] for x in match):
                res.append(w)
        self.wordlist=res
