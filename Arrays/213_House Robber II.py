class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        a=nums[0]
        b=max(nums[0],nums[1])
        for i in range(2,n-1):
            not_take=b
            take=nums[i]+a
            c=max(not_take,take)
            a=b
            b=c
        ans1=b
        a=nums[1]
        b=max(nums[1],nums[2])
        for i in range(3,n):
            not_take=b
            take=nums[i]+a
            c=max(not_take,take)
            a=b
            b=c
        ans2=b
        return max(ans1,ans2)