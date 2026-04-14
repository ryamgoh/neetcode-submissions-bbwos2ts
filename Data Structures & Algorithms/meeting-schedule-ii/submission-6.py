"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        if len(intervals) == 0:
            return 0

        # print([(itv.start, itv.end) for itv in intervals])
        minEnds = []
        heapq.heappush(minEnds, intervals[0].end)

        for inv in intervals[1:]:
            start = inv.start
            end = inv.end
            smallestEnd = minEnds[0]
            if smallestEnd > start:
                heapq.heappush(minEnds, end)
            else:
                smallestEnd = heapq.heappop(minEnds)
                heapq.heappush(minEnds, end)

        return len(minEnds)