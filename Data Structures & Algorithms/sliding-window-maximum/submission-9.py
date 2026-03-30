from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # (val, idx)
        
        # First pass: handle the first window (indices 0 to k-1)
        for i in range(k):
            # pop smaller values from q
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        
        # First window's maximum
        output.append(q[0][0])
        
        # Second pass: slide the window from k to end
        for i in range(k, len(nums)):
            # pop smaller values from q
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
            
            # remove left val from window if it's out of range
            if q[0][1] < i - k + 1:
                q.popleft()
            
            # current window's maximum
            output.append(q[0][0])
        
        return output