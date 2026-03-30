class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        
        while L <= R:
            M = L + (R - L) // 2
            
            if nums[M] == target:
                return M
            
            # Left half is sorted
            if nums[L] <= nums[M]:
                # Target is in left sorted half
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            # Right half is sorted
            else:
                # Target is in right sorted half
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        
        return -1