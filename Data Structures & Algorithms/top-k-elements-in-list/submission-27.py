class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create separate empty lists for each bucket
        bucketsFrequency = [[] for _ in range(len(nums) + 1)]
        
        # Count frequencies
        numToFrequency = {}
        for n in nums:
            numToFrequency[n] = numToFrequency.get(n, 0) + 1
        
        # Place numbers into frequency buckets
        for n, f in numToFrequency.items():
            bucketsFrequency[f].append(n)
        
        # Collect top k frequent elements
        res = []
        for i in range(len(nums), -1, -1):  # Start from highest frequency
            for num in bucketsFrequency[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res