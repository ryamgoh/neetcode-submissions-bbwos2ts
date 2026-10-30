class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # for each n
        # search in the rest if there's a duplicate
        # like say i pick idx 0, then i'll need ot check from 1 - (n - 1)
        # this gives a time compelxity of about O(n^2)

        # then whats the solution
        # we can try to save precomputed stuff as we go in a linear approach
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)

        return False
