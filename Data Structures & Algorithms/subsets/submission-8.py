class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        
        res = []

        def dfs(i, seq: List[int]):
            if i >= len(nums):
                res.append(seq)
                return
            dfs(i + 1, seq + [nums[i]])
            dfs(i + 1, seq)

        dfs(0, [])

        return res