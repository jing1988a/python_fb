class Lca:
    def solve(self, root, a, b):
        if not root:
            return [None , None]
        if root.val == a or root.val == b:
            return [root, True]
        l, flagL = self.solve(root.left, a, b)
        r, flagR = self.solve(root.right, a, b)
        if l and r:
            return [root , False]
        if l:
            if flagL:
                return [root, False]
            else:
                return [l, False]
        if r:
            if flagR:
                return [root, False]
            else:
                return [r, False]
        return [None  , None]


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root=Node(5)
d=Node(6)
c = Node(0)
a = Node(1)
b = Node(2)
root.left=c
root.right=d
c.left = a
a.left = b
test = Lca()
print(test.solve(root, 1, 2)[0].val)
