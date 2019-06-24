from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.curMax = -1
        self.buckets = [[]]
        self.numMap = defaultdict(lambda: 0)

    def push(self, x: int) -> None:
        self.numMap[x] += 1
        self.curMax = max(self.curMax, self.numMap[x])
        while len(self.buckets) <= self.numMap[x] + 1:
            self.buckets.append([])
        self.buckets[self.numMap[x]].append(x)

    def pop(self) -> int:
        bucket = self.buckets[self.curMax]
        res = bucket.pop()
        self.numMap[res] -= 1

        while not bucket and self.curMax > 0:
            self.curMax -= 1
            bucket = self.buckets[self.curMax]
        return res
