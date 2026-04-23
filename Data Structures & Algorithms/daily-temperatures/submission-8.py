class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = [] # store (tempature and index)
        for newest_index, newest_temp in enumerate(temperatures):
            while stack and stack[-1][0] < newest_temp:
                prev_temp, prev_index = stack.pop()
                output[prev_index] = newest_index - prev_index

            stack.append((newest_temp, newest_index))
            
        return output