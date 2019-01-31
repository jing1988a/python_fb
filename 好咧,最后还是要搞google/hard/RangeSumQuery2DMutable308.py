# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
#
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#
#


# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.



# 这道题让我们求二维区域和检索，而且告诉我们数组中的值可能变化，这是之前那道Range
# Sum
# Query
# 2
# D - Immutable的拓展，由于我们之前做过一维数组的可变和不可变的情况Range
# Sum
# Query - Mutable和Range
# Sum
# Query - Immutable，那么为了能够通过OJ，我们还是需要用到树状数组Binary
# Indexed
# Tree(参见Range
# Sum
# Query - Mutable)，其查询和修改的复杂度均为O(logn)，那么我们还是要建立树状数组，我们根据数组中的每一个位置，建立一个二维的树状数组，然后还需要一个getSum函数，以便求得从(0, 0)
# 到(i, j)
# 的区间的数字和，然后在求某一个区间和时，就利用其四个顶点的区间和关系可以快速求出，参见代码如下：
#
# http://www.cnblogs.com/grandyang/p/5300458.html

# http://www.cnblogs.com/grandyang/p/4985506.html
# 这道题是之前那道Range Sum Query - Immutable 区域和检索 - 不可变的延伸，之前那道题由于数组的内容不会改变，所以我们只需要建立一个累计数组就可以支持快速的计算区间值了，而这道题说数组的内容会改变，如果我们还是用之前的方法建立累计和数组，那么每改变一个数字，之后所有位置的数字都要改变，这样如果有很多更新操作的话，就会十分不高效。这道题我们要使用一种新的数据结构，叫做树状数组Binary Indexed Tree，又称Fenwick Tree，这是一种查询和修改复杂度均为O(logn)的数据结构。这个树状数组比较有意思，所有的奇数位置的数字和原数组对应位置的相同，偶数位置是原数组若干位置之和，假如原数组A(a1, a2, a3, a4 ...)，和其对应的树状数组C(c1, c2, c3, c4 ...)有如下关系：
#
#
#
# C1 = A1
# C2 = A1 + A2
# C3 = A3
# C4 = A1 + A2 + A3 + A4
# C5 = A5
# C6 = A5 + A6
# C7 = A7
# C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
# ...
# 那么是如何确定某个位置到底是有几个数组成的呢，原来是根据坐标的最低位Low Bit来决定的，所谓的最低位，就是二进制数的最右边的一个1开始，加上后面的0(如果有的话)组成的数字，例如1到8的最低位如下面所示：
#
# 坐标          二进制          最低位
#
# 1               0001          1
#
# 2               0010          2
#
# 3               0011          1
#
# 4               0100          4
#
# 5               0101          1
#
# 6               0110          2
#
# 7               0111          1
#
# 8               1000          8
#
# ...
#
# 最低位的计算方法有两种，一种是x&(x^(x–1))，另一种是利用补码特性x&-x。
#
# 这道题我们先根据给定输入数组建立一个树状数组bit，然后更新某一位数字时，根据最低位的值来更新后面含有这一位数字的地方，一般只需要更新部分偶数位置的值即可，在计算某一位置的前缀和时，利用树状数组的性质也能高效的算出来，参见代码如下：



#
# if brutefoce, update O(1), sum O(n * m) if preSum, update O(n * m), sum O(1)
#
# if only do prefix of row, update O(m), sum O(n)
#
# if Binary Indexed Tree.which is update O(logN * logM), sum(logN * logM)


class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]



        """
        self.matrix=matrix
        self.preSumMatrix = []
        for i in range(len(matrix)):
            cur = 0
            self.preSumMatrix.append([])
            for j in range(len(matrix[0])):
                cur += matrix[i][j]
                self.preSumMatrix[i].append(cur)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]

        for i in range(col, len(self.preSumMatrix[0])):
            self.preSumMatrix[row][i] = self.preSumMatrix[row][i] + diff
        self.matrix[row][col]=val
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.preSumMatrix[i][col2]
            if col1 != 0:
                ans -= self.preSumMatrix[i][col1 - 1]
        return ans


# ["NumMatrix","update","update","update","sumRegion"]
# [[[[2,4],[-3,5]]],[0,1,3],[1,1,-3],[0,1,1],[0,0,1,1]]

test = NumMatrix([[2,4],[-3,5]])
test.update(0,1,3)

test.update(1,1,-3)
test.update(0,1,1)

print(test.sumRegion(0,0,1,1))
