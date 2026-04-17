class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        stack = [0]
        
        while stack:
            i = stack.pop()
            
            if i == len(nums) - 1:
                return True
            
            if i in memo:
                continue
                
            end = min(len(nums) - 1, i + nums[i])
            # Push positions in reverse order to simulate DFS order
            for j in range(end, i, -1):
                if j not in memo:
                    stack.append(j)
            
            memo[i] = False  # Mark as visited
        
        return False