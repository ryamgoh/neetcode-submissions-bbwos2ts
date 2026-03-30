class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curSum = 0, 0

        prefixSums = defaultdict(int)

        prefixSums[0] = 1

        for num in nums:
            curSum += num
            diff = curSum - k

            if prefixSums[diff]:
                res += prefixSums[diff]
            prefixSums[curSum] = prefixSums[curSum] + 1

        return res