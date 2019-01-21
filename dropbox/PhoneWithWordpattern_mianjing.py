# 4.	phone number + dictionary：leetcode 上的电话本问题的扩展。区别在于多了一个 dictionary，提供了一个函数 isWord（String word）返回 word 是否在 dictionary 中， 要求是只返回在 dictionary 中的 word。问了复杂度，问了优化方式，需要用 trie，对这个数据结构也不是很熟悉，简单说了一下怎么用，面试官也没细问。
#
# 0-9每个数字可以map到几个字母上，就和电话上的numberpad类似，然后给你一个词典，给你一串数字，让你输出所有用词典里的词把整个数字map出来的方法。比如说给你数字234567，给你词典["ADG", "JMP", "JMQ"], 你要输出[["ADG", "JMP"], ["ADG", "JMQ"]]
#
# 给一个号码，1928337，求对应的有效单词，例如 dropbox。followup 1: 求有效词组，比如一个号码拆分后也可以是｛ ‘drop’， ‘box’ ｝；2: 如果这个function 被heavily call，怎么办？hash map。http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=207171&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D25%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
#
#
# 初始是7位号码，输出所有可能的单词，用dfs。
# 然后给一个api判断一个词是否在字典里，只输出在词典里的词，加一句代码，在结果里判断一下。
# 然后说结果可以是几个小词拼接起来的，小词最短长度是3，dfs函数中加一个变量表示当前词开始的下标。
# 然后说如果我能访问词典里所有词，能再怎么做？hashmap，key是长度为3或4或7的所有number String，value是这个number string对应的所有单词。
# 然后说这样还不行，让我另想一个数据结构，主动给hint说，我要判断一个词在不在词典里必须长度足够才行。就是用trie了，不用实现trie，给我两个方法，containpre和containstr，用dfs再做一下。. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
# 然后剩几分钟了，他说可以了，我主动说还能再改进，这样的计算还有冗余的地方，假设前面的两个字符我已经判断出了在前缀树里了，下一层递归我还要在判断一次这两个字符。改进的方法就是，不用trie的方法，而是直接拿trienode作为传参。.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
# 然后就对他提问，结束。http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=180510&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D25%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
#
#
# 问了一道17. Letter Combinations of a Phone Number with isWord() API， 输入7位数，输出List of valid String 这个没问题 BackTrack solve。然后follow up 是给一个7位数字，字典里的词最小长度是3, 输出3+4, 4+3, 7个字母组成的valid词。这个的做法，就是另外写了一个函数去判断任意的一个长度为7的词是不是符合条件。



# 然后follow up 给了一个 validPrefix API, 让优化。面试官提示在BackTrack函数里优化。没想出，BackTrack  里怎么去判断3+4 或者是 4＋3呢， 提示是大于三就可以用validPrefix， 但是还是没有写完。请教一下大家，怎么在BackTrack 里用validPrefix 来优化。



class PhoneAndWordbreak:
    # def isword(self):

    def solve(self, phone, dic):
        l=len(phone)
        if l==0:
            return []
        intCharMap = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        ans=[]
        self.dfs( [] , 0 , l ,phone , intCharMap , ans , dic)
        return ans
    def dfs(self , candidate , idx , l , phone , intCharMap , ans , dic):
        if idx==l:

            words=self.isValid(''.join(candidate) , dic)
            #print(words)
            if words:
                #print(words)
                ans.extend(words)
            return
        for c in intCharMap[int(phone[idx])]:
            candidate.append(c)
            self.dfs(candidate , idx+1 , l , phone , intCharMap  , ans , dic)
            candidate.pop()
    def isValid(self , strs , dic):
        ans=[]
        #print(strs)
        l=len(strs)
        self.dfsWord( 0 ,l ,  [] , strs , dic , ans )
        return ans
    # can  i use word multiple times? assume yes.
    def dfsWord(self , idx , l ,  candidate , strs , dic , ans):
        if idx==l:
            #print(candidate)
            ans.append(candidate[::])
            return
        for i in range(idx , l):
            if strs[idx:i+1] in dic:
                candidate.append(strs[idx:i+1])
                self.dfsWord(i+1 , l , candidate , strs , dic , ans)
                candidate.pop()

# test=PhoneAndWordbreak()
# print(test.solve('234567' , ["adg", "jmp", "jmq"]))

# 上面能不能优化一下一遍dfs 一边确定candidate??


class PhoneAndWordbreak2:
    # def isword(self):

    def solve(self, phone, dic):
        l = len(phone)
        if l == 0:
            return []
        intCharMap = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                      ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        self.dfs([], [] ,  0, l, phone, intCharMap, ans, dic)
        return ans

    def dfs(self, candidate, chars ,idx, l, phone, intCharMap, ans, dic):
        if idx == l:
            if len(chars)==0:
                ans.append(candidate[::])
            return

        for c in intCharMap[int(phone[idx])]:
            chars.append(c)
            if ''.join(chars) in dic:
                candidate.append(''.join(chars))
                self.dfs(candidate, [] , idx + 1, l, phone, intCharMap, ans, dic)
                candidate.pop()
            self.dfs(candidate, chars , idx + 1, l, phone, intCharMap, ans, dic)
            chars.pop()


test=PhoneAndWordbreak2()
print(test.solve('234567' , ["adg", "jmp", "jmq"]))
# followup: 电话长度不为7， 想了一下，用DFS秒了, 其实就是word break. 然后分析各个函数的复杂度。
# followup: 优化search函数（非complexity级别）。我在函数开始添加了一个从后向前的搜索，避免了不必要的递归。面试官说不错，还有没有什么优化办法。. From 1point 3acres bb
# followup: 面试官：考虑一下号码长度很长，但不至于stack overflow的情况，比方说["AAAAAAAAAAAAAA", "BAAAAAAAAAAAAA"]。 trie, 一开始就只用搜 A 和B 开始的, C到Z都不用搜了



# follow up 1: 字典里的词组成的也可以，同时知道字典里的词最小长度是3。那么只有两种情况，3+4或者4+3.





class PhoneAndWordbreak2fourorthree:
    # def isword(self):

    def solve(self, phone, dic):
        l = len(phone)
        if l == 0:
            return []
        intCharMap = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                      ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        self.dfs([], [] ,  0, l, phone, intCharMap, ans, dic)
        return ans

    def dfs(self, candidate, chars ,idx, l, phone, intCharMap, ans, dic):
        if idx == l:
            if len(chars)==0:
                ans.append(candidate[::])
            return

        for c in intCharMap[int(phone[idx])]:
            chars.append(c)
            if len(chars) in [3,  4 , 7] and ''.join(chars) in dic:
                candidate.append(''.join(chars))
                self.dfs(candidate, [] , idx + 1, l, phone, intCharMap, ans, dic)
                candidate.pop()
            self.dfs(candidate, chars , idx + 1, l, phone, intCharMap, ans, dic)
            chars.pop()

test=PhoneAndWordbreak2fourorthree()
print(test.solve('234567' , ["adg", "jmp", "jmq"]))
# import unittest
#
# class Mytest(unittest.TestCase):
#     def case1(self):
#         test=PhoneAndWordbreak2()
#         self.assertEqual(test.solve('234567' , ["adg", "jmp", "jmq"]) , [['adg', 'jmp'], ['adg', 'jmq']])


#
# 上面的 , 如果 字典里单词长度都固定怎么优化?
# 1. 如果电话号码长度不能整除单词长度就直接return false
# 2. 假设字典长度3 , dfs 每到3 或者3的倍数就check candidate 在不在dic 里, 不在就直接return
#



# 初始是7位号码，输出所有可能的单词，用dfs。
# 然后给一个api判断一个词是否在字典里，只输出在词典里的词，加一句代码，在结果里判断一下。
# 然后说结果可以是几个小词拼接起来的，小词最短长度是3，dfs函数中加一个变量表示当前词开始的下标。
# 然后说如果我能访问词典里所有词，能再怎么做？hashmap，key是长度为3或4或7的所有number String，value是这个number string对应的所有单词。
# 然后说这样还不行，让我另想一个数据结构，主动给hint说，我要判断一个词在不在词典里必须长度足够才行。就是用trie了，不用实现trie，给我两个方法，containpre和containstr，用dfs再做一下。. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
# 然后剩几分钟了，他说可以了，我主动说还能再改进，这样的计算还有冗余的地方，假设前面的两个字符我已经判断出了在前缀树里了，下一层递归我还要在判断一次这两个字符。改进的方法就是，不用trie的方法，而是直接拿trienode作为传参。.鐣欏


class PhoneAndWordbreakwithTrie2:
    # def isword(self):

    def solve(self, phone, dic):
        l = len(phone)
        if l == 0:
            return []
        intCharMap = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                      ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        self.dfs([], [] ,  0, l, phone, intCharMap, ans, dic)
        return ans

    def dfs(self, candidate, chars ,idx, l, phone, intCharMap, ans, dic):
        if idx == l:
            if len(chars)==0:
                ans.append(candidate[::])
            return

        for c in intCharMap[int(phone[idx])]:
            chars.append(c)
            if not self.inPrefix(chars):
                return
            if ''.join(chars) in dic:
                candidate.append(''.join(chars))
                self.dfs(candidate, [] , idx + 1, l, phone, intCharMap, ans, dic)
                candidate.pop()
            self.dfs(candidate, chars , idx + 1, l, phone, intCharMap, ans, dic)
            chars.pop()

    def inPrefix(self , chars):
        return

    def buildTrie(self):
        return