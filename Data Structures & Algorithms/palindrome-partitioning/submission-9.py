class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subseq = []
        
        def isPali(s):
            L = 0
            R = len(s) - 1
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(subseq[::])
                return
            for j in range(i, len(s)):
                print(s[i:j+1])
                if isPali(s[i:j+1]):
                    subseq.append(s[i:j+1])
                    dfs(j + 1)
                    subseq.pop()

        dfs(0)
        return res
