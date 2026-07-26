class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS on the treasures

        CANNOT_MOVE = -1
        TREASURE = 0
        MOVEABLE = 2147483647

        q = deque()

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    q.append((r,c))

        count = 0
        while q:
            count += 1
            level_size = len(q)

            for _ in range(level_size):
                row, col = q.popleft()

                for dr, dc in dirs:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < rows and \
                        0 <= new_col < cols and \
                        grid[new_row][new_col] == MOVEABLE:
                        grid[new_row][new_col] = count
                        q.append((new_row,new_col))

        