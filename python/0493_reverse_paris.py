class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nlen = len(nums)

        appear = {}
        for i in range(nlen):
            if nums[i] not in appear:
                appear[nums[i]] = 1
            else:
                appear[nums[i]] += 1

        numsSorted = sorted(appear.keys())
        BIT = [0] * (len(numsSorted) + 1)
        for i, num in enumerate(numsSorted):
            self.updateBIT(BIT, i + 1, appear[num])

        res = 0
        for i in range(nlen - 1, -1, -1):
            self.updateBIT(BIT, self.search(numsSorted, nums[i]), -1)
            j = self.search(numsSorted, nums[i] * 2)
            if j < len(numsSorted):
                res += self.queryBIT(BIT, len(BIT) - 1) - self.queryBIT(BIT, j)

        return res

    def updateBIT(self, bit, i, diff):
        while i < len(bit):
            bit[i] += diff
            i += i & (-i)

    def queryBIT(self, bit, i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & (-i)
        return res

    def search(self, arr, val):
        lo, hi = 0, len(arr) - 1

        while lo <= hi:
            if lo == hi:
                if arr[lo] > val:
                    return lo
                return lo + 1

            mid = lo + (hi - lo) / 2
            if arr[mid] > val:
                hi = mid
            else:
                lo = mid + 1

