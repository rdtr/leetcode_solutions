class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)

        res, stack = 0, []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                cur = stack.pop()
                height = heights[cur]
                if stack:
                    width = i - 1 - stack[-1]
                else:
                    width = i
                res = max(res, height * width)
            stack.append(i)
        return res