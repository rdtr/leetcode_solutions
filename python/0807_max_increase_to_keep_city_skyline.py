class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        mlen = len(grid)
        if mlen == 0:
            return 0
        nlen = len(grid[0])
        if nlen == 0:
            return 0

        mmax, nmax = [0] * mlen, [0] * mlen
        for m in range(mlen):
            for n in range(nlen):
                mmax[m] = max(mmax[m], grid[m][n])
                nmax[n] = max(nmax[n], grid[m][n])

        res = 0
        for m in range(mlen):
            for n in range(nlen):
                res += (min(mmax[m], nmax[n]) - grid[m][n])
        return res