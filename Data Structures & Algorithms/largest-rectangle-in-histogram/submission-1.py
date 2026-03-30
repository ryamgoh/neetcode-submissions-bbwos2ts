class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = [] # pair: [height, idx]

        for currIndex, currHeight in enumerate(heights):
            start = currIndex
            while stack and stack[-1][0] > currHeight:
                prevHeight, prevIndex = stack.pop()
                maxArea = max(maxArea, prevHeight * (currIndex - prevIndex))
                start = prevIndex
            stack.append((currHeight, start))


        for height, idx in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))

        return maxArea