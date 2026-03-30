class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # do bfs on the treasures
        # to deal with conflicts, we just take the smaller of the two. 
        # if we found a smaller one, we should just stop traversing there.
        INF = 2**31 - 1
        WATER = -1
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # Find all treasure chests (0) and add them to queue as starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Treasure chest
                    q.append((r, c))
        
        # Multi-source BFS
        distance = 0
        while q:
            distance += 1
            level_size = len(q)
            
            for _ in range(level_size):
                r, c = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    
                    # Check if within bounds and if it's land (INF) or needs updating
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == INF):
                        grid[nr][nc] = distance
                        q.append((nr, nc))