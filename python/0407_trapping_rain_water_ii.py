from heapq import heappush, heappop, heapify


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        mlen = len(heightMap)
        if mlen == 0:
            return 0
        nlen = len(heightMap[0])
        if nlen == 0:
            return 0

        HEAP = []
        visited = [[False for _ in range(nlen)] for _ in range(mlen)]
        for i, height in enumerate(heightMap[0]):
            HEAP.append(Tile(0, i, height))
            visited[0][i] = True
        for i, height in enumerate(heightMap[-1]):
            HEAP.append(Tile(mlen - 1, i, height))
            visited[-1][i] = True
        for i in range(mlen):
            HEAP.append(Tile(i, 0, heightMap[i][0]))
            HEAP.append(Tile(i, nlen - 1, heightMap[i][-1]))
            visited[i][0] = True
            visited[i][-1] = True
        heapify(HEAP)

        res = 0
        while HEAP:
            tile = heappop(HEAP)
            m, n, h = tile.m, tile.n, tile.h
            if m < mlen - 1 and not visited[m + 1][n]:
                visited[m + 1][n] = True
                res += max(h - heightMap[m + 1][n], 0)
                heappush(HEAP, Tile(m + 1, n, max(h, heightMap[m + 1][n])))

            if tile.m > 0 and not visited[m - 1][n]:
                visited[m - 1][n] = True
                res += max(h - heightMap[m - 1][n], 0)
                heappush(HEAP, Tile(m - 1, n, max(h, heightMap[m - 1][n])))

            if n < nlen - 1 and not visited[m][n + 1]:
                visited[m][n + 1] = True
                res += max(h - heightMap[m][n + 1], 0)
                heappush(HEAP, Tile(m, n + 1, max(h, heightMap[m][n + 1])))

            if n > 0 and not visited[m][n - 1]:
                visited[m][n - 1] = True
                res += max(h - heightMap[m][n - 1], 0)
                heappush(HEAP, Tile(m, n - 1, max(h, heightMap[m][n - 1])))
        return res


class Tile:
    def __init__(self, m, n, h):
        self.m = m
        self.n = n
        self.h = h

    def __lt__(self, other):
        if self.h < other.h:
            return True
        elif self.h > other.h:
            return False
        else:
            if self.m < other.m:
                return True
            elif self.m > other.m:
                return False
            else:
                return self.n < other.n
