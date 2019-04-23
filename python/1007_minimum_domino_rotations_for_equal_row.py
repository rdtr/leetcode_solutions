class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        alen, blen = len(A), len(B)
        if alen != blen or alen == 0:
            return -1

        a, b = A[0], B[0]
        cur = [0] * 4
        for i in range(alen):
            if cur[0] >= 0 and A[i] != a: # case1: all elements of A will have A[0]
                if B[i] == a: cur[0] += 1
                else: cur[0] = -1
            if cur[1] >= 0 and A[i] != b: # case2: all elements of A will have B[0]
                if B[i] == b: cur[1] += 1
                else: cur[1] = -1
            if cur[2] >= 0 and B[i] != a: # case3: all elements of B will have A[0]
                if A[i] == a: cur[2] += 1
                else: cur[2] = -1
            if cur[3] >= 0 and B[i] != b: # case4: all elements of B will have B[0]
                if A[i] == b: cur[3] += 1
                else: cur[3] = -1
        res = -1
        for c in cur:
            if res == -1 and c != -1: res = c
            elif c >= 0 and c < res: res = c
        return res



