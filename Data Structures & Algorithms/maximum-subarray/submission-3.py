class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i == 0:
                return nums[i]
            if i in memo:
                return memo[i]
            
            res = max(nums[i], nums[i] + dfs(i - 1))
            memo[i] = res
            return res

        maxRes = float("-inf")
        for i in range(n):
            maxRes = max(maxRes, dfs(i))

        return int(maxRes)