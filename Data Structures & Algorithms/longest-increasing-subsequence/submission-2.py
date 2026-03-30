class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            max_len = 1  # At least the current element itself
            
            # Try all possible next elements
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:  # Can form increasing sequence
                    max_len = max(max_len, 1 + dfs(j))
            
            memo[i] = max_len
            return max_len
        
        # Try starting from each position
        result = 0
        for i in range(len(nums)):
            result = max(result, dfs(i))
            
        return result