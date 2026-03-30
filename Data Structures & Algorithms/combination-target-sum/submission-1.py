class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subarr = []

        def backtrack(i, sum):
            if i >= len(nums):
                return
            if sum > target:
                return
            elif sum == target:
                res.append(subarr[::])
                return
            subarr.append(nums[i])
            backtrack(i, sum + nums[i])
            subarr.pop()
            backtrack(i + 1, sum)

        backtrack(0, 0)

        return res