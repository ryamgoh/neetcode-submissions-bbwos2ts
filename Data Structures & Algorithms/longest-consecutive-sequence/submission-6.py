class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a_set = set(nums)
        longest = 0

        for num in a_set:
            if (num - 1) not in a_set:
                length = 1
                while (num + length) in a_set:
                    length += 1
                longest = max(longest, length)

        return longest