class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        maxCount = len(nums)
        buckets = [[] for _ in range(maxCount + 1)]  

        for key, value in counter.items():
            buckets[value].append(key)

        print(buckets)
        res: List[int] = []
        remaining = k  # Use a different variable name
        for i in range(maxCount, -1, -1):
            if remaining <= 0:
                print(res)
                return res
            if buckets[i]:
                print(remaining)
                remaining -= len(buckets[i])  # Changed: use 'remaining' instead of 'k'
                res.extend(buckets[i])