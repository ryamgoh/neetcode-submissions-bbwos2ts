class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count = 0

        def dfs(r, c):
            # check if invalid
            # what is invalid?
            # out of bound?
            # is 0? (meaning not an island)
            if (r < 0 or r >= len(grid) or 
                c < 0 or c >= len(grid[0]) or 
                grid[r][c] == "0"):
                return

            # if valid, we should set this to visited
            grid[r][c] = "0"
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r + dr, c + dc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
                # we would already recurse!

        return count

