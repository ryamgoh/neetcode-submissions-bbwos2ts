class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        self.val = 0
        
        res = []
        sub_arr = []
        def backtrack(i):
            if i >= len(nums):
                return
            if self.val > target:
                return
            if target == self.val:
                res.append(sub_arr[::])
                return
            
            self.val += nums[i]
            sub_arr.append(nums[i])
            backtrack(i)
            self.val -= nums[i]
            sub_arr.pop()
            backtrack(i + 1)

        backtrack(0)

        return res
                
            