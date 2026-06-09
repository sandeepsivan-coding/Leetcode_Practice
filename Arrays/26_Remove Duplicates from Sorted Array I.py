class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        start=0
        for i in range(1,l):
            if nums[i]!=nums[start]:
                start+=1
                nums[start]=nums[i]
        return start+1