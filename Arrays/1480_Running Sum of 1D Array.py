class Solution(object):
    def runningSum(self, nums):
        ans=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            ans.append(sum)
        return ans