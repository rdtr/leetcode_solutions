from collections import deque

class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.que = deque([])
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.que.append(val)
        if len(self.que) > self.size:
            self.que.popleft()
        return sum(self.que) / len(self.que)