class Solution:
    def numDistinctIslands(self, grid):
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

        s = set()
        for m in range(mlen):
            for n in range(nlen):
                if grid[m][n] == 1:
                    path = []
                    self.doNumDistinctIslands(grid, m, n, mlen, nlen, path)
                    s.add(''.join(path))
        return len(s)

    def doNumDistinctIslands(self, grid, m, n, mlen, nlen, path):
        grid[m][n] = 0
        if m > 0 and grid[m - 1][n] == 1:
            path.append('^')
            self.doNumDistinctIslands(grid, m - 1, n, mlen, nlen, path)
        if m < mlen - 1 and grid[m + 1][n] == 1:
            path.append('v')
            self.doNumDistinctIslands(grid, m + 1, n, mlen, nlen, path)
        if n > 0 and grid[m][n - 1] == 1:
            path.append('<')
            self.doNumDistinctIslands(grid, m, n - 1, mlen, nlen, path)
        if n < nlen - 1 and grid[m][n + 1] == 1:
            path.append('>')
            self.doNumDistinctIslands(grid, m, n + 1, mlen, nlen, path)
        path.append('|')