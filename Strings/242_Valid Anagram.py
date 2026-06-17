class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for j in t:
            if j in dict1:
                dict1[j]-=1
            else:
                return False
        for i in dict1.values():
            if i!=0:
                return False
        return True