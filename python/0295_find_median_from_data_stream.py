class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heapq.heappush(self.minheap, num)
        else:
            if num >= self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap) + 1:
            while True:
                num = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -num)
                if len(self.minheap) - len(self.maxheap) <= 1:
                    break
        elif len(self.maxheap) > len(self.minheap):
            while True:
                num = -1 * heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, num)
                if len(self.minheap) - len(self.maxheap) <= 1:
                    break

        if (len(self.minheap) + len(self.maxheap)) % 2 == 1:
            return self.minheap[0]
        else:
            return (self.minheap[0] + -1 * self.maxheap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
