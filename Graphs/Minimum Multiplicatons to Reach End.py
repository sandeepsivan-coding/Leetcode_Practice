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
    def minSteps(self, arr, start, end):
        if start==end:
            return 0
        q=Queue()
        q.push((0,start))
        mod=1000
        dist=[float('inf')]*mod
        dist[start]=0
        while q.size()>0:
            step,ans=q.pop()
            for x in arr:
                num=(x*ans)%mod
                if step+1<dist[num]:
                    dist[num]=step+1
                    if num==end:
                        return step+1
                    q.push((step+1 , num))
        return -1