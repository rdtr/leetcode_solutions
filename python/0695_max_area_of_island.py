from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mlen = len(grid)
        if mlen == 0:
            return 0
        nlen = len(grid[0])

        res = 0
        for i in range(mlen):
            for j in range(nlen):
                if grid[i][j] == 1:
                    que = deque([(i, j)])
                    area = 1
                    grid[i][j] = 0

                    while que:
                        qlen = len(que)
                        for k in range(qlen):
                            pointX, pointY = que.popleft()

                            for newPointX, newPointY in [(pointX + 1, pointY), (pointX, pointY + 1),
                                                         (pointX - 1, pointY), (pointX, pointY - 1)]:
                                if 0 <= newPointX < mlen and 0 <= newPointY < nlen and grid[newPointX][newPointY] == 1:
                                    que.append((newPointX, newPointY))
                                    grid[newPointX][newPointY] = 0
                                    area += 1
                    res = max(res, area)
        return res