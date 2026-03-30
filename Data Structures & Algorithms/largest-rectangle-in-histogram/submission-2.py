class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = [] # pair: [idx, height]

        for currIndex, currHeight in enumerate(heights):
            start = currIndex
            while stack and stack[-1][1] > currHeight:
                prevIndex, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (currIndex - prevIndex))
                start = prevIndex
            stack.append((start, currHeight))


        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))

        return maxArea