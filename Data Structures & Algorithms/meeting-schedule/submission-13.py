"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # sort meetings first by start
        sorted_meetings = sorted(intervals, key=lambda x: x.start)

        for i in range(len(sorted_meetings) - 1):
            if sorted_meetings[i].end > sorted_meetings[i + 1].start:
                return False
            
        return True