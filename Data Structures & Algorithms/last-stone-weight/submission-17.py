class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # at every step we get to pick 2 of the heaviest stone
        # we should be able to get them really easily
        # n * O(1) times
        # O(n)

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap)
            second_heaviest = -heapq.heappop(maxHeap)
            diff = heaviest - second_heaviest
            if diff != 0:
                heapq.heappush(maxHeap, -diff)

        return -maxHeap[0] if maxHeap else 0
