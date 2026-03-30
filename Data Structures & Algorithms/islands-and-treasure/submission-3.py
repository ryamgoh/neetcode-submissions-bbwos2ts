class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        q = deque()
        
        # BFS Method
        def bfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == -1 or (r, c) in visited):
                return
            visited.add((r, c))
            q.append([r, c])


        # Start at the 0s
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                # populate the element
                grid[r][c] = dist
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    bfs(r + dr, c + dc)

            dist += 1