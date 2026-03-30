from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_row_ok(board: List[List[str]], row: int, col: int) -> bool:
            # Check if current cell's value is valid in its row
            curr = board[row][col]
            if curr == '.':
                return True
            for c in range(9):
                if c != col and board[row][c] == curr:
                    return False
            return True

        def is_col_ok(board: List[List[str]], row: int, col: int) -> bool:
            # Check if current cell's value is valid in its column
            curr = board[row][col]
            if curr == '.':
                return True
            for r in range(9):
                if r != row and board[r][col] == curr:
                    return False
            return True

        def is_box_ok(board: List[List[str]], row: int, col: int) -> bool:
            # Check if current cell's value is valid in its 3x3 box
            curr = board[row][col]
            if curr == '.':
                return True
            
            # Find the top-left corner of the 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    if (r != row or c != col) and board[r][c] == curr:
                        return False
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if not (is_row_ok(board, row, col) and
                          is_col_ok(board, row, col) and
                          is_box_ok(board, row, col)):
                        return False
        return True