class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]<target:
                l=mid+1
            else:
                r=mid-1
        return False