class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        window_sum = 0
        L = 0
        max_sum = float("-inf")
        for R in range(len(nums)):
            window_sum += nums[R]
            max_sum = max(max_sum, window_sum)
            while window_sum < 0:
                window_sum -= nums[L]
                L += 1
            R += 1
        return int(max_sum)