from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we know that nums1 is sorted (biggest is at the end)
        # we know that nums2 is sorted (biggest is at the end)
        # and we need to do nums1 in-place

        # why not make use of the zeros in nums1
        # start from back and go backwards
        nums1_biggest = m - 1
        nums2_biggest = n - 1
        
        # Start from the end of nums1 (where the zeros are)
        for ptr_from_back in range(m + n - 1, -1, -1):
            # If we've exhausted nums2, we're done
            if nums2_biggest < 0:
                break
            
            # If we've exhausted nums1, just copy remaining nums2
            if nums1_biggest < 0:
                nums1[ptr_from_back] = nums2[nums2_biggest]
                nums2_biggest -= 1
            # Compare and place the larger element
            elif nums1[nums1_biggest] > nums2[nums2_biggest]:
                nums1[ptr_from_back] = nums1[nums1_biggest]
                nums1_biggest -= 1
            else:
                nums1[ptr_from_back] = nums2[nums2_biggest]
                nums2_biggest -= 1