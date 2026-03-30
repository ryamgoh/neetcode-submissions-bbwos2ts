class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        max_stones = [-x for x in stones]
        heapq.heapify(max_stones)
        print(max_stones)
        while len(max_stones) >= 2:
            heaviest = -heapq.heappop(max_stones)
            second_heaviest = -heapq.heappop(max_stones)
            if heaviest == second_heaviest:
                continue
            heapq.heappush(max_stones, -(heaviest - second_heaviest))
        
        return -max_stones[0] if max_stones else 0