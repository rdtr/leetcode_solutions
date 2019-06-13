class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        projects = sorted([Project(p, c, i) for p, c, i in zip(Profits, Capital, [i for i in range(len(Profits))])],
                          key=lambda x: x.capital)

        availableProjects = []
        pnum = 0
        i = 0
        curW = W

        while pnum < k:
            while i < len(projects) and projects[i].capital <= curW:
                heapq.heappush(availableProjects, projects[i])
                i += 1

            if not availableProjects:
                break

            prj = heapq.heappop(availableProjects)
            curW += prj.profit
            pnum += 1
        return curW


class Project:
    def __init__(self, profit, capital, i):
        self.profit = profit
        self.capital = capital
        self.id = i

    def __lt__(self, other):
        if self.profit > other.profit:
            return True
        elif self.profit < other.profit:
            return False
        else:
            return self.id < other.id