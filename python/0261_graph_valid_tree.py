class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        if len(edges) < n - 1:
            return False

        parentMap = [[] for i in range(n)]
        for edge in edges:
            parentMap[edge[0]].append(edge[1])
            parentMap[edge[1]].append(edge[0])

        allVisited = set()
        for i in range(n):
            if not self.traverse(i, None, parentMap, set(), allVisited):
                return False
        return True

    def traverse(self, node, prev, parentMap, visited, allVisited):
        for parent in parentMap[node]:
            if prev is not None and prev == parent:
                continue

            if parent in visited:  # we detect a cycle
                return False
            if parent in allVisited:  # the node is already examined and passed
                continue
            visited.add(parent)
            allVisited.add(parent)

            if not self.traverse(parent, node, parentMap, visited, allVisited):
                return False
            visited.remove(parent)
        return True
