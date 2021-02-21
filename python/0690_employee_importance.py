"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        m = {}
        for e in employees:
            if e not in m:
                m[e.id] = e
        
        res = 0
        if id not in m:
            return 0
        
        importance = 0
        q = deque([m[id]])
        while q:
            qlen = len(q)
            for i in range(qlen):
                e = q.popleft()
                importance += e.importance
                
                for sub in e.subordinates:
                    q.append(m[sub])
        return importance