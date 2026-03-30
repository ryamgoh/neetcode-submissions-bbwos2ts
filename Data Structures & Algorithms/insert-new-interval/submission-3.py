class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # this happens when our new interval is SURELY to the LEFT
            # outside the range [[1, 2], [3, 4]] <- [1, 2]
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # this happens when our new interval is SURELY to the RIGHT
            # outside the range
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
            
        res.append(newInterval)

        return res