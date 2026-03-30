class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo_max = {}
        memo_min = {}

        def dp_max(i):
            """
            Returns max product subarray ending at i
            """
            if i == 0:
                return nums[0]
            if i in memo_max:
                return memo_max[i]
            
            res = max(nums[i], 
                    nums[i] * dp_max(i - 1), 
                    nums[i] * dp_min(i - 1))
            
            memo_max[i] = res
            return res

        def dp_min(i):
            """
            Returns the min product subarray ending at i
            """
            if i == 0:
                return nums[0]
            if i in memo_min:
                return memo_min[i]
            
            res = min(nums[i], 
                    nums[i] * dp_max(i - 1), 
                    nums[i] * dp_min(i - 1))
            
            memo_min[i] = res
            return res

        # find maximum over all ending posiitons
        max_product = float("-inf")
        for i in range(n):
            max_product = max(max_product, dp_max(i))

        return int(max_product)