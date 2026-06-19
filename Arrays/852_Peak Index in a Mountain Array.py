class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l=0
        r=len(arr)-1
        ans=len(arr)
        while l<=r:
            m=(l+r)//2
            if arr[m]<arr[m+1]:
                l=m+1
            else:
                ans=m
                r=m-1
        return ans