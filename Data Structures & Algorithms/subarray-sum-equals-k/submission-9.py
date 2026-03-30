class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0

        # dictionary prefix_sum -> frequency
        # prefix_sum = {0: 1} # initialize empty prefix sum
        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1
        for num in nums:
            # increment sum
            current_sum += num
            # check (current_sum - k) exist in our dictionary, we have
            # already precomputed this before this index (i - 1) assume no i = 0
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]

            # add the current prefix sum to our dictionary
            prefix_sum[current_sum] += 1

        return count