class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        self.area = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return
            
            grid[r][c] = 0
            self.area += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)         

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.area = 0
                    dfs(r, c)
                    res = max(res, self.area)
                
        return res