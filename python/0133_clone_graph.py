class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}
        queue = [node]

        res = UndirectedGraphNode(node.label)
        cloneQueue = [res]
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                source = queue[0]
                queue.pop(0)

                destination = cloneQueue[0]
                cloneQueue.pop(0)

                destination.label = source.label

                for neighbor in source.neighbors:
                    destination.neighbors.append(
                        UndirectedGraphNode(neighbor.label))

                    if neighbor.label not in visited:
                        visited[neighbor.label] = True

                        queue.append(neighbor)
                        cloneQueue.append(destination.neighbors[-1])
        return res