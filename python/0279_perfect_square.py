from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        visited = set([0])
        q = deque([0])

        depth = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                num = q.popleft()

                j = 1
                while num + j * j <= n:
                    k = num + j * j
                    if k == n:
                        return depth + 1
                    if k in visited:
                        j += 1
                        continue

                    visited.add(k)
                    q.append(k)
                    j += 1
            depth += 1
        return 0
