class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        A sliding window is a natural choice because we're trying to find
        the LONGEST continuous subarray

        The CHALLENGE is how can we efficiently track the current min and max in the window
        as it moves

        DS:
        1. an efficient datastructure that can efficiently track the minimum values and supports left and right appending at O(1)
        1a. we also want to store the index
        2. elements in the window MUST be within the bounds of the left pointer
        
        Other notes:
        1. constantly move the right pointer
        2. only shrink the left pointer when invariant of max - min <= limit is violated
        """

        min_q = deque()  # monotonically increasing queue + (val, idx)
        max_q = deque()  # monotonically decreasing queue
        L = 0
        res = 0
        for R in range(len(nums)):
            while min_q and nums[R] < min_q[-1][0]:
                min_q.pop()
            while max_q and nums[R] > max_q[-1][0]:
                max_q.pop()

            min_q.append((nums[R], R))
            max_q.append((nums[R], R))

            while max_q[0][0] - min_q[0][0] > limit:
                L += 1
                if max_q[0][1] < L:
                    max_q.popleft()
                if min_q[0][1] < L:
                    min_q.popleft()

            res = max(res, R - L + 1)


        return res