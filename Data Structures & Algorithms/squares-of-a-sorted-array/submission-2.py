class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = 0
        R = len(nums) - 1
        res = []
        while L <= R:
            if nums[L] * nums[L] > nums[R] * nums[R]:
                res.append(nums[L] * nums[L])
                L += 1
            else:
                res.append(nums[R] * nums[R])
                R -= 1
        return res[::-1]