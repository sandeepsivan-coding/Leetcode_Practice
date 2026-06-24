from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        adj=[[] for _ in range(n+1)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        heap=[]
        dist=[float('inf')]*(n+1)
        dist[1]=0
        heapq.heappush(heap,(dist[1],1))
        parent=[i for i in range(n+1)]
        while len(heap)>0:
            wt,u=heapq.heappop(heap)
            if wt>dist[u]:
                continue
            for v,w in adj[u]:
                if dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    heapq.heappush(heap,(dist[v],v))
                    parent[v]=u
        if dist[n]==float('inf'):
            return [-1]
        path=[]
        node=n
        while parent[node]!=node:
            path.append(node)
            node=parent[node]
        path.append(1)
        path.reverse()
        return [dist[n]]+path