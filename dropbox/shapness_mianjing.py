# 10.	2-d array of "sharpness" values： Fine the path from left to right which has the highest minimum sharpness. 路径必须是从左往右，先有个起始点，然后每次要往右上，正右或右下跳一步。也就是说，路径长度是列数n，假设路径为(i1,1),(i2,2),...,(in,n)，路径必须满足每对i_k与i_{k-1}的距离不能大于1.
# .5 .7 .2
# .7 .5 .8
# .9 .1 .5more.
# 在这个例子中，理想路径是.7->.7->.8因为这条路径中的最小值.7在所有路径中最大。只需要返回这个值，不需要返回路径。http://www.1point3acres.com/bbs/thread-177627-1-1.html
#
# 从最左一列中的任意一个出发，到达最右一列的任意一个，要求：
# 1）当前格子要想往右走，只能往右上、右边、右下三个格子移动；
# 2）一条path中最小的那个值才是这条path的合格value；-google 1point3acres
# 3）在所有path中找到合格value最大的那一条，输出它的value。

class Shapness:

    def solve(self , matrix):
        n=len(matrix)
        m=len(matrix[0])
        dp=[[None for i in range(m)] for j in range(n)]
        for i in range(n):
            dp[i][0]=matrix[i][0]
        res=0
        for j in range(1 , m):
            for i in range(n):
                prePathMin=dp[i][j-1]
                if i-1>=0:
                    prePathMin=max(prePathMin , dp[i-1][j-1])
                if i + 1 < n:
                    prePathMin = max(prePathMin, dp[i + 1][j - 1])
                dp[i][j]=min(prePathMin , matrix[i][j])
                res=max(res , dp[i][j])
        return res


