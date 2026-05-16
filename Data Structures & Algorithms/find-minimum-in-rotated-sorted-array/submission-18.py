class Solution:
    def findMin(self, nums: List[int]) -> int:
        def dnc(left, right):
            if left >= right:
                return nums[left]
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            return min(dnc(left, mid), dnc(mid+1, right))
            
        return int(dnc(0, len(nums)-1))