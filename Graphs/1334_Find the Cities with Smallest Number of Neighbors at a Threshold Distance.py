class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        adj=[[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            adj[i][i]=0
        for u,v,wt in edges:
            adj[u][v]=wt
            adj[v][u]=wt
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][k] != float('inf') and adj[k][j]!= float('inf'):
                        adj[i][j]=min(adj[i][j], (adj[i][k]+ adj[k][j]))
        cityCount=n
        city=-1
        for i in range(n):
            count=0
            for j in range(n):
                if adj[i][j]<=distanceThreshold:
                    count+=1
            if count<=cityCount:
                cityCount=count
                city=i
        return city