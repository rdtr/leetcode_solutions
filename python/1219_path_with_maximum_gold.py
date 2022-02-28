from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rowNum = len(grid)
        if rowNum == 0:
            return -1
        colNum = len(grid[0])

        que = deque([(0, 0, k)])
        seen = set((0, 0, k))
        stepNum = 0

        while que:
            qlen = len(que)
            for i in range(qlen):
                x, y, num = que.popleft()
                if x == rowNum - 1 and y == colNum - 1:
                    return stepNum

                for nextX, nextY in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    nextNum = num
                    if nextX < 0 or nextX >= rowNum or nextY < 0 or nextY >= colNum:
                        continue
                    if grid[nextX][nextY] == 1:
                        nextNum -= 1
                    if nextNum >= 0 and (nextX, nextY, nextNum) not in seen:
                        seen.add((nextX, nextY, nextNum))
                        que.append((nextX, nextY, nextNum))
            stepNum += 1
        return -1