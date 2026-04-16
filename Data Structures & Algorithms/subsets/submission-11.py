class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        partial = []
        def backtrack(i):
            if i >= len(nums):
                res.append(partial[::])
                return

            partial.append(nums[i])
            backtrack(i + 1)
            partial.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
