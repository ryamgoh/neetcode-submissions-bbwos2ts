class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            # base case
            if i <= 2:
                return i
            
            if i in memo:
                return memo[i]

            # make choices
            result = dp(i - 1) + dp(i - 2)

            memo[i] = result
            return result

        return dp(n)