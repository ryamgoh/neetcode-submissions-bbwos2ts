class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we want a solution that supports some sort of monotonically decreasing property

        # 1 2 1 
        # 2 1 0
        # 1 0 0

        # (val, idx)
        window = deque()
        res = []

        L = 0
        for R in range(len(nums)):
            while window and window[-1][0] < nums[R]:
                window.pop()

            window.append((nums[R], R))

            while R - window[0][1] + 1 > k:
                window.popleft()

            # only append to output once we have full window
            if R >= k - 1:
                res.append(window[0][0])
            
        return res
