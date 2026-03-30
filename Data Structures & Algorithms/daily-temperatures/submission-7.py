class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = [] # store (tempature and index)
        stack.append((temperatures[0], 0))
        for newest_index, newest_temp in enumerate(temperatures):
            if newest_index == 0:
                continue
            while stack and stack[-1][0] < newest_temp:
                prev_temp, prev_index = stack.pop()
                output[prev_index] = newest_index - prev_index

            stack.append((newest_temp, newest_index))
            
        return output