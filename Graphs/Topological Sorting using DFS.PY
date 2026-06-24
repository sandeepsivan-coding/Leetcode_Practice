
        
class Solution:
    def dfs(self,node,adj,visited,st):
        visited[node]=1
        for x in adj[node]:
            if not visited[x]:
                self.dfs(x,adj,visited,st)
        st.append(node)
    def topoSort(self, V, edges):
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
        visited=[0]*V
        st=[]
        ans=[]
        for i in range(V):
            if visited[i]!=1:
                self.dfs(i,adj,visited,st)
        while len(st)>0:
            ans.append(st.pop())