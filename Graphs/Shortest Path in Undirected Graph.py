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
class Solution:
    def shortestPath(self, V, edges, src):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q=Queue()
        dist=[float('inf')]*V
        q.push(src)
        dist[src]=0
        while q.size()>0:
            u=q.pop()
            
            for v in adj[u]:
                if dist[u]+1 < dist[v]:
                    dist[v]=dist[u]+1
                    q.push(v)
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist