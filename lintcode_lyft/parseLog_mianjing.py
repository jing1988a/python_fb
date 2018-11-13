# 刚面完，妥妥的挂了。。。。白人小哥
# 一道题: 直接上来给了一串string log，说 parse the log，然后小哥就静音干自己的事去了。。。
# 每一行［e.g］[02/01/2014 5:7:8 + 0000] PUT /user/4324/riders/543534 HTTP1.1 304 chrome ...
# 要求输出:
# (1) 统计每一个request出现的次数 （request type + request url mapping + status code 组合）
# (2) unique user
# 写完之后，说不对。。。user个数不对
# 仔细看log, 只有跟在user后面的才算并且不是每个log都有user information。
# 改完后说，输出request统计输出不对，应该把data全部用'#'表示。
# 改完后说，还是不对，要求request的输出按照count个数排序。
# 。。。。然，并没有时间改了。。。。。
# 攒个经验，下次写题目之前要把要求问清楚了。
# 回去继续好好联系基本功
import collections


class Problem:
    def parseLog(self, logs):
        requestCount = collections.defaultdict(list)
        userSet = set()
        for log in logs:
            temp = log.split(' ')
            if temp[0] + temp[1] + temp[3] in requestCount:
                requestCount[temp[0] + temp[1] + temp[3]] = [requestCount[temp[0] + temp[1] + temp[3]][0] + 1,
                                                             temp[0] + temp[1] + temp[3]]
            else:
                requestCount[temp[0] + temp[1] + temp[3]] = [1, temp[0] + temp[1] + temp[3]]
            if 'user' in temp[1]:
                userInfo = temp.split('/')
                userSet.add(userInfo[1])

        requestCount.sort(key=lambda x: x[0])
        userCount = len(userSet)
