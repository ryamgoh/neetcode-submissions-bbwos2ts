class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [10,20,20,40<-a,0,0<-b] [1,2<-c]
        # [10,20,20<-a,0,0<-b,40] [1,2<-c]
        # [10,20<-a,0,0<-b,20,40] [1,2<-c]
        # [10<-a,0,0<-b,20,20,40] [1,2<-c]
        # [0,0<-b,20,20,20,40] [1,2<-c]
        # [0<-b,2,20,20,20,40] [1<-c,2]
        # [1,2,20,20,20,40] [1,2]

        a = m - 1
        b = m + n - 1
        c = n - 1

        while b >= 0:
            if a >= 0 and c >= 0:
                # compare
                if nums1[a] > nums2[c]:
                    nums1[b] = nums1[a]
                    a -= 1
                    b -= 1
                else:
                    nums1[b] = nums2[c]
                    c -= 1
                    b -= 1
                
            elif a < 0 and c >= 0:
                nums1[b] = nums2[c]
                c -= 1
                b -= 1
            elif a >= 0 and c < 0:
                nums1[b] = nums1[a]
                a -= 1
                b -= 1