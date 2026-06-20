class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums2)
        ans={}
        s=[]
        for i in range(n-1,-1,-1):
            while len(s)>0 and s[-1]<=nums2[i]:
                s.pop()
            if len(s)==0:
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=s[-1]
            s.append(nums2[i])
        res=[]
        for i in nums1:
            res.append(ans[i])
        return res