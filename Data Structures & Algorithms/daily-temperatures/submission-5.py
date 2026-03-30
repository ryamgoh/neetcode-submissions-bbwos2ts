class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []  # store (temperature, index)
        
        for newest_index, newest_temp in enumerate(temperatures):
            # Check all temperatures in stack that are less than current temp
            while stack and stack[-1][0] < newest_temp:
                prev_temp, prev_index = stack.pop()
                output[prev_index] = newest_index - prev_index
            # Push current temperature onto stack
            stack.append((newest_temp, newest_index))
        
        return output