class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        subset = []
        def backtrack(i):
            nonlocal total
            if i >= len(nums):
                curr_sum = 0
                for x in subset:
                    curr_sum ^= x
                total += curr_sum
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return total
            