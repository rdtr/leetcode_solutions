class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.cur = None
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while True:
            if self.cur is None and self.i >= len(self.A):
                break
            if self.cur is not None:
                if self.cur[0] > n:
                    self.cur = (self.cur[0] - n, self.cur[1])
                    return self.cur[1]
                n -= self.cur[0]
                if n == 0:
                    tmp = self.cur[1]
                    self.cur = None
                    return tmp
                self.cur = None
            else:
                self.cur = (self.A[self.i], self.A[self.i + 1])
                self.i += 2
        return -1
