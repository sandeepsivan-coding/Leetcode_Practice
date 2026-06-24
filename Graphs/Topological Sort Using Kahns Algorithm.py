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
    def topoSort(self, V, edges):
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        inDegree=[0]*V
        for u,v in edges:
            inDegree[v]+=1
        q= Queue()
        for i in range(V):
            if inDegree[i]==0:
                q.push(i)
        ans=[]
        while q.size()>0:
            node=q.pop()
            ans.append(node)
            for x in adj[node]:
                inDegree[x]-=1
                if inDegree[x]==0:
                   q.push(x)
        return ans