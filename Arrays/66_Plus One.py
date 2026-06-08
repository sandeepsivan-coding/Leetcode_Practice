class Solution(object):
    def plusOne(self, digits):
        num=int("".join(str(h) for h in digits))
        num+=1
        return [int(d) for d in str(num)]