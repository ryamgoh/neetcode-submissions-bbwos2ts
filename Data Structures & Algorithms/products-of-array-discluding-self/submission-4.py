class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize with 1 instead of 0
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and combine
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output