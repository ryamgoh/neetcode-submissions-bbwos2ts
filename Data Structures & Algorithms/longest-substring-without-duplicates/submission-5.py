class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        L = 0
        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            res = max(res, len(window))

        return res