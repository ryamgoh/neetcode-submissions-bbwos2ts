from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0] * len(nums)
        path = []
        def backtrack():
            # Base case: we have a full permutation
            if len(path) == len(nums):
                res.append(path[:])   # must copy!
                return

            # Try every unused number
            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose
                used[i] = 1
                path.append(nums[i])

                # Explore
                backtrack()

                # Un-choose (backtrack)
                used[i] = 0
                path.pop()

        backtrack()
        return res