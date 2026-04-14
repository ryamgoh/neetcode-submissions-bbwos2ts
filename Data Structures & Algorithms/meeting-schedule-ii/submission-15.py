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

        # print([(itv.start, itv.end) for itv in intervals])
        minEnds = []

        for inv in intervals:
            if minEnds and minEnds[0] <= inv.start:
                heapq.heappop(minEnds)
            heapq.heappush(minEnds, inv.end)
        return len(minEnds)