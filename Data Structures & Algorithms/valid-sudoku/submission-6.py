class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        ROWS = len(board)
        COLS = len(board[0])
        
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                num = board[r][c]
                if num == ".":
                    continue
                if (num in row_set[r] or 
                    num in col_set[c] or 
                    num in box_set[(r // 3, c // 3)]):
                    return False

                row_set[r].add(num)
                col_set[c].add(num)
                box_set[(r // 3, c // 3)].add(num)


        return True

