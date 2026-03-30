class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        time = 0
        fresh = 0
        q = deque()
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # mark this as visited (but we already know its visited here, because its ROTTEN)
        while q and fresh > 0: # this exits earlier
            time += 1
            curr_frontier = len(q)
            for _ in range(curr_frontier):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if nr in range(len(grid)) and \
                        nc in range(len(grid[0])) and \
                        grid[nr][nc] == 1:
                        # mark visited
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return time if fresh == 0 else -1