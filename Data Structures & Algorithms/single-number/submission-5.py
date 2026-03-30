class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # a ^ a ^ b = a ^ b ^ a = b (commutative + associative XOR property)
            res ^= num
        return res

        # This is a O(n) time and O(1) space