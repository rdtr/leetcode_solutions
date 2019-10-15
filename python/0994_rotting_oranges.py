from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        mlen = len(grid)
        if mlen == 0:
            return -1
        nlen = len(grid[0])
        if nlen == 0:
            return -1

        q = deque([])
        fresh = 0
        for i in range(mlen):
            for j in range(nlen):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        mins = 0
        cache = {}
        while True:
            qlen = len(q)
            for i in range(qlen):
                rotten = q.popleft()
                x, y = rotten[0], rotten[1]

                if x > 0 and grid[x - 1][y] == 1:
                    if (x - 1, y) not in cache:
                        cache[(x - 1, y)] = mins
                        q.append((x - 1, y))
                        fresh -= 1
                if x < mlen - 1 and grid[x + 1][y] == 1:
                    if (x + 1, y) not in cache:
                        cache[(x + 1, y)] = mins
                        q.append((x + 1, y))
                        fresh -= 1
                if y > 0 and grid[x][y - 1] == 1:
                    if (x, y - 1) not in cache:
                        cache[(x, y - 1)] = mins
                        q.append((x, y - 1))
                        fresh -= 1
                if y < nlen - 1 and grid[x][y + 1] == 1:
                    if (x, y + 1) not in cache:
                        cache[(x, y + 1)] = mins
                        q.append((x, y + 1))
                        fresh -= 1
            if not q:
                break
            mins += 1
        return mins if fresh == 0 else -1