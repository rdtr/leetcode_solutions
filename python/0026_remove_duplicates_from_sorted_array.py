class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nlen = len(nums)
        if nlen == 0:
            return 0

        prev = nums[0]
        left, right = 1, 1
        while True:
            if right > len(nums) - 1:
                break

            if nums[right] == prev:
                right += 1
                continue

            nums[left], nums[right] = nums[right], nums[left]
            prev = nums[left]
            left += 1
            right += 1

        nums = nums[:left]
        return left
