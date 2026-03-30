class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # this is a traversal on a NEW island
            # we know this tile is a "1"
            q = []
            q.append((r, c))
            while q:
                curr_row, curr_col = q.pop()
                # set curr to visited
                grid[curr_row][curr_col] = "0"
                # check neighbours
                for dr, dc in DIRECTIONS:
                    nr, nc = curr_row + dr, curr_col + dc
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == "1"):
                        q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count