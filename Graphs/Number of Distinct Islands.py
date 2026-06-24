class Solution:
    def dfs(self,r,c,visited,grid,ans,r0,c0):
        visited[r][c]=1
        m=len(grid)
        n=len(grid[0])
        ans.append((r-r0,c-c0))
        dirs=[(-1,0),(1,0),(0,1),(0,-1)]
        for dr,dc in dirs:
            nrow=r+dr
            ncol=c+dc
            if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]!=1 and grid[nrow][ncol]=="L":
                self.dfs(nrow,ncol,visited,grid,ans,r0,c0)
    def countDistinctIslands(self, grid):
        m=len(grid)
        n=len(grid[0])
        set1=set()
        visited=[[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j]!=1 and grid[i][j]=="L":
                    ans=[]
                    self.dfs(i,j,visited,grid,ans,i,j)
                    set1.add(tuple(ans))
        return len(set1)