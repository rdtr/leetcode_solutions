class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        mlen = len(matrix)
        if mlen == 0:
            return 0
        nlen = len(matrix[0])
        if nlen == 0:
            return 0

        dp = [[0] * nlen for x in range(mlen)]

        res = 0
        for i in range(nlen):
            dp[0][i] = 0 if matrix[0][i] == '0' else 1
            if dp[0][i] == 1:
                res = 1
        for i in range(mlen):
            dp[i][0] = 0 if matrix[i][0] == '0' else 1
            if dp[i][0] == 1:
                res = 1

        for m in range(1, mlen):
            for n in range(1, nlen):
                if matrix[m][n] == '0':
                    continue
                dp[m][n] = min(dp[m - 1][n - 1], dp[m][n - 1],
                               dp[m - 1][n]) + 1
                if res < dp[m][n]:
                    res = dp[m][n]
        return res * res