import heapq
class Solution:
    def countPaths(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v,t in edges:
            adj[u].append((v,t))
            adj[v].append((u,t))
        hp=[]
        dist=[float('inf')]*V
        ways=[0]*V
        dist[0]=0
        ways[0]=1
        heapq.heappush(hp,(dist[0],0))
        while len(hp)>0:
            time,node=heapq.heappop(hp)
            if time>dist[node]:
                continue
            for v,t in adj[node]:
                if dist[node] + t < dist[v]:
                    dist[v]=dist[node] + t
                    heapq.heappush(hp,(dist[v],v))
                    ways[v]=ways[node]
                elif time+t==dist[v]:
                    ways[v]=ways[v]+ways[node]
        return ways[V-1]