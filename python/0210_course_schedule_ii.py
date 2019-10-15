from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incomings = [0 for _ in range(numCourses)]
        directions = [[] for _ in range(numCourses)]

        for p in prerequisites:
            incomings[p[0]] += 1
            directions[p[1]].append(p[0])

        res = []
        starts = [i for i in range(numCourses) if incomings[i] == 0]
        visit = 0
        for start in starts:
            res.append(start)
            visit += 1

            q = deque([start])
            while q:
                qlen = len(q)
                for i in range(qlen):
                    node = q.popleft()
                    nexts = directions[node]
                    for n in nexts:
                        incomings[n] -= 1
                        if incomings[n] == 0:
                            res.append(n)
                            q.append(n)
                            visit += 1
        return res if visit == numCourses else []
