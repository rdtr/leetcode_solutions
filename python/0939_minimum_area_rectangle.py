class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        m = {(point[0], point[1]): True for point in points}

        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                if (p1[0] != p2[0] and p1[1] != p2[1]) and (p1[0], p2[1]) in m and (p2[0], p1[1]) in m:
                    cur = abs(p2[0] - p1[0]) * abs(p2[1] - p1[1])
                    res = min(cur, res) if res > 0 else cur
        return res
