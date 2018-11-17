class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nlen = len(nums)
        if nlen == 0:
            return 1

        i = 0
        while i < nlen:
            num = nums[i]

            if i + 1 == num:
                i += 1
                continue

            if num > 0 and num <= nlen and nums[num - 1] != num:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
            else:
                i += 1

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return nlen + 1
