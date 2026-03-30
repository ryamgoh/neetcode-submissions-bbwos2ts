class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        L = 0
        R = len(nums) - 1

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            M = L + (R - L) // 2
            res = min(res, nums[M])
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1

        return res