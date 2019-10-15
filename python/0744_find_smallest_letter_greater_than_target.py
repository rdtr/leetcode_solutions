class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        return letters[self.bisect_right(letters, target) % len(letters)]

    def bisect_right(self, nums, target):
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return lo
