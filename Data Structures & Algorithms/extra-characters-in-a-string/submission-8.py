class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        memo = {}
        def dp(i: int) -> int:
            if i >= len(s):
                return 0
            if i in memo:
                return memo[i]

            # Option 1: Skip current character
            result1 = 1 + dp(i + 1)

            # Option 2: Find the best match among all words
            result2 = float("inf")
            for word in dictionary:
                if s.startswith(word, i):
                    # Take minimum across all matching words
                    result2 = min(result2, dp(i + len(word)))

            memo[i] = min(result1, result2)
            return memo[i]

        return dp(0)