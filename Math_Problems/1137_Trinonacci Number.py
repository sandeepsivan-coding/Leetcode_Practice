class Solution(object):
    def tribonacci(self, n):
        result = []
        for i in range(n+1):
            if i == 0 or i == 1:
                result.append(i)
            elif i == 2:
                result.append(1)
            elif i > 2:
                result.append(result[i - 1] + result[i - 2] + result[i - 3])
        return result[-1]