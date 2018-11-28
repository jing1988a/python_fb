# 给一个日志的文件， 每行第一个字符串是ID ,由数字和字母组成。根据每一行的第二个字符串来进行排序，然后只排含字母的，如果含有数字的话全都放在最下面，顺序按照原顺序不变
import functools
class Problem:
    def solve(self, log):
        def myCmp(a, b):
            def intOnly(text):
                temp = text.split(' ')
                return all(x.isdigit() for x in temp)

            identifier1, content1 = a.split(' ', 1)
            identifier2, content2 = b.split(' ', 1)

            numOnly1 = intOnly(content1)
            numOnly2 = intOnly(content2)

            if numOnly1 and numOnly2:
                return 0
            if numOnly1:
                return 1
            if numOnly2:
                return -1

            if content1==content2:
                if identifier1>identifier2:
                    return 1
                elif identifier1<identifier2:
                    return -1
                else:
                    return 0
            else:
                if content1>content2:
                    return 1
                else:
                    return -1

        log.sort(key=functools.cmp_to_key(myCmp))
        return log

test=Problem()
log=[ 'a1 9 2 3 1', 'g1 act car' , 'zo4 4 7' ,'ab1 off key dog' , 'a8 act zoo' ]
print(test.solve(log))
# it is more like asking do you know ho can you customized comparator works and can you write one.
# the idea is straight forward, fist split the identifier and body
# then write the comparator function as the question described
