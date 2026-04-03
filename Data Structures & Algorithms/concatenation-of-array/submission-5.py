class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)

        for i in range(len(nums) * 2):
            copy = nums[i % len(nums)]
            res[i] = copy

        return res