class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for t in triplets:
            # Observation: 
            # For target[0], we need at least one triplet where:
            # 1. The first value == target[0]
            # 2. The other two values do not exceed the target
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])

            # Do this for the next two target[1] and target[2]
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
        if x and y and z:
            return True
        return False