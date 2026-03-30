class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        maximum = 0

        # Traverse from top-left to bottom-right
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = 1 + min(
                        dp[r-1][c],    # up
                        dp[r][c-1],    # left
                        dp[r-1][c-1]   # diagonal up-left
                    )
                    maximum = max(maximum, dp[r][c])

        return maximum * maximum