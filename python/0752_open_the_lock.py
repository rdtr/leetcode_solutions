from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        cur = "0000"

        deadendsSet = {deadend for deadend in deadends}
        if cur in deadendsSet:
            return -1

        res = 0
        q = deque([cur])
        seen = set(cur)
        while q:
            qlen = len(q)
            for i in range(qlen):
                num = q.popleft()

                if num == target:
                    return res

                for j in range(4):
                    plusOne = (int(num[j]) + 1) % 10
                    newNum = num[:j] + str(plusOne) + num[j+1:]
                    if newNum not in seen and newNum not in deadendsSet:
                        seen.add(newNum)
                        q.append(newNum)

                    minusOne = int(num[j]) - 1
                    if minusOne < 0:
                        minusOne += 10
                    newNum = num[:j] + str(minusOne) + num[j+1:]
                    if newNum not in seen and newNum not in deadendsSet:
                        seen.add(newNum)
                        q.append(newNum)
            res += 1
        return -1
