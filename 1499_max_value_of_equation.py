from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = float('-inf')
        queue = deque([])
        
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            
            if queue:
                res = max(res, queue[-1][0] + x + y)
            
            while queue and queue[-1][0] < y - x:
                queue.pop()
            
            queue.append((y - x, x))
        
        return res
                    