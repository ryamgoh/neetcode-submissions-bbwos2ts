class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # length of the longest common prefix is as long as the shortest word
        # we will need a pointer for each word (advancing all until we don't)
        # res = longest common prefix
        # O(n * m) where n is the number of strings, and m is the shortest string
        
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res