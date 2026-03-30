class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []  # minHeap of size k
        self.k = k
        # O(1) retrieval for kth largest
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]