class Solution(object):
    def containsDuplicate(self, nums):
        nums_len=len(nums)
        nums_set=set(nums)
        len_set=len(nums_set)
        return nums_len!=len_set