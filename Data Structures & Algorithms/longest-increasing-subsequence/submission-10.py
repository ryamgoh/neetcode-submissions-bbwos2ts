class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LENGTH = len(nums)

        memo = {}
        def dfs(i):
            if i >= LENGTH:
                return 0
            if i in memo:
                return memo[i]
            
            LIS = 1

            for j in range(i + 1, LENGTH):
                if nums[i] < nums[j]:
                    # print("Before ", LIS)
                    LIS = max(LIS, 1 + dfs(j))
                    # print("After ", LIS)

            memo[i] = LIS
            return memo[i]


        return max(dfs(i) for i in range(LENGTH))