class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    ans=True
    def isBipartite(self, graph):
        # Write your code here
        l=len(graph)
        state=[0 for i in range(l)]
        for i in range(l):
            if state[i]==0:
                self.dfs( i , graph , state , 1)
                if not self.ans:
                    return False
        return True
    def dfs(self , n , graph , state , flag):
        if state[n]!=0:
            if flag==-state[n]:
                self.ans=False
            return
        state[n]=flag
        for neighbor in graph[n]:
            self.dfs(neighbor , graph , state , -flag)