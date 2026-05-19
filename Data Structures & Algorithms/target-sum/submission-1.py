class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        curr_count = 0
        n = len(nums)

        def backtrack(i: int) -> None:
            nonlocal total, curr_count
            # Base case: used all numbers
            if i >= n:
                if curr_count == target:
                    total += 1
                return

            temp = curr_count
            # Option 1: add nums[i]
            curr_count = temp + nums[i]
            backtrack(i + 1)

            # Option 2: subtract nums[i]
            curr_count = temp - nums[i]
            backtrack(i + 1)
            # curr_count += nums[i]   # undo

        backtrack(0)
        return total