#
# 当时看了上面的贴子我还不是完全明白题目什么意思，和面试官交流后明白了要求什么。稍微解释下
#
# boolean allowDriverMode(shifts, current):
# shifts 就是一个的interval，按照顺时间顺序排好的，比如[[0-8], [10-12], [25,33]]
# current就是当前时间。
# 时间不是24小时制的,可以是任意大于0的数字，比如 40或100.
#
# 给一个shifts，给一个当前时间，求司机是否能进入驾驶模式。
# 在最近一次至少8小时休息后(必须是连续的休息时间)。
# 如果司机已经驾驶过12个小时，则不能进入驾驶模式。
# 否则返回可以。
# 周四面完后面试官和我说recruiter会notify me shortly. 到昨天还没消息。求过


class Solution:
    def allowDriverMode(self , shifts, current):
        # is it already sorted?
        #[ [1 , 7]]  8  is this true or false???
        l=len(shifts)
        if l==0:
            return True
        i=l-1
        total=0
        nextStart=current
        while i>-1:
            if total>=12:
                return False
            if nextStart-shifts[i][1]>=8:
                if total<12:
                    return True
            else:
                total+=shifts[i][1]-shifts[i][0]
                nextStart=shifts[i][0]
            i-=1

        return True

shifts=[(0, 4), (5, 9), (10, 14), (15, 19), (20, 24)]
current=24

test=Solution()
print(test.allowDriverMode(shifts , current))
