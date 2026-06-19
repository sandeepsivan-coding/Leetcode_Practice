class Solution(object):
    def searchRange(self, nums, target):
        l=0
        r=len(nums)-1
        ans1=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>=target:
                ans1=m
                r=m-1
            else:
                l=m+1
        l=0
        r=len(nums)-1
        ans2=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>target:
                ans2=m
                r=m-1
            else:
                l=m+1
        if ans1==ans2:
            return [-1,-1]
        else:
            return [ans1,ans2-1]