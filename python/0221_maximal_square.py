class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mlen = len(matrix)
        if mlen == 0:
            return 0
        nlen = len(matrix[0])
        if nlen == 0:
            return 0

        res = 0
        DP = [[0 for x in range(nlen)] for y in range(mlen)]

        for m in range(0, mlen):
            for n in range(0, nlen):
                if matrix[m][n] == '1':
                    if m == 0 or n == 0:
                        DP[m][n] = 1
                    else:
                        DP[m][n] = min(DP[m - 1][n], DP[m][n - 1], DP[m - 1][n - 1]) + 1

                    res = max(res, DP[m][n])
        return res ** 2