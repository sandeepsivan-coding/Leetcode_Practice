class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        current_sum=0
        max_sum=nums[0]
        for i in range(n):
            current_sum+=nums[i]
            if current_sum>max_sum:
                max_sum=current_sum
            if current_sum<0:
                current_sum=0
        return max_sum