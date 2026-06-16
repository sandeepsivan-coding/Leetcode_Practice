class Solution(object):
    def spiralOrder(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        total=m*n
        output=[]
        c=0
        row_start=0
        col_start=0
        row_end=m-1
        col_end=n-1
        while c<total:
            for i in range(col_start,col_end+1):
                output.append(matrix[row_start][i])
                c+=1
            row_start+=1
            if c==total:
                break
            for i in range(row_start,row_end+1):
                output.append(matrix[i][col_end])
                c+=1
            col_end-=1
            if c==total:
                break
            for i in range(col_end,col_start-1,-1):
                output.append(matrix[row_end][i])
                c+=1
            row_end-=1
            if c==total:
                break
            for i in range(row_end,row_start-1,-1):
                output.append(matrix[i][col_start])
                c+=1
            col_start+=1
            if c==total:
                break
        return output