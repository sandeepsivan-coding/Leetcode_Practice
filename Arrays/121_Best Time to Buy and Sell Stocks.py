class Solution(object):
    def maxProfit(self, prices):
        profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            curr_profit=prices[i]-min_price
            if curr_profit>profit:
                profit=curr_profit
            min_price=min(min_price,prices[i])
        return profit