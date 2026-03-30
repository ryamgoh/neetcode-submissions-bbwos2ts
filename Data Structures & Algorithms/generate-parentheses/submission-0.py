class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def isValid(s):
            # it is valid if the order makes sense
            open = 0
            for c in s:
                open += 1 if c == "(" else -1
                if open < 0:
                    return False
            return not open


        def dfs(s: str):
            # we stop when we get to the 2n length
            if n * 2 == len(s):
                if isValid(s):
                    res.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")

        dfs("")

        return res