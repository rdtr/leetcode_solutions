from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graphs = [[] for _ in range(n)]
        neighborNums = [0] * n
        for e in edges:
            graphs[e[0]].append(e[1])
            graphs[e[1]].append(e[0])

        leaves = deque([i for i, graph in enumerate(graphs) if len(graph) == 1])
        while n > 2:
            llen = len(leaves)
            for i in range(llen):
                leaf = leaves.popleft()
                neighbors = graphs[leaf]

                for neigh in neighbors:
                    graphs[neigh].remove(leaf)

                    if len(graphs[neigh]) == 1:
                        leaves.append(neigh)
                n -= 1

        return list(leaves) or [0]
