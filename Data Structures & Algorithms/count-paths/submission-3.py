class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if (i == m - 1 and j == n - 1):
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            res1, res2 = 0, 0
            if (i + 1 < m):
                res1 = dfs(i + 1, j)
            if (j + 1 < n):
                res2 = dfs(i, j + 1)
            memo[(i, j)] = res1 + res2
            return memo[(i, j)]

        return dfs(0, 0)