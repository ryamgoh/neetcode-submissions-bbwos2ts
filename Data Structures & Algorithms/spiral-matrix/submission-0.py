class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        directions = {
            "GO_RIGHT": [0, 1],   # Move right (increase column)
            "GO_DOWN": [1, 0],    # Move down (increase row)
            "GO_LEFT": [0, -1],   # Move left (decrease column)
            "GO_UP": [-1, 0]      # Move up (decrease row)
        }

        curr_direction = "GO_RIGHT"        
        i, j = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        
        res = [matrix[i][j]]
        visited = {(i, j)}
        
        while len(res) < rows * cols:
            # Calculate next position
            next_i = i + directions[curr_direction][0]
            next_j = j + directions[curr_direction][1]
            
            # Check if next position is valid and not visited
            if (0 <= next_i < rows and 
                0 <= next_j < cols and 
                (next_i, next_j) not in visited):
                # Move to next position
                i, j = next_i, next_j
                res.append(matrix[i][j])
                visited.add((i, j))
            else:
                # Change direction
                if curr_direction == "GO_RIGHT":
                    curr_direction = "GO_DOWN"
                elif curr_direction == "GO_DOWN":
                    curr_direction = "GO_LEFT"
                elif curr_direction == "GO_LEFT":
                    curr_direction = "GO_UP"
                else:  # GO_UP
                    curr_direction = "GO_RIGHT"
        
        return res