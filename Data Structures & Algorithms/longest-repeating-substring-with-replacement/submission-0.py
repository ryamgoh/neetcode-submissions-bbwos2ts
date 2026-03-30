class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int)

        L = 0
        window_max = float("-inf")
        for R in range(len(s)):
            count[s[R]] += 1
            window_max = max(count[s[R]], window_max)

            while (R - L + 1) - k > window_max:
                count[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res
