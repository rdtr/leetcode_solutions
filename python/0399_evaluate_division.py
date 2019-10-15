from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        edges = defaultdict(lambda: {})
        for equation, value in zip(equations, values):
            edges[equation[0]][equation[1]] = (value, 1)  # hold numerator and denominator
            edges[equation[1]][equation[0]] = (1, value)

        visited = set()
        results = [-1.0] * len(queries)
        for i, query in enumerate(queries):
            if query[0] not in edges:
                results[i] = -1.0
                continue
            if query[0] == query[1]:
                results[i] = 1.0
                continue

            visited.add(query[0])
            result = [-1.0]
            self.doCalcEquation(edges, visited, (1.0, 1.0), result, query[0], query[1])
            results[i] = result[0]
            visited.remove(query[0])
        return results

    def doCalcEquation(self, edges, visited, cur, result, start, end):
        neighs = edges[start]
        for neigh, val in neighs.items():
            if neigh in visited:
                continue

            if neigh == end:
                result[0] = (cur[0] * val[0]) / (cur[1] * val[1])
                return

            visited.add(neigh)
            self.doCalcEquation(edges, visited, (cur[0] * val[0], cur[1] * val[1]), result, neigh, end)
            visited.remove(neigh)
