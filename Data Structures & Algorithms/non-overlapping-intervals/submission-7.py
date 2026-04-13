class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # intuition: get as many intervals in the schedule

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
                # more chance of getting overlaps
                prevEnd = min(prevEnd, end)

        return res
