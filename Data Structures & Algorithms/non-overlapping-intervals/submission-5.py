class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        merged_intervals = [sorted_intervals[0].copy()]  # Start with first interval
        
        for start, end in sorted_intervals[1:]:  # Start from second interval
            last_start, last_end = merged_intervals[-1]
            
            if start < last_end:  # Overlap detected
                # Merge by updating the end to the minimum (greedy choice to remove fewer)
                merged_intervals[-1][1] = min(last_end, end)
            else:
                # No overlap, add as new interval
                merged_intervals.append([start, end])
        
        return len(intervals) - len(merged_intervals)