class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mlen = len(grid)
        if mlen == 0:
            return 0
        nlen = len(grid[0])
        if nlen == 0:
            return 0

        DP = [[0 for x in range(nlen)] for y in range(mlen)]
        DP[0][0] = grid[0][0]
        for i in range(1, nlen):
            DP[0][i] = DP[0][i - 1] + grid[0][i]
        for i in range(1, mlen):
            DP[i][0] = DP[i - 1][0] + grid[i][0]

        for i in range(1, mlen):
            for j in range(1, nlen):
                DP[i][j] = min(DP[i][j - 1], DP[i - 1][j]) + grid[i][j]
        return DP[-1][-1]
