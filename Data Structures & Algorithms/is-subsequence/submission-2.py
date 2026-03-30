class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dp(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            if s[i] == t[j]:
                return dp(i + 1, j + 1)
            return dp(i, j + 1)
        
        return dp(0, 0)