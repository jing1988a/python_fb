# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.



# Definition for a binary tree node.





#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """

# #         if root is None:
# #             return None
# #         s = ""

# #         l = self.serialize(root.left)
# #         r = self.serialize(root.right)
# #         s+=str(root.val)
# #         if not l is None:
# #             s+=','
# #             s+=l

# #         if not r is None:
# #             s+=','
# #             s+=r

# #         return s


#         if root is None:
#             return None
#         s=""
#         s+=str(root.val)
#         l=self.serialize(root.left)
#         r=self.serialize(root.right)
#         if l :
#             s+=','
#             s+=l
#         if r :
#             s+=','
#             s+=r

#         return s

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """

# #         if data is None:
# #             return None
# #         nodes = map(int, data.split(','))

# #         l = len(nodes)


# #         return self.recur(nodes, 0, l - 1)

#         if data is None:
#             return None


#         formated_node= map(int , data.split(','))


#         l=len(formated_node)


#         return self.recur(formated_node , 0  , l-1)

#     def recur(self, data, s, e):

# #         if s > e:
# #             return None

# #         root = TreeNode(data[s])
# #         rNodeIndex = e+1

# #         for i in range(s + 1, e + 1):
# #             if data[i] > data[s]:
# #                 rNodeIndex=i
# #                 break

# #         root.left = self.recur(data, s + 1, rNodeIndex - 1)
# #         root.right = self.recur(data, rNodeIndex, e)

# #         return root

#         if s>e:
#             return None

#         root=TreeNode(data[s])

#         rNodeIndex=e+1 # if there is no right tree this is the default

#         for i in range(s+1 , e+1):
#             if data[i]>data[s]:
#                 #if it is bigger than root , then it is the first node of right sub tree
#                 rNodeIndex=i
#                 break


#         root.left=self.recur(data , s+1 , rNodeIndex-1)
#         root.right=self.recur(data ,  rNodeIndex , e)

#         return root




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        l=self.serialize(root.left)
        r=self.serialize(root.right)
        ans=str(root.val)
        if l:
            # can improve here
            ans+='|'+l
        if r :
            ans+='|'+r
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data=list(map(int ,  data.split('|')))
        return self.recurBuild(data)

    def recurBuild(self , data):
        if not data:
            return None
        root=TreeNode(data[0])
        rightIdx=1
        while rightIdx<len(data):
            if data[rightIdx]>data[0]:
                break
            rightIdx+=1
        root.left=self.recurBuild(data[1:rightIdx])
        root.right=self.recurBuild(data[rightIdx:])
        return root





root=TreeNode(44)
root

