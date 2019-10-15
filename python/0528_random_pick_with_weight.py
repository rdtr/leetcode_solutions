from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.sums = [0] * len(w)
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            self.sums[i] = cur

    def pickIndex(self) -> int:
        target = randint(0, self.sums[-1] - 1)

        lo = 0
        hi = len(self.sums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.sums[mid] > target:
                hi = mid
            else:  # self.sums[mid] <= target
                lo = mid + 1

        if lo == len(self.sums):
            return len(self.sums) - 1
        else:
            return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
