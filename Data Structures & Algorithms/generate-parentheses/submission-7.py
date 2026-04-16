class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        sub_arr = []
        def backtrack(open, close):
            if open == n == close:
                res.append("".join(sub_arr))
                return

            if open < n:
                sub_arr.append("(")
                backtrack(open + 1, close)
                sub_arr.pop()
            if open > close:
                sub_arr.append(")")
                backtrack(open, close + 1)
                sub_arr.pop()

        backtrack(0, 0)
        return res