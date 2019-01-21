# 同样是tree
# 给一个tree
# 和一个int
# sum
# 比如下面的tree和5
# 找出所有能加到5的connected
#         1
#      2       3
#    3   5   6   1
# 上面应该print
# 2
# 3, 5, 1
# 3
# 1


class Node:
    def __init__(self , val):
        self.val=val
        self.left=None
        self.right=None
class Problem:
    def solve(self , root , k):
        self.ans=[]

        self.recur(root , k)
        return self.ans
    def checkAllPath(self , node  , k , candidate):
        #print(candidate)

        if not node:
            return
        candidate.append(node.val)
        if k-node.val == 0:
            self.ans.append(candidate[::])
        self.checkAllPath(node.left , k-node.val , candidate)
        self.checkAllPath(node.right , k-node.val , candidate)
        candidate.pop()

    def recur(self , node , k):
        if not node:
            return
        candidate = []
        self.checkAllPath(node , k , candidate)

        self.recur(node.left , k)
        self.recur(node.right , k)

root=Node(1)
a=Node(2)
b=Node(3)
c=Node(3)
d=Node(5)
e=Node(6)
f=Node(1)
root.left=a
root.right=b
a.left=c
a.right=d
b.left=e
b.right=f

test=Problem()
print(test.solve(root , 5))