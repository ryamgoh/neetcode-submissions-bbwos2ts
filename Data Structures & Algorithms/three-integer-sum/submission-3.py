class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) - 2):
            curr = nums[i]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if nums[L] + nums[R] + curr == 0:
                    res.add((curr, nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif nums[L] + nums[R] + curr > 0:
                    R -= 1
                else:
                    L += 1

        return [list(tup) for tup in res]