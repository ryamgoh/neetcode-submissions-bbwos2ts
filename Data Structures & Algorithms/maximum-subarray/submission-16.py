class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0
        left = 0
        
        for right in range(len(nums)):
            # Add current element to window
            curSum += nums[right]
            
            # If current sum becomes negative, reset window
            while curSum <= 0 and left <= right:
                curSum -= nums[left]
                left += 1
                
                # If window becomes empty, we need to start fresh
                if left > right:
                    # Start new window at next position
                    left = right + 1
                    curSum = 0
                    break
            
            # Update maxSum (handle case when window becomes empty)
            if left <= right:
                maxSum = max(maxSum, curSum)
            else:
                # If all numbers are negative, we need to track the max single element
                maxSum = max(maxSum, nums[right] if right < len(nums) else float("-inf"))
        
        return maxSum