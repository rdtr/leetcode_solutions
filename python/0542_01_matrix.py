from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mlen = len(mat)
        if mlen == 0:
            return mat
        nlen = len(mat[0])
        if nlen == 0:
            return mat

        out = [[0 for x in range(nlen)] for y in range(mlen)]
        
        queue = deque([])
        visited = set([])

        for i in range(mlen):
            for j in range(nlen):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        depth = 0
        while queue:
            qlen = len(queue)
            depth += 1
            for i in range(qlen):
                x, y = queue.popleft()
                for adj in [(x + 1, y), (x , y + 1), (x, y - 1), (x - 1, y)]:
                    if adj[0] >= 0 and adj[0] < mlen and adj[1] >= 0 and adj[1] < nlen and adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
                        out[adj[0]][adj[1]] = depth
        return out
