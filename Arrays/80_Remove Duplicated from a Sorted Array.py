class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        start=1
        if l<=2:
            return l
        for i in range(2,l):
            if nums[i]!=nums[start-1]:
                start+=1
                nums[start]=nums[i]
        return start+1