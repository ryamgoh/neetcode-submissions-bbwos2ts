class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def backtrack(l):
            if l == len(s):
                res.append(path[::])
                return
            
            for r in range(l+1, len(s)+1):
                if self.isPalindrome(s[l:r]):
                    path.append(s[l:r])
                    backtrack(r)
                    path.pop()

        backtrack(0)
        return res


    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True