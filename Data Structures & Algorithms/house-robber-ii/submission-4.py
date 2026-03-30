class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr1 = nums[1:]
        arr2 = nums[:-1]
        memo1 = {}
        memo2 = {}

        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 1, arr, memo), arr[i] + dfs(i + 2, arr, memo))
            return memo[i]

        return max(dfs(0, arr1, memo1), dfs(0, arr2, memo2))