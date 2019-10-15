class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.series = [0] * len(persons)
        vote = [0] * len(persons)
        win = -1
        for i, time in enumerate(times):
            person = persons[i]
            vote[person] += 1

            if vote[person] >= win:
                self.series[i] = person
                win = vote[person]
            else:
                self.series[i] = self.series[i - 1]

    def q(self, t: int) -> int:
        return self.series[self.bisect_right(t, self.times) - 1]

    def bisect_right(self, target, nums):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return hi
