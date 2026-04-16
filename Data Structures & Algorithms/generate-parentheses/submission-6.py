class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []
        def backtrack(open, close):
            if open == n == close:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            if open > close:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res