class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []

        subseq = []
        def dfs(i):
            if i >= len(s):
                res.append(subseq[::])
                return
            
            for word in wordSet:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    subseq.append(word)
                    dfs(i + len(word))
                    subseq.pop()

        dfs(0)
        formated_res = [" ".join(str_ls) for str_ls in res]
        return formated_res