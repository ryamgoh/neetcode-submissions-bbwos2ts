class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        
        def helper(i):
            if i >= len(nums) - 1:
                return True
            if i in memo:
                return memo[i]
            
            # Try largest jumps first to reach the end faster
            max_jump = nums[i]
            # Only jump to valid indices
            furthest = min(i + max_jump, len(nums) - 1)
            
            # Try from furthest down to nearest
            for jump in range(furthest, i, -1):
                if helper(jump):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return helper(0)