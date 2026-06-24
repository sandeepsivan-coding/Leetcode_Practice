class Solution(object):
    def dfs(self,row,col,ans,image,color,initColor):
        image[row][col]=color
        m=len(image)
        n=len(image[0])
        dirs=[(-1,0),(1,0),(0,1),(0,-1)]
        for dr,dc in dirs:
            nrow=row+dr
            ncol=col+dc
            if 0<=nrow<m and 0<=ncol<n and image[nrow][ncol]==initColor and image[nrow][ncol]!=color:
                self.dfs(nrow,ncol,ans,image,color,initColor)


    def floodFill(self, image, sr, sc, color):
        ans=image
        initColor=image[sr][sc]
        self.dfs(sr,sc,ans,image,color,initColor)
        return ans