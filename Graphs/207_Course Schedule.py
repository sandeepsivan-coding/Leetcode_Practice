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
    def canFinish(self, numCourses, prerequisites):
        adj=[[] for i in range(numCourses)]
        inDegree=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            inDegree[u]+=1
        q=Queue()
        for i in range(numCourses):
            if inDegree[i]==0:
                q.push(i)
        count=0
        while q.size()>0:
            node=q.pop()
            count+=1
            for x in adj[node]:
                inDegree[x]-=1
                if inDegree[x]==0:
                    q.push(x)
        if count==numCourses:
            return True
        return False