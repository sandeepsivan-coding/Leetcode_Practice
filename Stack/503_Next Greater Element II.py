class Solution(object):
    def nextGreaterElements(self, nums):
        nums+=nums
        n=len(nums)
        ans=[0]*n
        s=[]
        for i in range(n-1,-1,-1):
            while len(s)>0 and s[-1]<=nums[i]:
                s.pop()
            if len(s)==0:
                ans[i]=-1
            else:
                ans[i]=s[-1]
            s.append(nums[i])
        return ans[:len(nums)//2]