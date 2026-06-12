class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        a=nums[0]
        b=max(nums[0],nums[1])
        for i in range(2,n):
            not_take=b
            take=nums[i]+a
            c=max(not_take,take)
            a=b
            b=c
        return b