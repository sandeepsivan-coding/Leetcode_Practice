import heapq
class Solution:
    def spanningTree(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        hp=[]
        visited=[0]*V
        sum1=0
        mst=[]
        heapq.heappush(hp,(0,0,-1))
        while len(hp)>0:
            wt , node , parent = heapq.heappop(hp)
            if visited[node]==1:
                continue
            visited[node]=1
            sum1+=wt
            mst.append([parent,node])
            for v,w in adj[node]:
                if visited[v]!=1:
                    heapq.heappush(hp,(w,v,u))
        return sum1