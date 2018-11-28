# 给你一个String （I am Jack and my father is Jimmy. I like wearing Jack and Jone's. ）， 一个exclude list， 让你给出出现频率最高或者并列高的词(不Case sensitive, Jack和jack算一个词，都出现的话等于算jack出现两次). (而不是大家之前说的给一个k，然后求出出现频率最高的k个）, 比如Jack和Jone都是频率最高且出现三次，那么return [Jack, Jone]。
# 24/25 case


# 给你一个字符串， 一个排除的清单， 让你给出出现频率最高或者并列高的词，这里要注意大小写。很多人的是不区分，但是我这里是要区分的，大家做的时候多注意。
import collections


class Problem:
    def solve(self, text, d):
        exclude = set(d)

        words = text.split(' ')
        ans = []
        counter = collections.defaultdict(int)
        curMax = 0
        for w in words:
            temp = w.lower()
            if not temp in exclude:
                counter[temp] += 1
                if curMax < counter[temp]:
                    curMax = counter[temp]
                    ans=[temp]
                elif curMax==counter[temp]:
                    ans.append(temp)

        return ans


text = "jack jack and jill went to the arket to buy bread and cheese cheese is jack favorite food"
d = ['and', 'he', 'the', 'to', 'is']

test = Problem()
print(test.solve(text, d))
