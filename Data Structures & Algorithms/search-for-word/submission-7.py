from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c, index):
            # Found the entire word
            if index >= len(word):
                return True
            
            # Check bounds and character match
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                board[r][c] != word[index] or (r, c) in visited):
                return False
            
            # Mark as visited by temporarily changing the cell
            visited.add((r, c))
            
            # Explore all 4 directions
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            # Backtrack - restore the cell
            visited.remove((r, c))

            return found
        
        # Try starting from each cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False