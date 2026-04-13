class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # if no overlap, then update prevEnd = end
                prevEnd = end
            else:
                # start < prevEnd
                # overlap found, remove one interval
                res += 1
                # keep the interval with the smaller end
                prevEnd = min(prevEnd, end)

        return res
