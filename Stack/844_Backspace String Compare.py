class Solution(object):
    def backspaceCompare(self, s, t):
        s1=[]
        s2=[]
        for i in s:
            if i!="#":
                s1.append(i)
            else:
                if len(s1)>0:
                    s1.pop()
        for i in t:
            if i!="#":
                s2.append(i)
            else:
                if len(s2)>0:
                    s2.pop()

        return s1==s2