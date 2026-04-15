class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # (val, idx)

        R = 0

        while R < len(nums):
            # pop smaller values from q
            while q and q[-1][0] < nums[R]:
                q.pop()

            # add newest guy (nums[R])
            q.append((nums[R], R))

            # remove left val from window
            if q[0][1] < R - k + 1:
                q.popleft()

            # Only append to output once we have a full window
            if R >= k - 1:
                output.append(q[0][0])

            R += 1
        
        return output