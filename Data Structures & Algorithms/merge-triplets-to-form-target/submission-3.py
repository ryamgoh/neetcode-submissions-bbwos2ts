class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # filter out all the invalid triplets, meaning any of the values in the 
        # 3 indices are greater than their corresponding index in the target
        filtered = [trip for trip in triplets if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]]

        # now check if we can find all target values in their corresponding indices
        found = [False, False, False]  # Track which target values we've found
        
        for i in range(3):
            for trip in filtered:  # Iterate through filtered triplets, not indices
                if trip[i] == target[i]:  # Check if current value matches target
                    found[i] = True
        
        return all(found)  # Return True only if all target values were found