class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        first_prefix = strs[0]
        for i in range(len(first_prefix)):
            for s in strs:
                if i >= len(s) or s[i] != first_prefix[i]:
                    return res
            res += first_prefix[i]
        return res