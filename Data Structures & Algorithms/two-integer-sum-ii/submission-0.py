class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 2 3 3 4
        l = 0
        r = len(numbers) - 1

        while l <= r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum == target:
                return [l + 1, r + 1] # 1-index
            elif cur_sum > target:
                # lower the cur_sum, which means we should lower the right pointer
                # which is already pointing to a high number
                r -= 1
            else:
                # increase the cur_sum, meaning increment left pointer
                l += 1
