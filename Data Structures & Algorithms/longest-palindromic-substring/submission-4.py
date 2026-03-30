class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we want to return a string
        # 1. longest substring of s
        # 2. palindrome (eg. abcba)
        #   2a. if 2 or more substrings have same length, 
        #   we return any (we choose first one)

        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            

            # even len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return res