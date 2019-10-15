class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(-1)

        res = 0
        stack = []
        for i in range(len(heights)):
            if i > 0 and heights[i] < heights[i - 1]:
                while stack and stack[-1][1] > heights[i]:
                    prevIndex, prevHeight = stack.pop()
                    res = max(res, (i - 1 - (stack[-1][0] + 1) + 1) * prevHeight) if stack else max(res, i * prevHeight)
            stack.append((i, heights[i]))
        return res