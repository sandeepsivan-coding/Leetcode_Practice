import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        heap=[]
        dist=[float('inf')]*V
        dist[src]=0
        heapq.heappush(heap,(dist[src],src))
        while len(heap)>0:
            wt,u = heapq.heappop(heap)
            if wt>dist[u]:
                continue
            for v,w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v]=dist[u] + w
                    heapq.heappush(heap,(dist[v],v))
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist