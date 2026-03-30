class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(row, col):
            from collections import deque
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.popleft()
                grid[r][c] = "0"
                for dr, dc in DIRECTIONS:
                    new_row = r + dr
                    new_col = c + dc
                    if (
                        new_row in range(ROWS) and
                        new_col in range(COLS) and
                        grid[new_row][new_col] == "1"                    
                    ):
                        q.append((new_row, new_col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1

        return count