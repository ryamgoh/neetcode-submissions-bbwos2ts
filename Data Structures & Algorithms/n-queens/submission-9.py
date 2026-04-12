class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # a queen attack:
        # Vertical
        # Horizontal
        # Positive diag or Negative diag
        resBoard = []
        subBoard = []

        col = set()
        pos_diag = set()
        neg_diag = set()
        def backtrack(r):
            if r == n:
                resBoard.append(subBoard[::])
                return
            
            for c in range(n):
                if c in col or (c + r) in pos_diag or (c - r) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(c + r)
                neg_diag.add(c - r)
                row = ["." if i != c else "Q" for i in range(n)]
                subBoard.append("".join(row))
                backtrack(r + 1)
                subBoard.pop()
                col.remove(c)
                pos_diag.remove(c + r)
                neg_diag.remove(c - r)                

        backtrack(0)  # backtrack on row 0 first
        return resBoard