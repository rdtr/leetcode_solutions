class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        nodeMap = {}
        count = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    if (m, n) not in nodeMap:
                        nodeMap[(m, n)] = FUNode(m, n)
                        count += 1

                    if m > 0 and grid[m - 1][n] == "1":
                        if (m - 1, n) not in nodeMap:
                            nodeMap[(m - 1, n)] = FUNode(m - 1, n)
                            count += 1
                        count = Union(nodeMap[(m, n)], nodeMap[(m - 1, n)], count)
                    if n > 0 and grid[m][n - 1] == "1":
                        if (m, n - 1) not in nodeMap:
                            nodeMap[(m, n - 1)] = FUNode(m, n - 1)
                            count += 1
                        count = Union(nodeMap[(m, n)], nodeMap[(m, n - 1)], count)

        return count


class FUNode:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.rank = 0
        self.parent = self


def Union(node1, node2, count):
    node1.parent, node2.parent = Find(node1), Find(node2)

    if node1.parent == node2.parent:
        return count

    if node1.parent.rank == node2.parent.rank:
        node1.parent.rank += 1
        node2.parent.parent = node1.parent
    elif node1.parent.rank < node2.parent.rank:
        node1.parent.parent = node2.parent
    else:
        node2.parent.parent = node1.parent
    return count - 1


def Find(node):
    parent = node.parent
    nodes = []
    while node != parent:
        nodes.append(node)
        node = parent
        parent = node.parent

    for node in nodes:
        node.parent = parent
    return parent
