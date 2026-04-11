class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        subArr = []

        def backtrack(open, close):
            if open == n == close:
                res.append("".join(subArr[::]))
                return

                        # Try adding an opening bracket if we haven't used all
            if open < n:
                subArr.append("(")
                backtrack(open + 1, close)
                subArr.pop()
            
            # Try adding a closing bracket if it won't make it invalid
            if close < open:
                subArr.append(")")
                backtrack(open, close + 1)
                subArr.pop()

        backtrack(0, 0)

        return res