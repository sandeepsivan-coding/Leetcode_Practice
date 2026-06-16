class Solution(object):
    def generateMatrix(self, n):
        total=n*n
        output=[[0 for j in range(n)]for _ in range(n)]
        c=0
        row_start=0
        col_start=0
        row_end=n-1
        col_end=n-1
        while c<total:
            for i in range(col_start,col_end+1):
                c+=1
                output[row_start][i]=c
                
            row_start+=1
            if c==total:
                break
            for i in range(row_start,row_end+1):
                c+=1
                output[i][col_end]=c
                
            col_end-=1
            if c==total:
                break
            for i in range(col_end,col_start-1,-1):
                c+=1
                output[row_end][i]=c
               
            row_end-=1
            if c==total:
                break
            for i in range(row_end,row_start-1,-1):
                c+=1
                output[i][col_start]=c
                
            col_start+=1
            if c==total:
                break
        return output