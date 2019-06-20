class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nlen = len(nums)
        if nlen == 0:
            return []

        left = right = 0
        while True:
            while right < nlen and nums[right] == 0:
                right += 1
            if right == nlen:
                break

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1

        for i in range(right, nlen):
            nums[i] = 0
