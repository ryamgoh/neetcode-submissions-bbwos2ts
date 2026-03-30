class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1

        curr_ptr = 0
        for i in range(len(nums)):
            # Skip colors that have been fully placed
            while bucket[curr_ptr] == 0 and curr_ptr < 2:
                curr_ptr += 1
            nums[i] = curr_ptr
            bucket[curr_ptr] -= 1