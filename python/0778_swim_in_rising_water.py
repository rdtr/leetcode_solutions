from heapq import heapify, heappush, heappop


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mlen = len(grid)
        if mlen <= 1:
            return grid[0][0]

        h = [(grid[0][0], 0, 0)]  # day, grid X, grid Y
        heapify(h)
        visited = set()
        while True:
            day, m, n = heappop(h)
            if m == n == mlen - 1:
                return day

            if m > 0 and (m - 1, n) not in visited:
                visited.add((m - 1, n))
                heappush(h, (max(grid[m - 1][n], day), m - 1, n))

            if m < mlen - 1 and (m + 1, n) not in visited:
                visited.add((m + 1, n))
                heappush(h, (max(grid[m + 1][n], day), m + 1, n))
            if n > 0 and (m, n - 1) not in visited:
                visited.add((m, n - 1))
                heappush(h, (max(grid[m][n - 1], day), m, n - 1))

            if n < mlen - 1 and (m, n + 1) not in visited:
                visited.add((m, n + 1))
                heappush(h, (max(grid[m][n + 1], day), m, n + 1))