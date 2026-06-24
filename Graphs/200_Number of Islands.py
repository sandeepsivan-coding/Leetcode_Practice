class Solution(object):
    def dfs(self,i,j,grid):
        grid[i][j]="0"
        m=len(grid)
        n=len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr, dc in dirs:
            nrow = i + dr
            ncol = j + dc
            if(0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]=="1"):
                    self.dfs(nrow,ncol,grid)


    def numIslands(self, grid):
        m=len(grid)
        n=len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    ans+=1
                    self.dfs(i,j,grid)
        return ans