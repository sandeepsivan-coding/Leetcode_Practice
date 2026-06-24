import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        m=len(heights)
        n=len(heights[0])
        dist=[[float('inf') for i in range(n)]for _ in range(m)]
        hp=[]
        dist[0][0]=0
        heapq.heappush(hp,(0,(0,0)))
        while len(hp)>0:
            d,(row,col)=heapq.heappop(hp)
            if row==m-1 and col==n-1:
                return d
            dirs=[(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in dirs:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<m and 0<=ncol<n:
                    newEffort=max(abs(heights[row][col]-heights[nrow][ncol]),d)
                    if newEffort< dist[nrow][ncol]:
                        dist[nrow][ncol]=newEffort
                        heapq.heappush(hp,(newEffort,(nrow,ncol)))
        return 0