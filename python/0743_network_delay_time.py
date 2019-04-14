from collections import defaultdict
from heapq import heapify, heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        m = defaultdict(lambda: [])
        for item in times:
            m[item[0]].append((item[1], item[2]))

        h = [(K, 0)]
        heapify(h)
        minTimes = [-1 if i != K - 1 else 0 for i in range(N)]
        received = set([K])

        while h:
            u, timeSoFar = heappop(h)
            for v, w in m[u]:
                received.add(v)
                if minTimes[v - 1] == -1 or timeSoFar + w < minTimes[v - 1]:
                    minTimes[v - 1] = timeSoFar + w
                    heappush(h, (v, minTimes[v - 1]))

        return -1 if len(received) != N else max(minTimes)