class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        memo = {}  # Key: (index, prev_value) tuple
        
        def dfs(i, prev_val):
            # Base case: reached end of array
            if i >= len(nums):
                return 0
                
            # Check memo
            if (i, prev_val) in memo:
                return memo[(i, prev_val)]
            
            # Option 1: Skip current element
            skip = dfs(i + 1, prev_val)
            
            # Option 2: Take current element (if it's greater than previous)
            take = 0
            if nums[i] > prev_val:
                take = 1 + dfs(i + 1, nums[i])
            
            # Store and return the maximum of both options
            memo[(i, prev_val)] = max(skip, take)
            return memo[(i, prev_val)]
        
        # Start with index 0 and prev_val = -infinity
        return dfs(0, float('-inf'))