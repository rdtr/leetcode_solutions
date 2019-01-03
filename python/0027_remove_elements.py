class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        nlen = len(nums)
        if nlen == 1:
            return 0 if nums[0] == val else 1
        end = nlen - 1

        i = 0
        while i <= end:
            if nums[i] == val:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                continue
            i += 1
        return end + 1
