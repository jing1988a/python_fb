# 给你一个list word 你把所有isomorphic group的word分到一起
# isomorphic string的意思是string a 到string b 里面有每一个char都是one to one relationship
# 比如 aba 和cmc是isomorphic 但是aba 和ccc 就不是
# eg: {abba, cppc, abc, emf, bbbb, m} => {{abba, cppc}, {abc, emf}, {bbbb}, {m}}
import collections
class Problem:
    def solve(self , words):
        # assume no duplicate in words? not case censitive??

        d=collections.defaultdict(list)
        for w in set(words):
            d[self.getPattern(w)].append(w)
        return d.values()
    def getPattern(self , w):
        words=list('qwertyuiopasdfghjklzxcvbnm')

        ctoP=dict()
        pattern=[]
        for c in w:
            if c not in ctoP:
               p=words.pop()
               ctoP[c]=p
            pattern.append(ctoP[c])
        return ''.join(pattern)

test=Problem()
print(test.solve(['abba', 'cppc', 'abc', 'emf', 'bbbb', 'm']))
