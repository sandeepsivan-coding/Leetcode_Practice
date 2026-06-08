class Solution(object):
    def countDigits(self, num):
        count=0
        temp=num
        l=len(str(num))
        for i in range(l):
            digit=num%10
            if temp % digit ==0:
                count+=1
            num//=10
        return count