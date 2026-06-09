class Solution(object):
    def reverse(self, x):
        a=(2**31)-1
        b=len(str(x))
        if x>=0:
            rev=0
            for i in range(b):
                rem=x%10
                rev=rev*10+rem
                x=x//10
        elif x<0:
            x=abs(x)
            rev=0
            for i in range(b-1):
                rem=x%10
                rev=rev*10+rem
                x=x//10
            rev=-rev

        if rev<a and rev>(-a):
            return rev
        else:
            return 0