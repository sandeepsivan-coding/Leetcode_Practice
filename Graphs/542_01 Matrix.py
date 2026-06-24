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
    def updateMatrix(self, mat):
        m=len(mat)
        n=len(mat[0])
        visited=[[0 for i in range(n)] for _ in range(m)]
        output=[[0 for i in range(n)] for _ in range(m)]
        q=Queue()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.push(([i,j],0))
                    visited[i][j]=1
        t=0
        while q.size()>0:
            (r,c),t=q.pop()
            
            output[r][c]=t
            dirs=[(-1,0),(1,0),(0,1),(0,-1)]
            for dr,dc in dirs:
                nrow=r+dr
                ncol=c+dc
                if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]!=1 and mat[nrow][ncol]==1:
                    q.push(([nrow,ncol],t+1))
                    visited[nrow][ncol]=1
        return output