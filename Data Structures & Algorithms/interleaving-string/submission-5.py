class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        
        def dp(i, j):
            k = i + j
            if k == len(s3):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            res1 = res2 = False
            if i < len(s1) and s3[k] == s1[i]:
                res1 = dp(i + 1, j)
            if j < len(s2) and s3[k] == s2[j]:
                res2 = dp(i, j + 1)
            
            memo[(i, j)] = res1 or res2
            return memo[(i, j)]

        return dp(0, 0)