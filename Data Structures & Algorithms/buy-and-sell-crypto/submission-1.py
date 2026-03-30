class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0
        for R in range(len(prices)):
            while prices[R] < prices[L]:
                L += 1
            profit = max(profit, prices[R] - prices[L])

        return profit