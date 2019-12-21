from collections import defaultdict

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        row = len(A)
        if row == 0:
            return 0
        col = len(A[0])
        if col == 0:
            return 0
        
        aset, bset = set(), set()
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    aset.add((i, j))
                if B[i][j] == 1:
                    bset.add((i, j))
                
        resMap = defaultdict(lambda: 0)
        for a0, a1 in aset:
            for b0, b1 in bset:
                m0, m1 = b0 - a0, b1 - a1
                resMap[(m0, m1)] += 1
        
        res = 0
        for k, v in resMap.items():
            res = max(res, v)
        return res