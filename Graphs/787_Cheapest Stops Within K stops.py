class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1
    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x=self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
            self.front=-1
            self.q=[]
        return x
    def size(self):
        if self.front==-1:
            return 0
        return len(self.q)-self.front
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj=[[] for _ in range(n)]
        for u,v,c in flights:
            adj[u].append((v,c))
        q=Queue()
        cost=[float('inf')]*n
        cost[src]=0
        q.push((0,src,0))
        while q.size()>0:
            stop,node,Currcost=q.pop()
            if stop>k:
                continue
            for v,c in adj[node]:
                if Currcost+c<cost[v]:
                    cost[v]=Currcost+c
                    q.push(((stop+1),v,cost[v]))

        if cost[dst]==float('inf'):
            return -1
        else:
            return cost[dst]