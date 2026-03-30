class Solution:
    def numDecodings(self, s: str) -> int:
        
        setOfWordsInTermsOfNumString = set(
            str(i) for i in range(1, 27)
        )

        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]

            count = 0
            for alphabetNum in setOfWordsInTermsOfNumString:
                if i + len(alphabetNum) <= len(s) and s[i:i+len(alphabetNum)] == alphabetNum:
                    count += dfs(i + len(alphabetNum))

            memo[i] = count
            return memo[i]

        return dfs(0)