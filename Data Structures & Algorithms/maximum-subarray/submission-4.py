class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i == 0:
                return nums[i]
            if i in memo:
                return memo[i]
            
            # at position i,
            # should I start fresh, or continue my MAX
            # either start a new subarray at i or extend previous subarray
            res = max(nums[i], nums[i] + dfs(i - 1))
            memo[i] = res
            return res

        maxRes = float("-inf")
        for i in range(n):
            maxRes = max(maxRes, dfs(i))

        return int(maxRes)