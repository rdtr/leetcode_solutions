class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        hi = lo = 0
        for w in weights:
            hi += w
            lo = max(lo, w)

        mid = lo + (hi - lo) // 2
        while lo < hi:
            days = self.getDays(weights, mid, D)
            if days > D:
                lo = mid + 1
            else:
                hi = mid
            mid = lo + (hi - lo) // 2
        return hi

    def getDays(self, weights, n, D):
        day = 0
        i = 0
        while i < len(weights):
            remaining = n
            while remaining - weights[i] >= 0:
                remaining -= weights[i]
                i += 1
                if i >= len(weights):
                    break
            day += 1
            if day > D:  # no need to test further
                return day
        return day