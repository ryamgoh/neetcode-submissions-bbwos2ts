class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup_set = set()

        for num in nums:
            if num in dup_set:
                return num
            dup_set.add(num)