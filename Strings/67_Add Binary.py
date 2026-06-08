class Solution(object):
    def bintodec(self,y):
        ans=0
        for i in y:
            ans=(ans*2)+int(i)
        return ans


    def dectobin(self,x):
        if x==0:
            return "0"
        ans=''
        while x>0:
            ans=str(x%2) + ans
            x//=2
        return str(ans)

    def addBinary(self, a, b):
        x=self.bintodec(a)
        y=self.bintodec(b)
        
        res=self.dectobin(x+y)
        return res
