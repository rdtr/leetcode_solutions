class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.BIT = [0] * (len(nums) + 1)
        self.nums = nums

        for i, val in enumerate(nums):
            self.add(i, val)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.add(i, diff)

    def add(self, i, val):
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & -i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum_j = 0
        j += 1
        while j > 0:
            sum_j += self.BIT[j]
            j -= j & -j

        if i == 0:
            return sum_j

        sum_i = 0
        if i > 0:
            while i > 0:
                sum_i += self.BIT[i]
                i -= i & -i
        return sum_j - sum_i