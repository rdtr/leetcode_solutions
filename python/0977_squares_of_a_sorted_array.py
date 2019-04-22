class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return []

        neg = pos = 0
        while pos < len(A):
            if A[pos] < 0:
                pos += 1
                continue
            neg = pos - 1
            break

        res = []
        while neg >= 0 or pos < len(A):
            if neg < 0:
                res.append(A[pos] ** 2)
                pos += 1
                continue
            if pos >= len(A):
                res.append(A[neg] ** 2)
                neg -= 1
                continue

            if A[pos] >= -A[neg]:
                res.append(A[neg] ** 2)
                neg -= 1
            else:
                res.append(A[pos] ** 2)
                pos += 1
        return res