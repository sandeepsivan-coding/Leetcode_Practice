class Solution(object):
    def maximumWealth(self, accounts):
        wealth=0
        for account in accounts:
            wealth=max(sum(account),wealth)
        return wealth