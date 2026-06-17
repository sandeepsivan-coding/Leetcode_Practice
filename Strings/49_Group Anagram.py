class Solution(object):
    def groupAnagrams(self, strs):
        dict1={}
        for i in strs:
            j="".join(sorted(i))
            if j in dict1:
                dict1[j].append(i)
            else:
                dict1[j]=i
        return list[dict1.values()]