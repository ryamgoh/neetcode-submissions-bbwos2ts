class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        longest = 0
        for num in hashSet:
            if (num - 1) not in hashSet:
                # we can start from this
                count = 1
                curr = num
                while (curr + 1) in hashSet:
                    count += 1
                    curr += 1
                longest = max(longest, count)

        return longest