class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1], reverse=True)
        m = {}
        for t in tickets:
            if t[0] not in m:
                m[t[0]] = [t[1]]
            else:
                m[t[0]].append(t[1])

        circuit = []
        curpath = ['JFK']
        while curpath:
            if curpath[-1] in m and m[curpath[-1]]:
                next = m[curpath[-1]].pop()
                curpath.append(next)
            else:
                circuit.append(curpath[-1])
                curpath.pop()
        return circuit[::-1]
