class Solution:
    def dfs(self,i,adj,visited,st):
        visited[i]=1
        for (v,wt) in adj[i]:
            if visited[v]!=1:
                self.dfs(v,adj,visited,st)
        st.append(i)
    def shortestPath(self, V ,E, edges):
        adj=[[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v,wt))
        visited=[0]*V
        st=[]
        for i in range(V):
            if visited[i]!=1:
                self.dfs(i,adj,visited,st)
        ans=[float('inf')]*V
        ans[0]=0
        while len(st)>0:
            node=st.pop()
            if ans[node]!= float('inf'):
                for (v,wt) in adj[node]:
                    if ans[node]+wt<ans[v]:
                        ans[v]=ans[node]+wt
        for i in range(V):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans