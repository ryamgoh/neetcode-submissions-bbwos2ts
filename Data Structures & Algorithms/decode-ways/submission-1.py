class Solution:
    def numDecodings(self, s: str) -> int:
        
        setOfWordsInTermsOfNumString = set(
            str(i) for i in range(1, 27)
        )

        def dfs(i):
            if i >= len(s):
                return 1

            count = 0
            for alphabetNum in setOfWordsInTermsOfNumString:
                if i + len(alphabetNum) <= len(s) and s[i:i+len(alphabetNum)] == alphabetNum:
                    count += dfs(i + len(alphabetNum))

            return count

        return dfs(0)