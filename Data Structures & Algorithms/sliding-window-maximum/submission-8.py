class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # (val, idx)

        i = 0

        while i < len(nums):
            # pop smaller values from q
            while q and q[-1][0] < nums[i]:
                q.pop()

            # add newest guy (nums[i])
            q.append((nums[i], i))

            # remove left val from window
            if q[0][1] < i - k + 1:
                q.popleft()

            # Only append to output once we have a full window
            if i >= k - 1:
                output.append(q[0][0])

            i += 1
        
        return output