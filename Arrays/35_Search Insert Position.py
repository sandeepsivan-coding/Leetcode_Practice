class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        ans=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>=target:
                ans=m
                r=m-1
            else:
                l=m+1
        return ans