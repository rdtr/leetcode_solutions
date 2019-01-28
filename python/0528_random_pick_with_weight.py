class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.sums = [0] * len(w)
        self.sums[0] = w[0]
        for i in range(1, len(w)):
            self.sums[i] = self.sums[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """

        target = random.randint(1, self.sums[-1])

        i = self.bisect_right(self.sums, target)
        return i - 1 if self.sums[i - 1] == target else i

    def bisect_right(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return hi

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
