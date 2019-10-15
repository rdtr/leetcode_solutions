from collections import deque

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        neighbors = [[] for _ in range(len(stones))]
        mapX, mapY = {}, {}

        for i, stone in enumerate(stones):
            x, y = stone[0], stone[1]
            if x in mapX:
                neighbors[mapX[x]].append(i)
                neighbors[i].append(mapX[x])
            if y in mapY:
                neighbors[mapY[y]].append(i)
                neighbors[i].append(mapY[y])

            mapX[stone[0]] = i
            mapY[stone[1]] = i

        # BFS
        cnt = 0
        visited = set()
        for i in range(len(neighbors)):
            if i in visited:
                continue
            cnt += 1

            que = deque([i])
            visited.add(i)

            while que:
                qlen = len(que)
                for j in range(qlen):
                    stone = que.popleft()
                    for neigh in neighbors[stone]:
                        if neigh not in visited:
                            que.append(neigh)
                            visited.add(neigh)
        return len(stones) - cnt


class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        mapX, mapY = {}, {}
        nodes = []

        for stone in stones:
            newNode = UFNode(stone)
            newNode.parent = newNode

            if stone[0] in mapX:
                union(mapX[stone[0]], newNode)
            if stone[1] in mapY:
                union(mapY[stone[1]], newNode)
            mapX[stone[0]], mapY[stone[1]] = newNode, newNode
            nodes.append(newNode)

        cnt = 0
        for node in nodes:
            if node.parent != node:
                cnt += 1
        return cnt


def union(node1, node2):
    node1.parent, node2.parent = find(node1), find(node2)

    if node1.parent == node2.parent:
        return

    if node1.parent.rank == node2.parent.rank:
        node1.parent.rank += 1
        node2.parent.parent = node1.parent
    elif node1.parent.rank < node2.parent.rank:
        node1.parent.parent = node2.parent
    else:
        node2.parent.parent = node1.parent


def find(node):
    parent = node.parent
    while parent != node:
        node = parent
        parent = node.parent
    return parent


class UFNode:
    def __init__(self, val, parent=None, rank=0):
        self.rank = 0
        self.val = val
        self.parent = parent
