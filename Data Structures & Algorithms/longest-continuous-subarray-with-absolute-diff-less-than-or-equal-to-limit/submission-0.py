class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxHeap = []
        minHeap = []
        L = 0
        res = 0

        for R, val in enumerate(nums):
            heapq.heappush(maxHeap, (-val, R))
            heapq.heappush(minHeap, (val, R))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                L += 1
                while maxHeap and maxHeap[0][1] < L:
                    heapq.heappop(maxHeap)
                while minHeap and minHeap[0][1] < L:
                    heapq.heappop(minHeap)

            res = max(res, R - L + 1)

        return res