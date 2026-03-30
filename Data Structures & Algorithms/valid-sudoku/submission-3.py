class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_row_ok(row, col):
            curr = board[row][col]
            if curr == ".":
                return True
            for c in range(9):
                if c != col and board[row][c] == curr:
                    # same number but not same column, that means we found a duplicate
                    return False
            return True

        def is_col_ok(row, col):
            curr = board[row][col]
            if curr == ".":
                return True
            for r in range(9):
                if r != row and board[r][col] == curr:
                    return False
            return True

        def is_box_ok(row, col):
            curr = board[row][col]
            if curr == ".":
                return True
            curr_box_row = row // 3
            curr_box_col = col // 3

            for r in range(3):
                for c in range(3):
                    new_r = curr_box_row * 3 + r
                    new_c = curr_box_col * 3 + c
                    if ((new_r != row or new_c != col) and
                        board[new_r][new_c] == curr):
                        return False
            
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                if not (is_row_ok(row, col) and
                    is_col_ok(row, col) and
                    is_box_ok(row, col)):
                    return False

        return True