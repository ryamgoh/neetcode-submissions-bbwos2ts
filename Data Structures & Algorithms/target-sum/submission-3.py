class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i: int, curr_sum: int) -> int:
            # Base case: used all numbers
            if i >= len(nums):
                if curr_sum == target:
                    return 1
                return 0

            return dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])
            
        return dfs(0, 0)
