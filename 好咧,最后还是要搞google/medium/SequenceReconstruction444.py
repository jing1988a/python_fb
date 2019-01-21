# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.
#
# Example 1:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
#
# Output:
# false
#
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:
#
# Input:
# org: [1,2,3], seqs: [[1,2]]
#
# Output:
# false
#
# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
#
# Output:
# true
#
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:
#
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
#
# Output:
# true
# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.



# 题目大意：
# 判断原始序列org能否由一组序列seqs重建。org序列是整数1到n的一个排列，其中1 ≤ n ≤ 10^4。重建意味着使用seqs中的序列构建一个最短公共超序列（也就是说，一个最短的序列满足seqs中的所有序列均为其子序列）。判断seqs中的序列能否唯一确定org序列。
#
# 解题思路：
# 解法I 拓扑排序（Topological Sort）
#
# 将seqs中的各序列seq按照其中元素出现的先后顺序建立有向图g。
#
# 例如seqs中的某序列seq = [1, 2, 3]，对应有向图，顶点为1, 2, 3；边为(1, 2), (2, 3)。
#
# 利用数组indeg记录各顶点的入度（indegree），sucset记录各顶点的后继（边）。
#
# 然后对图g执行拓扑排序，将得到的排序结果与原始序列org作比对即可。


# class Solution(object):
#     def sequenceReconstruction(self, org, seqs):
#         """
#         :type org: List[int]
#         :type seqs: List[List[int]]
#         :rtype: bool
#         """
#         size = len(org)
#         indeg = [0] * size
#         sucset = [set() for x in range(size)]
#         if not seqs: return False
#         for seq in seqs:
#             if any(s > size or s < 1 for s in seq):
#                 return False
#             for i in range(1, len(seq)):
#                 if seq[i] not in sucset[seq[i - 1] - 1]:
#                     indeg[seq[i] - 1] += 1
#                     sucset[seq[i - 1] - 1].add(seq[i])
#         print(sucset)
#         print(indeg)
#         q = [i for i in org if not indeg[i - 1]]
#         for x in range(size):
#             if len(q) != 1 or q[0] != org[x]:
#                 return False
#             nq = []
#             for suc in sucset[q[0] - 1]:
#                 indeg[suc - 1] -= 1
#                 if not indeg[suc - 1]:
#                     nq.append(suc)
#             q = nq
#         return True
#
# test=Solution()
# test.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])


import collections


class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs:
            if not org:
                return True
            return False
        n = len(org)
        graph, degree, valid = self.constructGraph(seqs, n)

        print(graph)
        print(degree)
        print(valid)
        if not valid or not graph:
            return False
        return self.check(org, graph, degree , n)

    def constructGraph(self, seqs, n):
        degree = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        for seq in seqs:
            if any(s < 1 or s > n for s in seq):
                return None, None, False
            if len(seq)!=0 and seq[0] not in graph:
                graph[seq[0]]=set()
            for i in range(1, len(seq)):
                if seq[i] not in graph[seq[i - 1]]:
                    graph[seq[i - 1]].add(seq[i])
                    degree[seq[i]] += 1
        return graph , degree , True
    def check(self , org , graph , degree , n):
        q=[]
        for i in range(1, n+1):
            if not i in degree:
                q.append(i)
        cur=0
        #print(q)
        if not q:
            return False
        while q:
            p=[]
            if len(q)!=1 or q[0]!=org[cur]:
                return False
            parent=q[0]
            for child in graph[parent]:
                degree[child]-=1
                if degree[child]==0:
                    p.append(child)
            q=p
            cur+=1

        return cur==n

test=Solution()
# print(test.sequenceReconstruction([1], [[1], [1]]))
print(test.sequenceReconstruction([1,2,3,4] , [[1,2,3],[3,4],[4,3]]))