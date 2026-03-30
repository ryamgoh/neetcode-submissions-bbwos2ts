class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals are always a pair
        # new intervals are also a pair

        # if new interval overlaps with other intervals, merge them.
        
        n = len(intervals)
        i = 0
        res = []

        # we want to add all the intervals before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        new_start = newInterval[0]
        new_end = newInterval[1]

        # while there's overlap, merge
        # i.e. start to merge all the intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            # new start = min of the starts
            new_start = min(new_start, intervals[i][0])
            # new end = max of the ends
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start, new_end])

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
