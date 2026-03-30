class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        memo = {}
        def dp(i: int) -> int:
            if i >= len(s):
                return 0
            if i in memo:
                return memo[i]

            # option 1
            result = 1 + dp(i + 1)

            # option 2
            for word in dictionary:
                if s.startswith(word, i):
                    result = min(result, dp(i + len(word)))

            memo[i] = result
            return memo[i]

        return dp(0)