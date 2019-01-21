#
# 给你一个list输入 <name, building from, building to> 现在想要找到所有pair他们可以swap building .     比如 <a, 1, 2> <b, 2, 1>, <c, 1, 3> -> 输出<a,b > 因为他们能互换
# <a, 1, 2>
# <b, 2 ,1>
# <c, 1, 3>
# <d, 3, 1>
# <e, 1, 2>
# [名字][所在building][想去的building]
# 现在building满了 要找人换 找到所有可能的互换
# 这题就是<a,b>互换 <c,d>互换 e没人跟他换
import collections


class Problem:
    def solve(self, inputs):
        d = collections.defaultdict(list)
        ans = []
        for b, s, t in inputs:
            need = str(t) + '|' + str(s)
            if need in d:
                a = d[need].pop()
                if not d[need]:
                    del d[need]
                ans.append([a, b])
            else:
                d[str(s) + '|' + str(t)].append(b)
        return ans


test = Problem()
print(test.solve([['a', 1, 2], ['b', 2, 1], ['c', 1, 3], ['d', 3, 1], ['e', 1, 2]]))

# <a, 1, 2>
# <b, 2 ,1>
# <c, 1, 3>
# <d, 3, 1>
# <e, 1, 2>
