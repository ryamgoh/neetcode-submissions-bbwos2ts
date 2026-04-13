class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        L, R = 0, len(A) - 1

        while True:
            MID_A = (L + R) // 2
            PTR_B = half - (MID_A + 1) - 1  # indexed 0

            A_left = A[MID_A] if MID_A >= 0 else float("-inf")
            A_right = A[MID_A + 1] if (MID_A + 1) < len(A) else float("inf")
            B_left = B[PTR_B] if PTR_B >= 0 else float("-inf")
            B_right = B[PTR_B + 1] if (PTR_B + 1) < len(B) else float("inf")

            # partition if correct
            if A_left <= B_right and B_left <= A_right:
                # odd
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left)) / 2
            elif A_left > B_right:
                R = MID_A - 1
            else:
                L = MID_A + 1