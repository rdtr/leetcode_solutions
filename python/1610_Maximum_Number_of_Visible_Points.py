from math import atan2, pi

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        if len(points) == 1:
            return 1
        
        lx, ly = location
        angles = []
        me = 0
        
        for px, py in points:
            if px == lx and py == ly:
                me += 1
            else:
                angles.append(atan2(py - ly, px - lx))

        angles.sort()
        angles.extend([x + (2.0 * pi) for x in angles])
        
        l, r = 0, 0
        res = 0
        angle = (2 * pi * angle) / 360.0
        while l < len(angles) and r < len(angles):
            while r < len(angles) and angles[r] - angles[l] <= angle:
                res = max(res, r - l + 1)
                r += 1
            l += 1
        
        return res + me