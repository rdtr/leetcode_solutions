class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = b = 0
        res = []
        while a < len(A) or b < len(B):
            if a < len(A) and b < len(B):
                if B[b][1] < A[a][0]:
                    b += 1
                    continue
                if A[a][1] < B[b][0]:
                    a += 1
                    continue

                if A[a][0] <= B[b][0]:
                    if B[b][1] <= A[a][1]:
                        res.append([B[b][0], B[b][1]])
                        b += 1
                    else:
                        res.append([B[b][0], A[a][1]])
                        a += 1
                else:
                    if B[b][1] <= A[a][1]:
                        res.append([A[a][0], B[b][1]])
                        b += 1
                    else:
                        res.append([A[a][0], A[a][1]])
                        a += 1
                continue
            break

        return res