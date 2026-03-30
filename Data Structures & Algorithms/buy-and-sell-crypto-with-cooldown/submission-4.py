class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}  # Single memo with state as part of key
        
        def dp(i, holding):
            """
            i: current day
            holding: 0 = not holding (can buy), 1 = holding (can sell)
            """
            if i >= n:
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # Option 1: Skip today
            do_nothing = dp(i+1, holding)
            
            if holding:
                # Option 2: Sell today
                # After selling, we skip tomorrow (cooldown)
                do_something = prices[i] + dp(i+2, 0)
            else:
                # Option 2: Buy today
                do_something = -prices[i] + dp(i+1, 1)
            
            result = max(do_nothing, do_something)
            memo[(i, holding)] = result
            return result
        
        return dp(0, 0)