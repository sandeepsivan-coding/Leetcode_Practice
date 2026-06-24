class Solution:
    def bellmanFord(self, V, edges, src):
        dist=[10**8]*V
        dist[src]=0
        for _ in range(V):
            for u,v,wt in edges:
                if dist[u]!=10**8 and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        for u,v,wt in edges:
            if dist[u]!=10**8 and dist[u] + wt < dist[v]:
                return -1
        return dist