class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        parentMap = {}
        rankMap = {}
        for edge in edges:
            if not union(edge[0], edge[1], parentMap, rankMap):
                return edge


def union(n1, n2, parentMap, rankMap):
    p1 = find(n1, parentMap)
    p2 = find(n2, parentMap)
    if p1 == p2:
        return False

    rank1 = 0 if p1 not in rankMap else rankMap[p1]
    rank2 = 0 if p2 not in rankMap else rankMap[p2]

    # using rank to save growing height
    if rank1 > rank2:
        parentMap[p1] = p2
    elif rank2 > rank1:
        parentMap[p2] = p1
    else:
        parentMap[p1] = p2
        rank1 += 1
    rankMap[p1], rankMap[p2] = rank1, rank2
    return True


def find(node, parentMap):
    cur = node
    while cur in parentMap and parentMap[cur] != cur:
        cur = parentMap[cur]
    parentMap[node] = cur  # path compression
    return cur
