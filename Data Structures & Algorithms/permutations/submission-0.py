class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # unique integers
        # 0   1 2 3 
        # 1   12 13 21 23 31 32
        # 2   123 132 213 231 312 321

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res