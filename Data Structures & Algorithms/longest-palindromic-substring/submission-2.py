class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we want to return a string
        # 1. longest substring of s
        # 2. palindrome (eg. abcba)
        #   2a. if 2 or more substrings have same length, 
        #   we return any (we choose first one)
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res
                