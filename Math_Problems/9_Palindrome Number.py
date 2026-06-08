class Solution(object):
    def isPalindrome(self, x):
        temp=x

        ans=0
        while x>0:
            rem=x%10
            ans=(ans*10)+rem
            x=x//10
        return temp==ans