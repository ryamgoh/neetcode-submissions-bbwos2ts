class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        arr = self.store[key]
        l = 0
        r = len(arr) - 1
        
        # Binary search to find the rightmost element with timestamp <= given timestamp
        result = ""
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][1] <= timestamp:
                # This could be our answer, but we need to check if there's a later one
                result = arr[m][0]  # Store the value, not the timestamp
                l = m + 1  # Try to find a later timestamp
            else:
                r = m - 1
        
        return result
        