import collections
class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """

    def findMinHeightTrees(self, n, edges):
        # Wirte your code here
        graph = self.construct(n, edges)
        q = []
        for n in graph:
            if len(graph[n]) == 1:
                q.append(n)
        while q and len(graph) > 2:
            p = []
            for n in q:
                candidate = graph[n].pop()
                graph[candidate].remove(n)
                if len(graph[candidate]) == 1:
                    p.append(candidate)
                del graph[n]
            q = p
        return list(graph.keys())

    def construct(self, n, edges):
        graph = collections.defaultdict(set)
        for i in range(n):
            graph[i] = set()
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph

test=Solution()
print(test.findMinHeightTrees( 4 , [[1,0],[1,2],[1,3]]  ))