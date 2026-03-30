class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow, fast = 0, 0
        while fast < len(nums):
            # Process current elements
            # When we find a new unique element, place it at slow position
            if fast == 0 or nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            
            # Fast pointer always moves forward
            fast += 1
        
        print(nums)
        return slow