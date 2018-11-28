# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.



class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.maxStack=[]
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.maxStack or x>=self.maxStack[-1]:
            self.maxStack.append(x)
        else:
            self.maxStack.append(self.maxStack[-1])

    def pop(self):
        """
        :rtype: int
        """
        cur=self.stack.pop()
        self.maxStack.pop()
        return cur


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxStack[-1]


    def popMax(self):
        """
        :rtype: int
        """
        temp=[]
        curMax=self.maxStack[-1]
        while self.stack[-1]!=self.maxStack[-1]:
            temp.append(self.stack.pop())
            self.maxStack.pop()
        self.stack.pop()
        self.maxStack.pop()
        while temp:
            self.push(temp.pop())
        return curMax