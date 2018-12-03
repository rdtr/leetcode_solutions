class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 0:
            return 0

        height = [0] + height + [0]
        mins = [0] * len(height)

        cur = height[0]
        for i in range(1, len(height)):
            cur = max(cur, height[i - 1])
            mins[i] = cur

        cur = height[-1]
        for i in range(len(height) - 2, 0, -1):
            cur = max(cur, height[i + 1])
            mins[i] = min(mins[i], cur)

        res = 0
        for i in range(1, len(height) - 1):
            res += max(mins[i] - height[i], 0)
        return res
