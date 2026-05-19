class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # The idea is to make a choice for each coin
        # 1. Skip the coin and MOVE to the next one
        # 2. Use the coin and reduce the remaining amount (amount - coin) to 0

        # Recursion makes sense here, because each choice leads to a smaller subproblem
        # FN: How many ways can I form amount 'a' using coins starting from index i?
        coins.sort()
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return 1
            elif remaining < 0:
                return 0

            if i >= len(coins):
                return 0

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            res = 0
            res += dfs(i + 1, remaining)
            res += dfs(i, remaining - coins[i])

            memo[(i, remaining)] = res
            
            return res

        return dfs(0, amount)
