class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        curr_count = 0

        def backtrack(i: int) -> None:
            nonlocal total, curr_count
            # Base case: used all numbers
            if i >= len(nums):
                if curr_count == target:
                    total += 1
                return

            # Option 1: add nums[i]
            curr_count += nums[i]
            backtrack(i + 1)
            curr_count -= nums[i]

            # Option 2: subtract nums[i]
            curr_count -= nums[i]
            backtrack(i + 1)
            curr_count += nums[i]

        backtrack(0)
        return total