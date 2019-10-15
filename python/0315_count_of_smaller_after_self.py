class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        appear = collections.Counter(nums)
        numSet = sorted(appear.keys())

        BIT = [0] * (len(numSet) + 1)
        for i in range(0, len(numSet)):
            self.update(BIT, i + 1, appear[numSet[i]])

        res = [0] * len(nums)
        for i in range(0, len(nums)):
            index = self.search(numSet, nums[i])

            self.update(BIT, index + 1, -1)

            res[i] = self.query(BIT, index)

        return res

    def search(self, arr, num):
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if arr[mid] == num:
                return mid
            elif arr[mid] > num:
                hi = mid - 1
            else:
                lo = mid

            if lo == hi:
                break
            if lo == hi - 1:
                if arr[lo] == num:
                    return lo
                else:
                    return hi
        return lo

    def update(self, BIT, i, diff):
        while i < len(BIT):
            BIT[i] += diff
            i += i & -i

    def query(self, BIT, i):
        res = 0
        while i > 0:
            res += BIT[i]
            i -= i & -i
        return res
