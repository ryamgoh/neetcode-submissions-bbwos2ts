from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        p1 = m - 1  # Last element in nums1 (the real elements, not zeros)
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last position in nums1 array
        
        # Merge from the back
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1