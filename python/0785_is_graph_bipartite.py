class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        if not graph:
            return False

        visited = {}
        for node in range(len(graph)):
            if node in visited:
                continue
            visited[node] = 0
            if not self.doIsBipartite(graph, visited, node, 1):
                return False
        return True

    def doIsBipartite(self, graph, visited, node, flag):
        nbhrs = graph[node]
        for nbhr in nbhrs:
            if nbhr in visited:
                if visited[nbhr] != flag:
                    return False
                continue

            visited[nbhr] = flag
            if not self.doIsBipartite(graph, visited, nbhr, 1 - flag):
                return False
        return True
