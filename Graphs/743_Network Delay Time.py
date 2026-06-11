import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjList=[]
        for i in range(n):
            adjList.append([])
        for edge in times:
            x=edge[0]-1
            y=edge[1]-1
            w=edge[2]
            adjList[x].append([y,w])
            
        heap=[]
        dist=[float('inf')]*n
        dist[k-1]=0
        heapq.heappush(heap,(dist[k-1],k-1))
        while len(heap)>0:
            d,u=heapq.heappop(heap)
            for v,w in adjList[u]:
                if dist[u] + w < dist[v]:
                    dist[v]=dist[u] + w
                    heapq.heappush(heap,(dist[v],v))
        ans=max(dist)
        return -1 if ans==float('inf') else ans